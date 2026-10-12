price = float(input("Enter the price of the item: "))
discount_percentage = float(input("Enter the discount percentage: "))
discount_amount = price * (discount_percentage / 100)
final_price = price - discount_amount
print("The final price after discount is:", final_price)