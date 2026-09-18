inventory = 0
failed_attempts= 0
deliveries_processed = 0

def get_valid_input():

    while True:
        new_stock = input("How many stocks to add, or type 'quit' to leave: ")

        if new_stock.lower() == "quit":
            return "quit"

        if not new_stock.isdigit():
            print("type a positive integer.")
            failed_attempts +=1
            continue

        return int(new_stock)

def process_delivery(current_total,new_value):
    new_total = current_total +new_value    
    return new_total

def calculate_tax(amount):
    tax = amount * 0.15
    return tax

def generate_report(total_units, failed_attempts):
    print('Total inventory:', total_units)
    print('Failed entries:', failed_attempts)