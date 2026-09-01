package orders;

import org.junit.jupiter.api.Test;

import java.util.List;

import static org.junit.jupiter.api.Assertions.assertEquals;

class OrderPricerHiddenTest {

    private final OrderPricer pricer = new OrderPricer();

    private static Customer customer(String id) {
        return new Customer(id, "Jane Doe", false);
    }

    @Test
    void zeroQuantityItemContributesNothingToSubtotalButShippingStillApplies() {
        LineItem zeroQty = new LineItem("A1", 0, 10.0);
        Order order = new Order("O1", customer("C1"), Channel.WEB, List.of(zeroQty), "USD");

        // subtotal = 0, vat = 0, shipping = 9.99 (below the free-shipping threshold)
        assertEquals(9.99, pricer.totalPrice(order), 0.001);
    }

    @Test
    void negativeUnitPriceIsHandledArithmeticallyAsWrittenNotRejected() {
        LineItem negative = new LineItem("A1", 1, -20.0);
        Order order = new Order("O2", customer("C2"), Channel.WEB, List.of(negative), "USD");

        // subtotal = -20, vat = -4.2, shipping = 9.99 -> total = -14.21
        assertEquals(-14.21, pricer.totalPrice(order), 0.001);
    }

    @Test
    void totalIsCorrectToTheCentOnNonRoundSubtotals() {
        LineItem item = new LineItem("A1", 1, 19.99);
        Order order = new Order("O3", customer("C3"), Channel.WEB, List.of(item), "USD");

        // subtotal = 19.99, vat = 4.1979, shipping = 9.99 -> total = 34.1779
        assertEquals(34.1779, pricer.totalPrice(order), 0.001);
    }
}
