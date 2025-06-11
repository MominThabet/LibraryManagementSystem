from models.base import *

class DVD(LibraryItem , Reservable):
  def __init__(self, item_id , title, author ,duration ,available=True, borrowed_by=None ,reserved_by = None):  
    super().__init__(item_id ,title, author , available , borrowed_by)
    self.duration = duration
    self._reserved_by = reserved_by # protected
  
  def display_info(self):
    return (f"id {self.item_id}, DVD: {self.title} by {self.author}, Duration: {self.duration} minutes")

  def reserve(self, user):
    if self.check_availability():
      self._reserved_by = user
      self._available = False
      return True
      # print(f"Book '{self.title}' reserved by {user}")
    else:
      return False
      # print(f"Book '{self.title}' is not available")

  def to_dict(self):
    # Convert the DVD object to a dictionary for saving in json files
    return {
      "type": "DVD",
      "item_id": self.item_id,
      "title": self.title,
      "author": self.author,
      "duration": self.duration,
      "available": self._available,
      "borrowed_by": self._borrowed_by.user_id if self._borrowed_by else None,
      "reserved_by": self._reserved_by.user_id if self._reserved_by else None
    }
  
  def __str__(self):
    return f'DVD Id {self.item_id}, Title {self.title}, Author {self.author}, Duration {self.duration}, Available {self._available}'

  @classmethod
  def from_dict(cls,library, data):
    # Convert a dictionary to a DVD object
    if data.get('borrowed_by') is not None:
      borrowed_by = library.get_user(data.get('borrowed_by'))
    else:
      borrowed_by = None
    if data.get('reserved_by') is not None:
      reserved_by =  library.get_user(data.get('reserved_by'))
    else:
      reserved_by = None
    return cls(
      item_id=data['item_id'],
      title=data['title'],
      author=data['author'],
      duration=data.get('duration'),
      available=data.get('available', True),
      borrowed_by=borrowed_by,
      reserved_by=reserved_by
    )