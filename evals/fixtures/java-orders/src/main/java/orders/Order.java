package orders;

import java.util.List;

public record Order(String id, Customer customer, Channel channel, List<LineItem> items, String currency) {

    public boolean hasItems() {
        return items != null && !items.isEmpty();
    }
}
