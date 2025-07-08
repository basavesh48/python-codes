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
while True:
    fruit = input("\nEnter the name of the fruit (or type 'done' to finish): ").lower()

    if fruit == 'done':
        break
    elif fruit not in fruit_prices:
        print("Sorry, we don't have that fruit.")
        continue
try:
        quantity = float(input(f"Enter quantity of {fruit} in kg: "))
        cost = fruit_prices[fruit] * quantity
        total_bill += cost
        print(f"{quantity} kg of {fruit} costs ₹{cost}")
    except ValueError:
        print("Invalid quantity. Please enter a number.")
        print("\n-------------------------")
        print(f"Total Bill: ₹{total_bill:.2f}")
        print("Thank you for shopping with us!")
