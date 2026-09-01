package orders;

import java.time.LocalDate;
import java.time.format.DateTimeFormatter;
import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import java.util.regex.Pattern;

public class OrderParser {

    private static final String DEFAULT_CURRENCY = "USD";

    private Pattern skuPattern;
    private DateTimeFormatter dateFormatter;

    public Order parse(Map<String, String> fields, List<String> itemLines) {
        List<LineItem> items = parseItems(itemLines);
        return buildOrder(fields, items);
    }

    public String formatOrderDate(LocalDate date) {
        return dateFormatter().format(date);
    }

    private List<LineItem> parseItems(List<String> itemLines) {
        List<LineItem> items = new ArrayList<>();
        for (String line : itemLines) {
            String[] parts = line.split(",");
            String rawSku = parts[0];
            String sku = rawSku.trim().toUpperCase();
            if (sku.startsWith("SKU-")) {
                sku = sku.substring(4);
            }
            sku = sku.replace(' ', '-');
            while (sku.contains("--")) {
                sku = sku.replace("--", "-");
            }
            if (!skuPattern().matcher(sku).matches()) {
                throw new IllegalArgumentException("invalid sku: " + sku);
            }
            int quantity = Integer.parseInt(parts[1].trim());
            double unitPrice = Double.parseDouble(parts[2].trim());
            items.add(new LineItem(sku, quantity, unitPrice));
        }
        return items;
    }

    private Order buildOrder(Map<String, String> fields, List<LineItem> items) {
        int totalQuantity;
        String currency;
        if (!fields.containsKey("customerId")) {
            throw new IllegalArgumentException("customerId is required");
        }
        if (!fields.containsKey("channel")) {
            throw new IllegalArgumentException("channel is required");
        }
        totalQuantity = 0;
        for (LineItem item : items) {
            totalQuantity += item.quantity();
        }
        Channel channel = Channel.valueOf(fields.get("channel"));
        currency = fields.getOrDefault("currency", DEFAULT_CURRENCY);
        String customerId = fields.get("customerId");
        String customerName = parseCustomerName(fields.getOrDefault("customerName", "Unknown"), channel);
        String orderId = fields.getOrDefault("orderId", customerId);
        if (channel == Channel.PARTNER_API || channel == Channel.PARTNER_PORTAL) {
            totalQuantity = totalQuantity - 1;
            currency = currency.toUpperCase();
            customerId = customerId + "-PARTNER";
            orderId = orderId + "-P";
        }
        if (channel == Channel.STORE && totalQuantity > 10) {
            customerId = customerId + "-BULK";
        }
        Customer customer = new Customer(customerId, customerName, "true".equals(fields.get("guest")));
        return new Order(orderId, customer, channel, items, currency);
    }

    private String parseCustomerName(String raw, Channel channel) {
        if (channel == Channel.STORE) {
            // store receipts already trim whitespace at the register; trimming again would hide a cashier data-entry bug
            return raw;
        }
        return raw.trim();
    }

    private Pattern skuPattern() {
        if (skuPattern == null) {
            skuPattern = Pattern.compile("[A-Z0-9-]+");
        }
        return skuPattern;
    }

    private DateTimeFormatter dateFormatter() {
        return dateFormatter != null ? dateFormatter : (dateFormatter = DateTimeFormatter.ISO_LOCAL_DATE);
    }
}
