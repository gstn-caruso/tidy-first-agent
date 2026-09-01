package orders;

import org.junit.jupiter.api.Test;

import java.lang.reflect.Method;
import java.util.List;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertThrows;

class OrderPricerTest {

    private final OrderPricer pricer = new OrderPricer();

    private static Customer customer(String id) {
        return new Customer(id, "Jane Doe", false);
    }

    @Test
    void emptyOrderTotalsToZero() {
        Order order = new Order("O1", customer("C1"), Channel.WEB, List.of(), "USD");

        assertEquals(0, pricer.totalPrice(order));
    }

    @Test
    void vatAppliedAndShippingWaivedAtFreeShippingThreshold() {
        LineItem a = new LineItem("A1", 2, 30.0);
        LineItem b = new LineItem("B2", 1, 40.0);
        Order order = new Order("O2", customer("C2"), Channel.WEB, List.of(a, b), "USD");

        // subtotal = 100.0, vat = 21.0, free shipping applies (>= threshold, >= 2 items, not phone, not guest)
        assertEquals(121.0, pricer.totalPrice(order), 0.001);
    }

    @Test
    void shippingChargedJustBelowFreeShippingThreshold() {
        LineItem a = new LineItem("A1", 1, 59.99);
        LineItem b = new LineItem("B2", 1, 40.00);
        Order order = new Order("O3", customer("C3"), Channel.WEB, List.of(a, b), "USD");

        // subtotal = 99.99, vat = 20.9979, shipping = 9.99 (below threshold)
        assertEquals(130.9779, pricer.totalPrice(order), 0.001);
    }

    @Test
    void shippingChargedWhenOnlyOneLineItemEvenAboveThreshold() {
        LineItem a = new LineItem("A1", 1, 150.0);
        Order order = new Order("O4", customer("C4"), Channel.WEB, List.of(a), "USD");

        // subtotal = 150.0, vat = 31.5, shipping = 9.99 (only one line item, free shipping needs >= 2)
        assertEquals(191.49, pricer.totalPrice(order), 0.001);
    }

    @Test
    void shippingChargedOnPhoneChannelEvenAboveThreshold() {
        LineItem a = new LineItem("A1", 2, 60.0);
        LineItem b = new LineItem("B2", 1, 40.0);
        Order order = new Order("O5", customer("C5"), Channel.PHONE, List.of(a, b), "USD");

        // subtotal = 160.0, vat = 33.6, shipping = 9.99 (phone channel never gets free shipping)
        assertEquals(203.59, pricer.totalPrice(order), 0.001);
    }

    @Test
    void shippingChargedForGuestCustomerEvenAboveThreshold() {
        LineItem a = new LineItem("A1", 2, 60.0);
        LineItem b = new LineItem("B2", 1, 40.0);
        Order order = new Order("O6", new Customer("C6", "Guest", true), Channel.WEB, List.of(a, b), "USD");

        // subtotal = 160.0, vat = 33.6, shipping = 9.99 (guest customers never get free shipping)
        assertEquals(203.59, pricer.totalPrice(order), 0.001);
    }

    @Test
    void partnerChannelsGetDiscountRoundedToTheCent() {
        LineItem a = new LineItem("A1", 1, 100.0);
        Order apiOrder = new Order("O7", customer("C7"), Channel.PARTNER_API, List.of(a), "USD");
        Order portalOrder = new Order("O8", customer("C8"), Channel.PARTNER_PORTAL, List.of(a), "USD");
        Order webOrder = new Order("O9", customer("C9"), Channel.WEB, List.of(a), "USD");

        assertEquals(95.0, pricer.discountedSubtotal(apiOrder), 0.001);
        assertEquals(95.0, pricer.discountedSubtotal(portalOrder), 0.001);
        assertEquals(100.0, pricer.discountedSubtotal(webOrder), 0.001);
    }

    @Test
    void mapsAllSixChannelsToTheirCode() {
        assertEquals(ChannelCode.WEB, pricer.toCode(Channel.WEB));
        assertEquals(ChannelCode.MOBILE, pricer.toCode(Channel.MOBILE));
        assertEquals(ChannelCode.PHONE, pricer.toCode(Channel.PHONE));
        assertEquals(ChannelCode.STORE, pricer.toCode(Channel.STORE));
        assertEquals(ChannelCode.PARTNER, pricer.toCode(Channel.PARTNER_API));
        assertEquals(ChannelCode.PARTNER, pricer.toCode(Channel.PARTNER_PORTAL));
    }

    @Test
    void auditLabelIsInvokedReflectivelyByThisTest() throws Exception {
        Order order = new Order("O10", customer("C10"), Channel.WEB, List.of(), "USD");

        Method auditLabel = OrderPricer.class.getDeclaredMethod("auditLabel", Order.class);
        auditLabel.setAccessible(true);
        String label = (String) auditLabel.invoke(pricer, order);

        assertEquals("WEB-C10", label);
    }

    @Test
    void unknownChannelIsRejectedByEnumValueOf() {
        assertThrows(IllegalArgumentException.class, () -> Channel.valueOf("CARRIER_PIGEON"));
    }
}
