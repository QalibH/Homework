# Task 1:

height = float(input("Enter your height: "))

ideal_weight_min = 18.5 * (height ** 2)
ideal_weight_max = 25 * (height ** 2)

print(f"Your recommended weight range is {round(ideal_weight_min, 2)} kg to {round(ideal_weight_max, 2)} kg")


# Task 2:

products = {
    "shirt": 35.9,
    "shoes": 27.9,
    "tie": 9.9,
    "trousers": 49.9,
    "T-shirt": 19.9,
    "jacket": 59.9,
    "hat": 15.9,
    "shorts": 25.9,
    "socks": 5.9,
    "coat": 99.9
}

total_cost = 0
item_count = 0

for i in range(5):
    item = input("Enter product name: ")
    if item in products:
        total_cost += products[item]
        item_count += 1
    else:
        print("Product is out of stock, please select another product.")
    if item_count == 5:
        break

total_cost_with_tax = total_cost * 1.18

print(f"Total cost with taxes (azn): {total_cost_with_tax:.2f}")

if total_cost_with_tax >= 50 and total_cost_with_tax < 100:
    print("You won a 10 azn coupon!")
elif total_cost_with_tax >= 100:
    print("You won a 15 azn coupon!")
else:
    print('Thank you for your purchase! Come again.')


# Task 3:

distance = float(input("Enter travel distance (km): "))
vehicle_type = input("Enter vehicle type (car, truck, bus): ")

if vehicle_type == "car":
    cost = distance * 0.50
elif vehicle_type == "truck":
    cost = distance * 1.00
elif vehicle_type == "bus":
    cost = distance * 2.00
else:
    print("Invalid vehicle type")

print(f"The total cost of the trip is {cost} dollars.")