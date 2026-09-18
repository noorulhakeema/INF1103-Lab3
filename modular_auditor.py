inventory = 0

get_valid_input = input("How many stocks to add, or type 'quit' to leave: ")
def process_delivery(current_total,new_value):
    current_total += new_value
    return current_total

def calculate_tax(amount):
    tax = amount * 0.15
    return tax

def generate_report(total_units, failed_attempts):
    print('Total inventory:', total_units)
    print('Failed entries:', failed_attempts)