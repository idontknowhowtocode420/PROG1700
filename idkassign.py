
def report_single():
        cust_id = int(input("Customer ID to find customer info: "))

        if cust_id in customers:
            print(f'\nCustomer ID: {cust_id}')
            for key, value in customers[cust_id].items():
                        print(f'{key}: {value}')
                        return




    










customers = {
    1: {"Name": "Jim", "Contact": "192-567-3567", "Orders": []},
    2: {"Name": "Bobby", "Contact": "192-233-9981", "Orders": []},
}



while True:
    user_input = input("""1. Add Customer

2. Place Order

3. Generate Customer Report

4. Generate All Customer Reports

5. Exit """)
 
    try:
        user_input = int(user_input)
        if 1 <= user_input <= 5:
            break
        
        else:
            print("Invalid input. Please enter a number between 1 and 5.")
    except ValueError:
        print("Invalid input. Please enter")
        


if user_input == 5:
    print("Thank you! Goodbye!")
    
if user_input == 4:
    for cust_id, cust_info in customers.items():
        print("\nCustomer ID:", cust_id)
        
        for key in cust_info:
            print(key + ':', cust_info[key])
      
    
if user_input == 3:
    report_single()

    
if user_input == 2:
    print("I am 2")
    

if user_input == 1:
    print("I am 1")
    


