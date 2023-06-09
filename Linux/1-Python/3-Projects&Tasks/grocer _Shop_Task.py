grocery_items = (
    ("apple", 10.0),
    ("banana", 5.0),
    ("orange", 4.5),
)

def display_items():
    print("Available items in the grocery shop:")
    for item in grocery_items:
        print(f"{item[0]} - ${item[1]}")

def calculate_total(items):
    total_cost = 0
    for item in items:
        for grocery_item in grocery_items:
            if grocery_item[0] == item:
                total_cost += grocery_item[1]
    return total_cost

display_items()
user_input = input("Enter the items you want to purchase (separated by commas): ")
items_purchased = [item.strip() for item in user_input.split(",")]

total_cost = calculate_total(items_purchased)
print(f"Total cost of items purchased: ${total_cost}")
