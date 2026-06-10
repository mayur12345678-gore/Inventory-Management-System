import csv
import os

FILE_NAME = "products.csv"

def add_product():
    pid = input("Enter Product ID: ")
    name = input("Enter Product Name: ")
    qty = input("Enter Quantity: ")
    price = input("Enter Price: ")

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([pid, name, qty, price])

    print("Product Added Successfully!")

def view_products():
    if not os.path.exists(FILE_NAME):
        print("No Products Found!")
        return

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

def search_product():
    pid = input("Enter Product ID: ")

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == pid:
                print("Found:", row)
                return

    print("Product Not Found!")

while True:
    print("\n1. Add Product")
    print("2. View Products")
    print("3. Search Product")
    print("4. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_product()
    elif choice == "2":
        view_products()
    elif choice == "3":
        search_product()
    elif choice == "4":
        break
    else:
        print("Invalid Choice")
