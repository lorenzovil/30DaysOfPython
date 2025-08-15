import os
import json

products_file = "products.json"

# Load existing products if file exists
if os.path.exists(products_file):
    with open(products_file, "r") as f:
        product_data = json.load(f)
else:
    product_data = {}

while True:
    print("\nWelcome to Product Management System")
    print("1. Add Product")
    print("2. View Products")
    print("3. Delete Product")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        pname = input("Product Name: ")
        quantity = int(input("Product Quantity: "))
        price = int(input("Product Price: "))
        
        product_data[pname] = {"quantity": quantity, "price": price}
        
        with open(products_file, "w") as f:
            json.dump(product_data, f)
        print(f"✅ Product '{pname}' added successfully.")

    elif choice == "2":
        if not product_data:
            print("No products available.")
        else:
            print("\nYour Products:")
            for pname, details in product_data.items():
                print(f"Product: {pname} - Quantity: {details['quantity']} / Price: {details['price']}")

    elif choice == "3":
        pname = input("Enter the product name to delete: ")
        if pname in product_data:
            del product_data[pname]
            with open(products_file, "w") as f:
                json.dump(product_data, f)
            print(f"🗑️ Product '{pname}' deleted successfully.")
        else:
            print(f"❌ Product '{pname}' not found.")

    elif choice == "4":
        confirm = input("Are you sure you want to exit? (yes/no): ")
        if confirm.lower() == "yes":
            print("Goodbye!")
            break
    else:
        print("❌ Invalid input. Please try again (1-4).")
