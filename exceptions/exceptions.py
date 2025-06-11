# Custom exception for when an item is not available for borrowing or reservation
class ItemNotAvailableError(Exception):
  def __init__(self, item_title):
    super().__init__(f"Item '{item_title}' is not available.")

# Custom exception for when a user ID is not found in the system
class UserNotFoundError(Exception):
  def __init__(self, user_id):
      super().__init__(f"User with ID '{user_id}' not found.")

# Custom exception for when an item is not found in the library's collection
class ItemNotFoundError(Exception):
  def __init__(self, item_title):
      super().__init__(f"Item '{item_title}' not found in the library.")

class ItemNotReservableError(Exception):
  def __init__(self, item_title):
      super().__init__(f"Item '{item_title}' is not reservable.")

class UserAlreadyExistsError(Exception):
  def __init__(self, user_id):
      super().__init__( f"User with ID '{user_id}' already exists.")