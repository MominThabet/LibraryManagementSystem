import os
import json
from models import *
from models.base import Reservable
from exceptions import *

class LibraryController:
  def __init__(self,items_path="data/items.json",users_path="data/users.json"):
    self._items_path = items_path
    self._users_path = users_path
    
    self.library = Library()
    self.load_data()
  
  def load_data(self):
    if os.path.exists(self._users_path) and os.path.getsize(self._users_path) > 0: 
      try:
        with open(self._users_path , 'r') as f:
          users_data = json.load(f)
          for user_dict in users_data:
            user = User.from_dict(user_dict)
            self.library.add_user(user)
          
      except FileNotFoundError:
        print("Warning: Data files not found. Starting fresh.")

    if os.path.exists(self._items_path) and os.path.getsize(self._items_path) > 0:
      try:
        with open(self._items_path, 'r') as f:
          items_data = json.load(f)
          #convert the dicts to objects
          for item_dict in items_data:
            item_type = item_dict.get("type")
            if item_type == "Book":
              item = Book.from_dict(self.library, item_dict)
            elif item_type == "DVD":
              item = DVD.from_dict(self.library,item_dict)
            elif item_type == "Magazine":
              item = Magazine.from_dict(self.library,item_dict)
            else:
              continue
            self.library.add_item(item)
      except json.JSONDecodeError:
        print(f"Warning: {self._items_path} contains invalid JSON. Skipping item loading.")
    for user in self.library.get_all_users(): 
        resolved_items = []
        for item_id in user._borrowed_items_ids:
          item = self.library.find_item_by_id(item_id)
          if item:
            resolved_items.append(item)
        user._borrowed_items = resolved_items
  def save_date(self):
    print('saving Data before exiting ')
    try:
      with open(self._items_path,'w') as f:
        json.dump([item.to_dict() for item in self.library.get_all_items()], f, indent=2)
      with open(self._users_path,'w') as f:
        json.dump([user.to_dict() for user in self.library.get_all_users()], f, indent=2)

    except IOError as e:
      print("Error saving data:",e)

  @classmethod
  def output(cls ,items):
    out = [f"{i}. {str(item)}\n" for i, item in enumerate(items,1) if item.check_availability()]
    return "".join(out)
  def list_available_items(self):
    return LibraryController.output(self.library.get_all_available_items()) 
  def search_items(self, query):
    print(f"Searching for '{query}'")
    results = self.library.find_item_by_title_or_type(query)
    
    if len(results) == 0:
      return "Item not found. \n"
    return LibraryController.output(results)
  
  def register_user(self ,name , email):
    user_id = len(self.library._users)
    user = User(user_id,name ,email ,[])
    self.library.add_user(user)
    return f'User {name} with ID {user.user_id} registered successfully.'

  def borrow_item(self, user_id, item_id):
    
    item = self.library.find_item_by_id(item_id)
    user = self.library.get_user(user_id)
    # check if item is available and is it reserved ot not 
    if not item.check_availability():
      raise ItemNotAvailableError(item_id) # raise an error if the item is not available and return the item
    # first check if the item is a reservable item
    # check if it is reserved only the user that reserve it can borrow it
  
    if isinstance(item, Reservable) and item._reserved_by and item._reserved_by != user:
      return f"{item.title} is reserved by {item._reserved_by.name}"
    
    if item._reserved_by == user:
      self.library.borrow_item(user,item)
      item._reserved_by = None
      return f"{item.title} borrowed by {user.name}"


    self.library.borrow_item(user, item)
    return f"{item.title} borrowed by {user.name}"  
  def reserve_item(self, user_id, item_id):
    item = self.library.find_item_by_id(item_id)
    user = self.library.get_user(user_id)

    if not user:
      raise UserNotFoundError(user_id)

    if not item.check_availability():
      raise ItemNotAvailableError(item_id)
    
    if not isinstance(item, Reservable):
      raise ItemNotReservableError(item_id)
    
    if item._reserved_by:
      return f"{item.title} is already reserved by {item._reserved_by.name}"
    
    self.library.reserve_item(user, item)
    return f"{item.title} reserved by {self.library.get_user(user_id).name}"
  
  def return_item(self, user_id, item_id):
    item = self.library.find_item_by_id(item_id)
    user = self.library.get_user(user_id)
    if not user:
      raise UserNotFoundError(user_id)

    if item.check_availability():
      return f"{item.title} is already available. \n"

    self.library.return_item(user, item)
    return f"{item.title} returned by {self.library.get_user(user_id).name}"
  
  def exit(self):
    self.save_date()
    return ("Data Had been Saved , Goodbye!")

  def get_All_Users(self):
    users = self.library.get_all_users()
    output = [f"{i}. {str(user)}\n" for i, user in enumerate(users,0)]
    return ''.join(output)
  def main_menu(self):
    return """Welcome to the Library System
1. View all available items
2. Search item by title or type
3. Register as a new user
4. Borrow an item
5. Reserve an item
6. Return an item
7. Exit and Save"""