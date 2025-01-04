def add_item(cart):
    item=input("Enter item name:")
    price=float(input(f"Enter price of {item}:"))
    quantity=int(input(f"Enter quantity of {item}:"))
    cart.append((item,price,quantity))
def display_bill(cart):
    print("\n-----Your Bill-----")
    total=0
    for item,price,quantity in cart:
        total+=price*quantity
        
