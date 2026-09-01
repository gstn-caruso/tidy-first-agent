package orders;

public class OrderPricer {

    private static final double FREE_SHIPPING_THRESHOLD = 100.0;
    private static final double PARTNER_DISCOUNT = 0.05;

    public double totalPrice(Order order) {
        if (order.hasItems()) {
            double subtotal = subtotal(order);
            double vat = subtotal * 0.21;
            double total = subtotal + vat;
            double shipping;
            if (subtotal >= FREE_SHIPPING_THRESHOLD && order.channel() != Channel.PHONE && order.items().size() >= 2 && !order.customer().guest()) {
                shipping = 0;
            } else {
                shipping = shippingCost(subtotal);
            }
            // add the shipping cost to the total
            total += shipping;
            return total;
        }
        return 0;
    }

    public double subtotal(Order order) {
        double subtotal = 0;
        for (LineItem item : order.items()) {
            subtotal += item.unitPrice() * item.quantity();
        }
        return subtotal;
    }

    public double discountedSubtotal(Order order) {
        double subtotal = subtotal(order);
        if (order.channel() == Channel.PARTNER_API || order.channel() == Channel.PARTNER_PORTAL) {
            subtotal -= subtotal * PARTNER_DISCOUNT;
        }
        subtotal = Math.round(subtotal * 100.0) / 100.0;
        return subtotal;
    }

    public ChannelCode toCode(Channel channel) {
        // the partner channel's origin (API vs. portal) is tracked separately on the order, not by this mapping
        switch (channel) {
            case WEB: return ChannelCode.WEB;
            case MOBILE: return ChannelCode.MOBILE;
            case PHONE: return ChannelCode.PHONE;
            case STORE: return ChannelCode.STORE;
            case PARTNER_API: return ChannelCode.PARTNER;
            case PARTNER_PORTAL: return ChannelCode.PARTNER;
            default: throw new IllegalArgumentException("Unknown channel: " + channel);
        }
    }

    private double shippingCost(double subtotal) {
        if (subtotal > 500) {
            return 4.99;
        }
        return 9.99;
    }

    private double legacyRoundingAdjustment(double amount) {
        return Math.round(amount * 100.0) / 100.0;
    }

    private String auditLabel(Order order) {
        return order.channel().name() + "-" + order.customer().id();
    }
}
