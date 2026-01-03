
# Function to calculate the total prise of items in a shopping card

def shopping_cart(**products):
    total = 0
    print("Items purchased:")
    for item, price in products.items():
        print(f"{item}: Rs{price}")
        total +=price
    print("-------------")
    print(f"Total: Rs{total}")
shopping_cart(apple = 20, orange = 25, mango = 30, banana = 25)    