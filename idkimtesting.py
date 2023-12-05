def add_customer():
    new_cust_id = len(customers) + 1
    name = input("enter customer name: ")
    contact = input("enter customer contact: ")
    customers[new_cust_id] = {"Name": name, "Contact": contact, "Orders": []}
    print(f'customer {new_cust_id} added successfully.')


def report_single():
    cust_id = int(input("customer ID to find customer info: "))
    if cust_id in customers:
        print(f'\ncustomer ID: {cust_id}')
        for key, value in customers[cust_id].items():
            print(f'{key}: {value}')
    else:
        print(f'customer ID {cust_id} not found.')





def add_order():
    cust_id = int(input("Enter customer ID to place an order: "))
    if cust_id in customers:
        order_details = {
            "Order": input("Enter order details: "),
            "Quantity": int(input("Enter quantity: ")),
            "Unit Price": float(input("Enter unit price: "))
        }
        customers[cust_id]["Orders"].append(order_details)
        print(f'Order placed successfully for customer {cust_id}.')
    else:
        print(f'Customer ID {cust_id} not found.')
 
customers = {
    1: {"Name": "Jim", "Contact": "192-567-3567", "Orders": []},
    2: {"Name": "Bobby", "Contact": "192-233-9981", "Orders": []},
}
 
while True:
    user_input = input("""
    1. Add Customer
    2. Place Order
    3. Generate Customer Report
    4. Generate All Customer Reports
    5. Exit
    """)
 
    try:
        user_input = int(user_input)
 
        if 1 <= user_input <= 5:
            if user_input == 1:
                add_customer()
            elif user_input == 2:
                add_order()
            elif user_input == 3:
                report_single()
            elif user_input == 4:
                for cust_id, cust_info in customers.items():
                    print("\nCustomer ID:", cust_id)
                    for key, value in cust_info.items():
                        if key == "Orders":
                            print(f'{key}:')
                            for order in value:
                                print(f'  Order: {order["Order"]}, Quantity: {order["Quantity"]}, Unit Price: {order["Unit Price"]}')
                        else:
                            print(f'{key}: {value}')
            else:
                print("Thank you! Goodbye!")
                break  
        else:
            print("Invalid input. Please enter a number between 1 and 5.")
    except ValueError:
        print("Invalid input. Please enter a number.")