print("welcome to calculator")
while True:
    num1= float(input("Enter First Number: "))
    num2= float(input("Enter Second Number: "))

    print("Operation , + , - , * , ** , /  ")
    operation = input("Enter your operation: ")

    if operation == "+" :
     result = num1 + num2 
    elif operation == "-" : 
        result = num1 - num2
    elif operation == "*" :
        result = num1 * num2
    elif operation == "**" :
        result = num1 ** num2
    elif operation == "/" :
        if num2!=0:
            result = num1 / num2     
        else : 
            result = "ERROR"
    else :
        result = "ERROR"

    print("result" , result )

    print("do you want to keep using calculator? yes/No ")
    again = input ("yes or no?" )
    if again != "yes" :
        print("GOODBYE")
        break
   






