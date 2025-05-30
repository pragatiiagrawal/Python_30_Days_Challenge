# Challenge: Inventory Tracking System 
print('''\n****** Welcome to our Inventory Store ******\n''')

# Inventory Dictionary 
store = {
    'Printer': 10,
    'Desktop': 50,
    'Mouse': 25,
}
# Function to view items present in store
def view_items():
    if not store:
        print("Oops, store is out of stock! Come later.")
    else:
        print("\nInventory stock:")
        for item, qty in store.items():
            print(f" → {item} : {qty}")
# Function to add items in store
def add_item():
    item = input("Enter the item name: ").title()
    if item in store:
        print("The item is already in stock, select 3 to update.")
    else:
        try:
            qty = int(input("Enter the quantity: "))
        except ValueError:
            print("Invalid quantity! Please enter a number.")
        return
        store[item] = qty
        print(f"{item} added to the store.")
# Function to update items present in stock
def update_item():
    item = input("Enter the name of the item to update: ").title()
    if item in store:
        try:
            qty = int(input("Enter the quantity to add: "))
        except ValueError:
            print("Invalid quantity! Please enter a number.")
            return
        store[item] += qty
        print(f"{item} quantity is updated to {store[item]}.")
    else:
        print("This item is not present in store, kindly select '2' to add the item.")
# Function to remove items from the store
def remove_item():
    item = input("Enter the name of the item to remove: ").title()
    if item in store:
        try:
            qty = int(input("Enter the quantity to remove: "))
        except ValueError:
            print("Invalid quantity! Please enter a number.")
            return
        if qty <= store[item]:
            store[item] -= qty
            if store[item] == 0:
                del store[item]
                print(f"{item} is now out of stock and removed from store.")
            else:
                print(f"{item} quantity is now updated to {store[item]}.")
        else:
            print(f"Cannot remove {qty} units. Only {store[item]} units available.")
    else:
        print("This item is not present in store, kindly select '2' to add the item.")
# Main loop
while True:
    print('\n')
    print("** Press '1' : To view all items in the store.")
    print("** Press '2' : To add new items in the store.")
    print("** Press '3' : To update the items in the store.")
    print("** Press '4' : To delete item in the store.")
    print("** Press '5' : To exit from in the store.")

    select = input("Enter your choice: 1-5 → ")

    if select == '1':
        view_items()
    elif select == '2':
        add_item()
    elif select == '3':
        update_item()
    elif select == '4':
        remove_item()
    elif select == '5':
        print("****** Thank you for using Inventory Store. Goodbye! ******")
        break
    else:
        print("Invalid choice! Please enter a number from 1 to 5.")
