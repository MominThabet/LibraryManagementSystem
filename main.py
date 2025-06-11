from controllers import LibraryController
from exceptions import *
import sys
def choices_map (LC ,choice):

  if choice == "1":
    return LC.list_available_items()
  
  elif choice == "2":
    search_query = input("Enter search query: ")
    return LC.search_items(search_query)
  
  elif choice == "3":
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    return LC.register_user(name,email)
  
  elif choice == "4":
    user_id = int(input("Enter user_Id: "))
    item_id = int(input("Enter item id: "))
    return LC.borrow_item(user_id, item_id)
  
  elif choice == "5":
    user_id = int(input("Enter user_Id: "))
    item_id = int(input("Enter item_id: "))
    return LC.reserve_item(user_id, item_id)
  
  elif choice == "6":
    user_id = int(input("Enter user_Id: "))
    item_id = int(input("Enter item_Id: "))
    return LC.return_item(user_id, item_id)

  elif choice == "7":
    LC.exit()
    sys.exit()

  else:
    return "Invalid choice. Please try again. \n"
def main ():
  LC = LibraryController()  
  try :
    while True:
      print(LC.main_menu())
      choice = input("Enter your choice: ")
      try :
        print(choices_map(LC ,choice))
      except Exception as e:
        print(f"Unexpected error: {e}")
  except KeyboardInterrupt :
    LC.exit()

if __name__ == "__main__":
  main()