# 1 - Retail:

retail = []

for instance in range(0, 6):
     product = input('Product name: ')
     price = input('Price: ')
     play = {
          'Product': product,
          'Price': price,
     }

     retail.append(play)


print('Products: ', retail)



# 2 - Finance:

total_value = 0

for i in range(3):
    num_shares = input("Enter number of shares: ")
    price_per_share = int(input("Enter share price: "))
    
    total_value += price_per_share

print("Total value of stock portfolio:", total_value)



# 3 - Healtcare:

healtcare = []

for instance in range(0, 5):
     patient = input('Patient name: ')
     age = input('Age: ')
     play = {
          'Patient': patient,
          'Age': age,
     }

     healtcare.append(play)


print('Patients: ', healtcare)



# 4 - Education :

education = []

for instance in range(0, 8):
     student = input('Student name: ')
     age = input('Age: ')
     play = {
          'Student': student,
          'Age': age,
     }

     education.append(play)


print('Students: ', education)



# 5 - Restaurant:

restaurant = []

for instance in range(0, 4):
     food_product = input('Food product: ')
     price = input('price: ')
     play = {
          'Food product': food_product,
          'price': price,
     }

     restaurant.append(play)


print('All in: ', restaurant)



# 6 - Tecnology:

tecnology = []

for instance in range(0, 4):
     developer = input('Developer name: ')
     age = input('Age: ')
     program = input('Program language: ')
     play = {
          'Student': developer,
          'Age': age,
          'Program language': program,
     }

     tecnology.append(play)


print('Developers: ', tecnology)


# 7 - Transport:

num1 = float(input("Enter distance: "))
num2 = float(input("Enter time: "))


avg = (num1/ num2) 


print("Average speed = %.1f" %avg)



# 8 - Entertainment:

entertainment = []

for instance in range(0, 4):
     film = input('Film name: ')
     year = input('year: ')
     play = {
          'Film name': film,
          'year': year,
     }

     entertainment.append(play)

print('Films: ', entertainment)



# 9 - Real Estate:

real_estate = []

for instance in range(0, 4):
     kv2 = input('The square footage of the house: ')
     price = input('Price: ')
     play = {
          'The square footage of the house': kv2,
          'price': price,
     }

     real_estate.append(play)

print('Houses: ', real_estate)



# 10 - E-commerce:

e_commerce = []

for instance in range(0, 7):
     product = input('Product name: ')
     price = input('Price: ')
     play = {
          'Product': product,
          'Price': price,
     }

     e_commerce.append(play)


print('Products: ', e_commerce)



# 11 - Agriculture:

agriculture = []

for instance in range(0, 2):
     vegetable = input('Vegetable name: ')
     price = input('Price: ')
     play = {
          'Vegetable': vegetable,
          'Price': price,
     }

     agriculture.append(play)


print('Vegetables: ', agriculture)



# 12 - Telecommunication

telecommunication = []

for instance in range(0, 6):
     telephone = input('Telephone name: ')
     price = input('Price: ')
     play = {
          'Telephone': telephone,
          'Price': price,
     }

     telecommunication.append(play)


print('Telephones: ', telecommunication)



# 13 - Travel Industry:

def trip_cost():
    flight_cost = int(input("Enter the cost of air tickets: "))
    hotel_cost = int(input("Enter the hotel price: "))
    car_rental_cost = int(input("Enter car rental price: "))

    total_cost = flight_cost + hotel_cost + car_rental_cost

    print("Total cost of the trip: ", total_cost)

trip_cost()



# 14 - Construction Industry:

wood = int(input("Enter the amount of wood: "))
wood_cost = int(input("Enter the cost of wood per unit: "))

cement = int(input("Enter the amount of cement: "))
cement_cost = int(input("Enter the cost of cement per unit: "))

sand = int(input("Enter the amount of sand: "))
sand_cost = int(input("Enter the cost of sand per unit: "))

iron = int(input("Enter the amount of iron: "))
iron_cost = int(input("Enter the cost of iron per unit: "))


total_cost = wood * wood_cost + cement * cement_cost + sand * sand_cost + iron * iron_cost


print(f"Total cost of materials for the construction project: {total_cost}")