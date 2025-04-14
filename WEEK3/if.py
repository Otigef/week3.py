def calculate_discount(price, discount_percent):
    """
    Calculates the final price after applying a discount.
    Applies the discount only if it's 20% or higher.

    Parameters:
    - price (float): The original price of the item.
    - discount_percent (float): The discount percentage to apply.

    Returns:
    - float: The final price after applying the discount (if applicable).
    """
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price

# Prompt the user for input
try:
    original_price = float(input("Enter the original price of the item: "))
    discount_percentage = float(input("Enter the discount percentage: "))

    # Calculate the final price
    final_price = calculate_discount(original_price, discount_percentage)

    # Display the result
    if discount_percentage >= 20:
        print(f"Discount applied. The final price is: {final_price:.2f}")
    else:
        print(f"No discount applied. The price remains: {original_price:.2f}")
except ValueError:
    print("Invalid input. Please enter numeric values for price and discount percentage.")
