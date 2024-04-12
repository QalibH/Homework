import sqlite3
import random

sq = sqlite3.connect('casino.db')
sql = sq.cursor()

print('Welcome to the casino!')

login = None  

while True:

    choice = input('Choice: (1) Register (2) Log in (3) Log out (4) Play (5) Remove user from database (6) Check balance (7) Exit: ')

    if choice == '1':
        login = input('Enter your login (only letters and numbers): ')
        password = input('Enter your password  (only letters and numbers): ')
        cash = int(input('Enter your initial cash amount: '))
        sql.execute('INSERT INTO casino (login, password, cash) VALUES (?, ?, ?)', (login, password, cash))
        sq.commit()
        print('Registration successful!')

    elif choice == '2':
        if login:
            print("You are already logged in.")
            continue
        login_attempt = input('Enter your login: ')
        password_attempt = input('Enter your password: ')
        sql.execute('SELECT * FROM casino WHERE login=? AND password=?', (login_attempt, password_attempt))
        result = sql.fetchone()
        if result:
            login = login_attempt
            print('Login successful!')
        else:
            print('Invalid login or password. Please try again.')

    elif choice == '3':
        if login:
            print("Logging out...")
            login = None
        else:
            print("You are not logged in.")

    elif choice == '4':
        if login is None:
            print("Please log in first.")
            continue
        balance = sql.execute('SELECT cash FROM casino WHERE login=?', (login,)).fetchone()[0]
        if balance < 5:
            print('Insufficient funds')
        else:
            result = random.choice(['win', 'lose'])
            if result == 'win':
                print('You have won 10 azn')
                balance += 10
            else:
                print('You lost 5 azn')
                balance -= 5
            sql.execute('UPDATE casino SET cash=? WHERE login=?', (balance, login))
            sq.commit()

    elif choice == '5':
        if login is None:
            print("Please log in first.")
            continue

        while True:
            check1 = input('Are you sure? y/n: ')
            if check1 == 'y':
                sql.execute('DELETE FROM casino WHERE login=?', (login,))
                sq.commit()
                print('User removed from database')
                login = None 
                break  
            elif check1 == 'n':
                print('Canceling actions. Return to selection menu')
                break 
            else:
                print('Invalid choice. Please enter y/n.')
                continue  

    elif choice == '6':
        if login is None:
            print("Please log in first.")
            continue
        balance = sql.execute('SELECT cash FROM casino WHERE login=?', (login,)).fetchone()
        if balance:
            print(f'Your current balance is {balance[0]} azn')
        else:
            print('User not found.')

    elif choice == '7':
        print('Exiting the game...')
        break
    
    else:
        print('Invalid choice. Try again.')