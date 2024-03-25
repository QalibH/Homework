# Task 1:

# def calcuclate(lis):
#     slis = sum(lis)
#     plis = 1
#     for x in lis:
#         plis *= x

#     return slis, plis

# lis = [10, 29, 34, 47, 52]

# sresult, presult = calcuclate(lis)

# print(f"Sum of all list elements: {sresult}")
# print(f"Product of all elements of a list: {presult}")


# Task 2:

# lis = ['friend', 'dear', 'my', 'Hello']

# lis.reverse()

# print(lis)


# Task 3:

# lis1 = ['Hel', 'm', 'de', 'fri']

# lis2 = ['lo', 'y', 'ar', 'end']

# a = [ x + y  for x,y in zip(lis1, lis2) ] 

# print(a)


# Task 4:

# lis = [['Jacob', 'Alex', 'Lena'], ['Petr', 'Selena', 'Nona'], ['Sasha', 'Jax', 'Scadi']]

# lis[2][1] = 'Calliope'

# print(lis) 


# Task: 5

# lis = ['Azalaviacargo', 'Azal' ,'Silk Line', 'Improtex', 'Turan']

# index = lis.index('Silk Line')
# print("Value index Silk Line: ", index)

# lis[2] = 'Silk West'
# print(lis)


# Task 6:

# def Average(lst): 
# 	return sum(lst) / len(lst) 

# lis = [97, 52, 64] 
# average = Average(lis) 
 
# print("Average is =", round(average, 2)) 


# Task 7:

# start = int(input("Start: "))
# end = int(input("End: "))


# even_numbers = 0


# for number in range(start, end):
    
#     if number % 2 == 0:
#         even_numbers += 1
#         print(f"{number} - even")
#     else:
#         print(f"{number} - not even")


# print(f"Total even numbers: {even_numbers}")


# Task 8:

# lis = [23, 57, 64, 23, 58, 64, 98]

# lisw = list(set(lis))

# print (lisw)


# Task 9:

# lis = [77, 88, 99]

# com = []
# for i in range(len(lis)):
#     for j in range(len(lis)):
#         for k in range(len(lis)):
#             if i != j and j != k and i != k:
#                 com.append([lis[i], lis[j], lis[k]])

# print(com)


# Task 10:

# lis = {'Klara', 'Lena', 'Nona'}

# choice = int(input('(1) Add (2) Delete : '))

# if choice == 1:
#     new_name = input('Enter name to add: ')
#     if not new_name:
#         print('Error: You did not enter a name')
#     else:
#         lis.add(new_name)
#         print(lis)
# elif choice == 2:
#     old_name = input('Enter name to delete: ')
#     if not old_name:
#         print('Error: You did not enter a name')
#     elif old_name not in lis:
#         print('Error: This name is not in the database')
#     else:
#         lis.remove(old_name)
#         print(lis)
# else:
#     print('Invalid choice')


# Task 11:

# printer = input("Enter a word: ")
# for x in range(6):

#     print(printer)