import json
menu = []
orders = []


try:
    with open('menu.json') as f:
        menu = json.load(f)
    with open('orders.json') as f:
        orders = json.load(f)
except FileNotFoundError:
    pass


def save_data():
   
    with open('menu.json', 'w') as f:
        json.dump(menu, f)
    with open('orders.json', 'w') as f:
        json.dump(orders, f)


def print_menu():
    print("\n--- Menu ---")
    for dish in menu:
        availability = "Available" if dish['availability'] else "Not Available"
        print(f"{dish['dish_id']}. {dish['dish_name']} - ${dish['price']} ({availability})")


def add_dish():
    dish_id = input("Enter the dish ID: ")
    dish_name = input("Enter the dish name: ")
    price = float(input("Enter the price: "))
    availability = input("Is the dish available? (yes/no): ").lower() == "yes"
    menu.append({'dish_id': dish_id, 'dish_name': dish_name, 'price': price, 'availability': availability})
    print("Dish added successfully!")


def remove_dish():
    dish_id = input("Enter the dish ID to remove: ")
    for dish in menu:
        if dish['dish_id'] == dish_id:
            menu.remove(dish)
            print("Dish removed successfully!")
            break
    else:
        print("Dish not found!")


def update_dish_availability():
    dish_id = input("Enter the dish ID to update availability: ")
    for dish in menu:
        if dish['dish_id'] == dish_id:
            availability = input("Is the dish available now? (yes/no): ").lower() == "yes"
            dish['availability'] = availability
            print("Dish availability updated successfully!")
            break
    else:
        print("Dish not found!")


def take_order():
    customer_name = input("Enter the customer name: ")
    order_items = input("Enter the dish IDs (comma-separated): ").split(',')
    order = {'order_id': len(orders) + 1, 'customer_name': customer_name, 'order_items': order_items, 'status': 'received'}
    orders.append(order)
    print(f"Order taken successfully! Order ID: {order['order_id']}")


def update_order_status():
    order_id = int(input("Enter the order ID to update status: "))
    for order in orders:
        if order['order_id'] == order_id:
            status = input("Enter the new status: ")
            order['status'] = status
            print("Order status updated successfully!")
            break
    else:
        print("Order not found!")


def review_orders():
    print("\n--- Orders ---")
    for order in orders:
        print(f"Order ID: {order['order_id']}")
        print(f"Customer Name: {order['customer_name']}")
        print(f"Order Items: {', '.join(order['order_items'])}")
        print(f"Status: {order['status']}")
        print()

while True:
    print("\n--- Zesty Zomato ---")
    print("1. Print Menu")
    print("2. Add Dish")
    print("3. Remove Dish")
    print("4. Update Dish Availability")
    print("5. Take Order")
    print("6. Update Order Status")
    print("7. Review Orders")
    print("8. Exit")
    
    choice = input("Enter your choice (1-8): ")

    if choice == '1':
        print_menu()
    elif choice == '2':
        add_dish()
    elif choice == '3':
        remove_dish()
    elif choice == '4':
        update_dish_availability()
    elif choice == '5':
        take_order()
    elif choice == '6':
        update_order_status()
    elif choice == '7':
        review_orders()
    elif choice == '8':
        save_data()
        print("Thanku for using it please visit Once again!")
        break
    else:
        print("Wrong data you enter please try again!")

