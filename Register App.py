import sqlite3
import hashlib

sq = sqlite3.connect('register.db')
sql = sq.cursor()

sql.execute("""CREATE TABLE IF NOT EXISTS register (

    user_name VARCHAR(50) UNIQUE,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    email VARCHAR(50) UNIQUE,
    password_hash VARCHAR(64)

            )""")

while True:
    user_name1 = input('Enter your user name: ')
    user_name_exists = sql.execute("SELECT user_name FROM register WHERE user_name=?", (user_name1,)).fetchone()

    if len(user_name1) < 3 or len(user_name1) > 25:
        print("User name must be between 3 and 25 characters.")
        continue

    if user_name_exists:
        print("This user name already exists. Please use a different user name.")
        continue
    break

while True:
    first_name1 = input('Enter your first name: ')
    last_name1 = input('Enter your last name: ')

    if len(first_name1) < 3 or len(first_name1) > 25:
        print("First name must be between 3 and 25 characters.")
        continue

    if len(last_name1) < 3 or len(last_name1) > 25:
        print("Last name must be between 3 and 25 characters.")
        continue

    if first_name1 == last_name1:
        print("You cannot enter the same first name and last name. Please enter them again.")
        continue
    break

while True:
    email1 = input('Enter your email: ')
        
    email_exists = sql.execute("SELECT email FROM register WHERE email=?", (email1,)).fetchone()
    if email_exists:
        print("Email already exists. Please use a different email.")
        continue
    break

password_match = False
password1 = input('Create your password: ')
while not password_match:
    password2 = input('Enter your password again: ')
    if password1 == password2:
        if len(password1) < 8 or len(password1) > 15:
            print("Password must be between 8 and 15 characters.")
            continue
        password_match = True
    else:
        print("Passwords do not match. Please try again.")
    
password_hash = hashlib.sha256(password1.encode()).hexdigest()

try:
    sql.execute("INSERT INTO register (user_name, first_name, last_name, email, password_hash) VALUES (?, ?, ?, ?, ?)",
                (user_name1, first_name1, last_name1, email1, password_hash))
    sq.commit()
    print("Registration successful!")
except sqlite3.Error as e:
    print("An error occurred:", e)

sq.close()