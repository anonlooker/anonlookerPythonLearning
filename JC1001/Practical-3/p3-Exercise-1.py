#1) An online retailer offers discounts on the total number of items purchased based
#on the following criteria:
#• No discount for less than 10 items
#• 20% discount for purchases with between 10 and 19 items
#• 30% discount for purchases with between 20 and 30 items
#• 50% discount for purchases with more than 30 items
#Write a program that asks the user to enter the total number of items purchased,
#followed by the price of the sum of all items and then displays the final amount to
#pay, considering any discounts that are applicable.
num_items = int(input("Enter the total number of items purchased: "))
total_price = float(input("Enter the total price of all items: "))
if num_items < 10:
    discount = 0
elif num_items < 20:
    discount = 0.2
elif num_items < 31:
    discount = 0.3
else:
    discount = 0.5
final_amount = total_price - (total_price * discount)
print("Final amount to pay: %.2f" % final_amount)
#p3-Exercise-1.py