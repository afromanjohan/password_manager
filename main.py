# -*- coding: utf-8 -*-

#Imports
import sys
import psycopg2
import pyperclip
from password_generator import PasswordGenerator


while True:
    pw = input("Input password to access database (5 to quit application) ")
    if pw == "5":
        sys.exit()
    try:
        conn = psycopg2.connect(
        host="localhost",
        database="password_manager",
        user="postgres",
        password=pw)
        print("Correct password... Accessing database...")
        break
    except:
        print("...Incorrect password input...")
        
pwgen = PasswordGenerator()
pwgen.minlen = 32
pwgen.maxlen = 32
pwgen.minuchars = 3
pwgen.minlchars = 3
pwgen.minschars = 3
#pwgen.excludeschars = "!$%^" # (if certain characters are typically not accepted)
cur = conn.cursor()

while True:
    print("")
    print("1: Generate and add password to password bank")
    print("2: Access passwords")
    print("3: See all registered applications")
    print("4: See all registered data")
    print("5: Quit application")
    
    selected_option = input()
    print("")
    
    if selected_option == "1":
        appname = input("Input name of application: ")
        username = input("Input username: ")
        email = input("Input email: ")
        generated_password = pwgen.generate()
        print(f"Randomly generated password: {generated_password}")
        print("Password automatically saved to clipboard")
        pyperclip.copy(generated_password)
        print("")
        should_save = input("Press 1 to save entry into database ")
        if should_save == 1:
            
            cur.execute("INSERT INTO data(application_name, username, affiliated_email, pw) VALUES(%s, %s, %s, %s)",
                    (appname, username, email, generated_password))
            conn.commit()
        
    elif selected_option == "2":
        desired_application = input("Input application: ")
        print("Registered users for desired application: ")
        cur.execute('SELECT * FROM data WHERE application_name = %s;', (desired_application,))
        rows = cur.fetchall()
        for r in rows:
            print(f'Username: {r[1]}   Password: {r[2]}')
        
    elif selected_option == "3":
        cur.execute("SELECT application_name FROM data")
        rows = cur.fetchall()
        for r in rows:
            print(f'Application: {r[0]}')
    elif selected_option == "4":
        cur.execute("SELECT * FROM data")
        rows = cur.fetchall()
        for r in rows:
            print(f'Application: {r[0]} Username: {r[1]} Affiliated email: {r[3]} Password: {r[2]}')
        
    elif selected_option == "5":
        break
    else:
        continue


cur.close()
conn.close()