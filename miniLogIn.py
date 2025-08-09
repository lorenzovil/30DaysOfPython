users = {}

while True :
    print ("Welcome")
    print ("1. Login")
    print ("2 Register")
    print ("3 exit")

    num = input("ENTER your number 1-3 : ")

    if num == "1" :
        username = input("Username : ")
        if username in users:
            print("This Username Already Registerd")
        else:
             password=input("Password : ")
             users[username]= password
             print ("Registration successfull")

    elif num == "2" :
        username = input("Enter Your Username : ")
        password = input("Enter Your Password : ")

        if username in users and users[username] == password :
            print("WELCOME")
        else : 
            print("invalid input try again ")

    elif num == "3" :
        print("GOODBYE")
        break 

    else :
        print("invalid number please Try Again ")

        
        
        
        