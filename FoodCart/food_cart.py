food_prices = {
    "Burger": 120,
    "Pizza": 250,
    "Pasta": 180,
    "Sandwich": 90,
    "French Fries": 100,
    "Ice Cream": 80,
    "Coffee": 70,
    "Tea": 40
}

items = []
total = 0

for key, value in food_prices.items():
    print(f"{key:<15}: ₹{value}")

print("----------------------------------------")

print(f"Your Cart\n\n")