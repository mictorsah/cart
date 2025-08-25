#Shopping Cart application

item = input("Enter item name: ")
price = input("Price of item: ")
qty = int(input("Enter Quantity: "))


total = price * qty

if qty > 1:
    print(f"Total for {qty} {item}s is {total}")
else:
    print(f"Total for {qty} {item} is {total}")

