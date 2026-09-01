package orders;

import org.junit.jupiter.api.Test;

import java.util.List;
import java.util.Map;

import static org.junit.jupiter.api.Assertions.assertEquals;

class OrderParserHiddenTest {

    private final OrderParser parser = new OrderParser();

    @Test
    void missingOptionalCustomerNameDefaultsToUnknown() {
        Map<String, String> fields = Map.of("customerId", "C900", "channel", "WEB");
        List<String> itemLines = List.of("A1,1,5.00");

        Order order = parser.parse(fields, itemLines);

        assertEquals("Unknown", order.customer().name());
    }

    @Test
    void whitespaceInsideSkusIsCollapsedToASingleDash() {
        Map<String, String> fields = Map.of("customerId", "C901", "channel", "WEB");
        List<String> itemLines = List.of(" wid  get1 , 3 , 2.50");

        Order order = parser.parse(fields, itemLines);

        assertEquals("WID-GET1", order.items().get(0).sku());
    }
}
