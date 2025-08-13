import os
import json

PASSWORD_FILE = "password.json"

if os.path.exists(PASSWORD_FILE):
    with open(PASSWORD_FILE, "r")as f:
        password = json.load(f)

else:
   passwords = {}


while True:
    print("Welcome to password Managaer")
    print("1. Add New Login")
    print("2. view all Logins")
    print("3. delete Login")
    print("4. Exit")

    choice = input("eneter Your Choice (1-4) :")

    if choice == "1":
        site = input("Website name : ")
        username = input("Username: ")
        password = input ("Password: ")
        passwords[site] = {"username": username, "passsword": password}
        with open (PASSWORD_FILE, "w") as f:
            json.dump(passwords, f)
        print("Login Added Successfully")
    
    elif choice == "2":
        if not passwords:
            print("No Logins Aavailable")
        else:
            print("Your Logins:")
            for site, creds in passwords.items():
                print(f"website: {site} - {creds['username']} / {creds['password']}")

    elif choice == "3":
        site = input("Enter the website name to delete: ")
        if site in passwords:
            del passwords[site]
            with open(PASSWORD_FILE, "w")as f:
                json.dump(passwords, f)

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("invalid choice, please try again.")

    