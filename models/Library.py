from models.base import Reservable
from models.User import User
from exceptions import (UserNotFoundError ,ItemNotFoundError , ItemNotAvailableError , ItemNotReservableError)
class Library:
  def __init__(self):
    self._items = []  # List of LibraryItem objects
    self._users = []  # List of USers

  def add_item(self, item):
    self._items.append(item)

  def remove_item(self, item):
    if item in self._items:
      self._items.remove(item)

  def add_user(self,user):
    self._users.append(user)
    return user


  def borrow_item(self, user, item):

    item._available = False
    item._borrowed_by = user
    user.borrow_item(item)
    print(f"{user.name} borrowed '{item.title}'")
    
  def reserve_item(self, user, item):
    item.reserve(user)
  
  def return_item(self, user, item):
   
    item._available = True
    item._borrowed_by = None
    item._reserved_by = None
    user.return_item(item)

  
  def find_item_by_title_or_type(self, query):
    return [item for item in self._items if ((query.lower() in item.title.lower()) or (query.lower() == item.__class__.__name__.lower()))]

  def find_item_by_id(self, item_id):
    item = self._items[item_id-1]
    if not item:
      raise ItemNotFoundError(item_id)
    return item
  def get_all_available_items(self):
    return [item for item in self._items if item.check_availability()]

  def get_all_items(self):
    # print('items are: ',self._items)
    return self._items

  def get_user(self, user_id):
    for user in self._users:
        if user.user_id == user_id:
            return user
    raise UserNotFoundError(user_id)
  def get_all_users(self):
    return self._users