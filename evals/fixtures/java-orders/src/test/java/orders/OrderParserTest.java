package orders;

import org.junit.jupiter.api.Test;

import java.lang.reflect.Field;
import java.time.LocalDate;
import java.util.List;
import java.util.Map;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertSame;
import static org.junit.jupiter.api.Assertions.assertThrows;

class OrderParserTest {

    private final OrderParser parser = new OrderParser();

    @Test
    void happyPathParsesFieldsAndNormalizesSkus() {
        Map<String, String> fields = Map.of(
                "customerId", "C100",
                "channel", "WEB",
                "currency", "EUR",
                "customerName", " Jane Doe ");
        List<String> itemLines = List.of("sku-abc, 2, 10.50", "widget 1,1,5.00");

        Order order = parser.parse(fields, itemLines);

        assertEquals("C100", order.id());
        assertEquals("C100", order.customer().id());
        assertEquals("Jane Doe", order.customer().name());
        assertFalse(order.customer().guest());
        assertEquals(Channel.WEB, order.channel());
        assertEquals("EUR", order.currency());
        assertEquals(2, order.items().size());
        assertEquals(new LineItem("ABC", 2, 10.50), order.items().get(0));
        assertEquals(new LineItem("WIDGET-1", 1, 5.00), order.items().get(1));
    }

    @Test
    void currencyDefaultsToUsdWhenFieldMissing() {
        Map<String, String> fields = Map.of("customerId", "C101", "channel", "WEB");
        List<String> itemLines = List.of("A1,1,9.00");

        Order order = parser.parse(fields, itemLines);

        assertEquals("USD", order.currency());
    }

    @Test
    void partnerChannelsUppercaseCurrencyAndTagIds() {
        Map<String, String> fields = Map.of("customerId", "C200", "channel", "PARTNER_API", "currency", "usd");
        List<String> itemLines = List.of("X1,1,10.00");

        Order order = parser.parse(fields, itemLines);

        assertEquals("C200-P", order.id());
        assertEquals("C200-PARTNER", order.customer().id());
        assertEquals("USD", order.currency());
    }

    @Test
    void storeChannelTagsBulkOrdersOverTenUnits() {
        Map<String, String> fields = Map.of("customerId", "C300", "channel", "STORE");
        List<String> itemLines = List.of("A1,11,2.00");

        Order order = parser.parse(fields, itemLines);

        assertEquals("C300-BULK", order.customer().id());
    }

    @Test
    void storeChannelKeepsNameAsIsButOtherChannelsTrimIt() {
        Map<String, String> storeFields = Map.of("customerId", "C400", "channel", "STORE", "customerName", " Bob ");
        Map<String, String> webFields = Map.of("customerId", "C401", "channel", "WEB", "customerName", " Bob ");
        List<String> itemLines = List.of("A1,1,2.00");

        Order storeOrder = parser.parse(storeFields, itemLines);
        Order webOrder = parser.parse(webFields, itemLines);

        assertEquals(" Bob ", storeOrder.customer().name());
        assertEquals("Bob", webOrder.customer().name());
    }

    @Test
    void invalidSkuCharactersAreRejected() {
        Map<String, String> fields = Map.of("customerId", "C500", "channel", "WEB");
        List<String> itemLines = List.of("@@@,1,5.00");

        assertThrows(IllegalArgumentException.class, () -> parser.parse(fields, itemLines));
    }

    @Test
    void lazyFieldsAreInitializedOnlyOnce() throws Exception {
        Map<String, String> fields = Map.of("customerId", "C600", "channel", "WEB");
        List<String> itemLines = List.of("A1,1,2.00");

        Field skuPatternField = OrderParser.class.getDeclaredField("skuPattern");
        skuPatternField.setAccessible(true);
        Field dateFormatterField = OrderParser.class.getDeclaredField("dateFormatter");
        dateFormatterField.setAccessible(true);

        parser.parse(fields, itemLines);
        parser.formatOrderDate(LocalDate.of(2024, 1, 1));
        Object firstPattern = skuPatternField.get(parser);
        Object firstFormatter = dateFormatterField.get(parser);

        parser.parse(fields, itemLines);
        parser.formatOrderDate(LocalDate.of(2024, 2, 2));
        Object secondPattern = skuPatternField.get(parser);
        Object secondFormatter = dateFormatterField.get(parser);

        assertSame(firstPattern, secondPattern);
        assertSame(firstFormatter, secondFormatter);
    }

    @Test
    void formatsOrderDateInIsoForm() {
        assertEquals("2024-01-15", parser.formatOrderDate(LocalDate.of(2024, 1, 15)));
    }
}
