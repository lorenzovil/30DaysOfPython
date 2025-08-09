ITEM = []

while True:
    print ("WELCOME TO ADD Product")
    print ("1. ADD Product ")
    print ("2 View All Product")
    print ("3 Remove Product")
    print ("4  EXIT ")

    choice = input("choose ( 1 - 4 )")

    if choice == "1" :
        product = input("ENTER Your Product : ")
        ITEM.append(product)
        print("Product Added Successfully ")

    elif choice == "2" :
        if not ITEM : 
            print ("The Product Is Emty")
        else :
            print ("here is your Product")
            for i , product in enumerate(ITEM, 1):
                print(f"{i}. {product}")

    elif choice == "3" :
        if not ITEM :
            print ("The Product Is Emty")
        else :
            print ("Here Is Your Product")
            for i , product in enumerate(ITEM , 1) :
                print (f"{i} . {product}")
            remove = int(input("enter a number To Remove  : "))
            if 1 <= remove <= len(ITEM):
                removed = ITEM.pop(remove -1)
                print (f"removed : {removed}")
            else : 
                print ("invalid Number")

    elif choice == "4":
        print ("Goodbye")
        break
    
    else :
        print ("invalid input only Choose between 1-2")
       


            
