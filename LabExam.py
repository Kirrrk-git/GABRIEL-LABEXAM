class Inventory():

  def __init__(self):

    self.itemName = []

    self.quantity = []

    self.price = []

    self.totalItemValue = []



  def add_item(self):

    itemName = input("Input Item Name: ")

    quantity = int(input("Input Item Quantity: "))

    price = float(input("Input Item Price: "))

    totalItemValue = quantity * price



    self.itemName.append(itemName)

    self.quantity.append(quantity)

    self.price.append(price)

    self.totalItemValue.append(totalItemValue)



    print("\n" + "-"*30)

    print("Item Added Successfully: \n" + "Item Name: " + itemName + "\nQuantity: " + str(quantity) + "\nPrice: PHP " + str(price))

    print("Total Value: PHP " + str(totalItemValue))



  def update_quantity(self):

    if len(self.itemName) == 0:

      print("No Items In Inventory.")

      return

    

    print("\nItems in Inventory:")

    for i in range(len(self.itemName)):

      print(f"{i + 1}. {self.itemName[i]}")

    

    index = int(input("Enter item number to update: ")) - 1

    if 0 <= index < len(self.itemName):

      new_quantity = int(input("Enter new quantity: "))

      self.quantity[index] = new_quantity

      self.totalItemValue[index] = new_quantity * self.price[index]

      print("Quantity updated successfully!")

    else:

      print("Invalid item number.")



  def display_items(self):

    if len(self.itemName) == 0:

      print("No Items In Inventory.")

    else:

      print("\n" + "-"*30)

      print("Inventory Items:")

      for i in range(len(self.itemName)):

        print(f"\nItem {i + 1}:")

        print("Item Name: " + self.itemName[i])

        print("Quantity: " + str(self.quantity[i]))

        print("Price: PHP " + str(self.price[i]))

        print("Total Value: PHP " + str(self.totalItemValue[i]))



  def calculate_total_inventory_value(self):

    if len(self.itemName) == 0:

      print("No Items In Inventory.")

    else:

      total = sum(self.totalItemValue)

      print("\n" + "-"*30)

      print("Total Inventory Value: PHP " + str(total))

  

  def menu(self):

    while True:

      print("\n" + "-"*30)

      print("Inventory Management System")

      print("1. Add New Item In Inventory"

         "\n2. Update Item In Inventory"

         "\n3. View Item In Inventory"

         "\n4. Total Inventory Value"

         "\n" + "-"*30)

      

      print("What Do You Want To Do?")

      choose = int(input("Input Number: "))



      if choose == 1:

        self.add_item()

      elif choose == 2:

        self.update_quantity()

      elif choose == 3:

        self.display_items()

      elif choose == 4:

        self.calculate_total_inventory_value()

      else:

        print("Invalid Option. Please Try Again.")



if __name__ == "__main__":

  inventory = Inventory()

  inventory.menu()
