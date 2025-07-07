#simple_list_mngr.py

"""
This is a shopping list app that lets you add, 
remove, view, or edit stuff on your list. 
You just pick an option from the menu, and it 
handles the rest!
"""

EMPTY_LIST = "Sorry, your list is currently empty."
list = []

while True:
  print("Shopping List Manager")
  print("1. Add item")
  print("2. Remove item")
  print("3. View list")
  print("4. Edit item")
  print("5. Exit list")

  option = input("Enter an option (1-5): ")

  if option == "1":
    item = input("Enter an item to add to your shopping list: ").lower()
    list.append(item)
    print(f"{item} added to list.")

  elif option == "2":
    if not list:
      print(EMPTY_LIST)
    else:
      item = input("Which item would you like to remove? ").lower()
      if item not in list:
        print(f"{item} is not in your list.")
      else: 
        list.remove(item)
        print(f"{item} removed from list.")

  elif option == "3":
    if not list:
      print(EMPTY_LIST) 
    else: 
      print("Here is your current Shopping List: ")
      for index, item in enumerate(list, start=1):
        print(f"{index}: {item}")
      print("-" * 10)
  
  elif option == "4":
      if not list:
        print(EMPTY_LIST)
      else:
        print("Current list: ")
        for index, item in enumerate(list, start=1):
          print(f"{index}: {item}")
        try:
          item_index = int(input("Enter number of item you wish to edit: ")) - 1
          if 0 <= item_index < len(list):
            new_item = input("Enter the replacement item: ").lower()
            print(f"{list[item_index]} has been updated to {new_item}")
            list[item_index] = new_item
          else:
            print("Invalid item number, try again.")
        except ValueError:
          print("Invalid input please enter a number.")

  elif option == "5":
    print("Exitting Shopping List Manager. Thank you!")
    break
  
  else:
    ("Invalid choice. Try again or 5 to exit.")
