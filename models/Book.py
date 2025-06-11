from models.base import *
from models.User import User
class Book(LibraryItem , Reservable):
  def __init__(self,item_id, title, author ,pages,available=True, borrowed_by=None ,reserved_by = None):
    super().__init__(item_id,title, author,available , borrowed_by)
    self.pages = pages
    self._reserved_by = reserved_by  # protected
  
  def display_info(self):
    return (f"Id {self.item_id}, Book: {self.title} by {self.author}, {self.pages} pages")

  def reserve(self, user):
    if self.check_availability():
      self._reserved_by = user
      self._available = False
      print(f"Book '{self.title}' reserved by {user.name}")
    else:
      print(f"Book '{self.title}' is not available")

  def to_dict(self):
    # Convert the Book object to a dictionary for saving in json files
    return {
      "type": "Book",
      "item_id": self.item_id,
      "title": self.title,
      "author": self.author,
      "pages": self.pages,
      "available": self._available,
      "borrowed_by": self._borrowed_by.user_id if self._borrowed_by else None,
      "reserved_by": self._reserved_by.user_id if self._reserved_by else None
    }
  
 

  @classmethod
  def from_dict(cls,library , data):
    # Convert a dictionary to a Book object
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
      pages=data.get('pages'),
      available=data.get('available', True),
      borrowed_by=borrowed_by,
      reserved_by=reserved_by
    )
  def __str__(self):
    return f'Book id {self.item_id}, Title {self.title}, Author {self.author}, Pages {self.pages}, Available {self._available}'
 
