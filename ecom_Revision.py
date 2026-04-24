def add_product(product_name: str, price: float, quantity: int) -> dict:
    """
    Creates a dictionary object for a product.
    """
    if price < 0 or quantity < 0:
        raise ValueError("Price and quantity cannot be negative")
    return {
        "product_name": product_name,
        "price": price,
        "quantity": quantity
    }

def update_price(product: dict, new_price: float) -> dict:
    """
    Updates the price of the product in the dictionary.
    """
    if new_price < 0:
        raise ValueError("New price cannot be negative")
    product["price"] = new_price
    return product

def update_quantity(product: dict, quantity_change: int) -> dict:
    """
    Updates the quantity of the product in the dictionary.
    """
    if product["quantity"] + quantity_change < 0:
        raise ValueError("Quantity cannot become negative")
    product["quantity"] += quantity_change
    return product

# Example Usage:
my_product = add_product("Laptop", 1200.00, 10)
print(f"Initial Product: {my_product}")
my_product = update_price(my_product, 1150.00)
print(f"Updated Price: {my_product}")
my_product = update_quantity(my_product, -3)
print(f"Updated Quantity: {my_product}")
