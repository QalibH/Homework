# Task 1:

lis = [71, 'sentinel', 44, 'jambo', 93, 'Kampfer']

# Method 1:

i = 1
while i < len(lis):
    print(lis)
    break

# Method 2:

index = 0

while index<len(lis):
    print(lis[index])
    index += 1


# Task 2:

lis = ['a', 'b', 'c', 'd', 'e', 'f']

i = 0
while i < len(lis):
    if lis[i] in ['c', 'e']:
        i += 1
        continue
    print(lis[i])
    i += 1


# Task 3:

p = int(input('Enter the number: '))

c = 0

while c <= p:
    print(c)
    c += 1

 
# Task 4:
    
password = 'lepik45'

attempts = 3

for x in range(attempts):
    password_attempt = input("Enter the password: ")
    if password_attempt != password:
        attempts -= 1
        print(f"Incorrect password. You have {attempts} attempts left.")
    else:
        print("Login successful!")
        break
else:
    print("You have been blocked.")


# Task 5:

questions = ["What is the capital of Germany? (a) Berlin (b) Rome (c) Paris",
             "What year did World War I end? (a) 1945 (b) 1918 (c) 1939",
             "Who wrote 'To Kill a Mockingbird'? (a) Harper Lee (b) J.K. Rowling (c) Stephen King",
             "What is the largest planet in our solar system? (a) Jupiter (b) Saturn (c) Earth",
             "What is the chemical symbol for silver? (a) Ag (b) Au (c) Hg",
             "What is the capital of Australia? (a) Sydney (b) Melbourne (c) Canberra",
             "Who is the current President of the United States? (a) Joe Biden (b) Donald Trump (c) Barack Obama",
             "What language is spoken in Azerbaijan? (a) Spanish (b) Azerbaijani (c) Russian",
             "What is the tallest mountain in the world? (a) Mount Everest (b) K2 (c) Kilimanjaro",
             "Who is the author of the 'Harry Potter' series? (a) J.R.R. Tolkien (b) J.K. Rowling (c) Stephenie Meyer"]

answers = ["a", "b", "a", "a", "a", "c", "a", "b", "a", "b"]

correct_count = 0
incorrect_count = 0

for i in range(10):
    print(questions[i])
    user_answer = input("Enter your answer (a, b, or c): ")
    if user_answer == answers[i]:
        correct_count += 1
    else:
        incorrect_count += 1

correct_count = correct_count - incorrect_count//4


print("Number of correct answers:", correct_count)
print("Number of incorrect answers:", incorrect_count)
