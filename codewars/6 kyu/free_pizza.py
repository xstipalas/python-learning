from typing import Iterator

def pizza_rewards(customers: dict[str, list[int]], min_orders: int, min_price: int) -> Iterator[str]:
    return (name for name, orders in customers.items() if sum(1 for order in orders if order >= min_price) >= min_orders)

# Example usage:
customers = {
    "Alice": [10, 15, 20],
    "Bob": [5, 12, 18],
    "Charlie": [25, 30, 35]
}
print(list(pizza_rewards(customers, 2, 15)))