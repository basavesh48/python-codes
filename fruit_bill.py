fruit_prices = {
    'apple': 100,
    'banana': 40,
    'mango': 80,
    'orange': 60,
    'grapes': 120
}
print("Welcome to the Fruit Shop!")
print("Available fruits and prices (per kg):")
for fruit, price in fruit_prices.items():
    print(f"{fruit.title()}: ₹{price}/kg")

total_bill = 0
