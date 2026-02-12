class Item:

    def __init__(self):
        self.items = []

    def menu(self):
        while True:
            print("\n=========================")
            print("Inventory Management System")
            print("1. Add New Item")
            print("2. Update Item Quantity")
            print("3. Display All Items")
            print("4. Total Inventory Value")
            print("5. Exit")

            try:
                choice = int(input("Choose an option: "))
            except ValueError:
                print("Invalid input. Please enter a number from 1 to 5.")
                continue

            if choice == 1:
                self.add_item()
            elif choice == 2:
                self.update_quantity()
            elif choice == 3:
                self.display_items()
            elif choice == 4:
                self.calculate_total_inventory_value()
            elif choice == 5:
                print("Hays Sawakas, Bye!")
                break
            else:
                print("Invalid Option. Try again.")

    def add_item(self):
        name = input("Input Item Name: ")

        try:
            quantity = int(input("Input Item Quantity: "))
            price = float(input("Input Item Price: "))
        except ValueError:
            print("Invalid input. Quantity and price must be a number.")
            return

        if quantity < 0 or price < 0:
            print("Quantity and price cant be negative.")
            return

        total = quantity * price

        item = {
            "name": name,
            "quantity": quantity,
            "price": price,
            "total": total
        }

        self.items.append(item)

        print("\n=========================")
        print("Item Added Successfully!")
        print("Item Name:", name)
        print("Quantity:", quantity)
        print("Price: PHP", price)

    def update_quantity(self):
        if len(self.items) == 0:
            print("No Items In Inventory.")
            return

        print("\nItems in Inventory:")
        for i in range(len(self.items)):
            print(i + 1, ".", self.items[i]["name"])

        try:
            choice = int(input("Enter item number to update: ")) - 1
        except ValueError:
            print("Invalid input. Please enter a number.")
            return

        if 0 <= choice < len(self.items):
            try:
                new_quantity = int(input("Enter new quantity: "))
            except ValueError:
                print("Invalid input. Quantity must be a whole number.")
                return

            if new_quantity < 0:
                print("Quantity cannot be negative.")
                return

            self.items[choice]["quantity"] = new_quantity
            self.items[choice]["total"] = new_quantity * self.items[choice]["price"]
            print("Quantity updated successfully!")
        else:
            print("Invalid item number.")

    def display_items(self):
        if len(self.items) == 0:
            print("No Items In Inventory.")
            return

        print("\n=========================")
        print("Inventory Items:")

        for i in range(len(self.items)):
            item = self.items[i]
            print("\nItem", i + 1)
            print("Item Name:", item["name"])
            print("Quantity:", item["quantity"])
            print("Price: PHP", item["price"])
            print("Total Value: PHP", item["total"])

    def calculate_total_inventory_value(self):
        if len(self.items) == 0:
            print("No Items In Inventory.")
            return

        total_inventory = 0
        for item in self.items:
            total_inventory += item["total"]

        print("\n=========================")
        print("Total Inventory Value: PHP", total_inventory)

item = Item()
item.menu()
