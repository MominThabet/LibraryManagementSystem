from models.base import LibraryItem

class Magazine(LibraryItem):
  def __init__(self, item_id,title, author ,issue_number ,available=True, borrowed_by=None):
    super().__init__(item_id, title, author , available , borrowed_by)
    self.issue_number = issue_number

  
  def display_info(self):
    return (f"Id {self.item_id}, Magazine: {self.title}, Issue #{self.issue_number} by {self.author}")

  def to_dict(self):
    # Convert the Magazine object to a dictionary for saving in json files
    return {
      "type": "Magazine",
      "item_id": self.item_id,
      "title": self.title,
      "author": self.author,
      "issue_number": self.issue_number,
      "available": self._available,
      "borrowed_by": self._borrowed_by.user_id if self._borrowed_by else None,
    }
  def __str__(self):
    return f'Magazine Id {self.item_id}, Title {self.title}, Author {self.author}, issue_number {self.issue_number}, Available {self._available}'
 

  @classmethod
  def from_dict(cls,library, data):
    # Convert a dictionary to a Magazine object
    if data.get('borrowed_by') is not None:
      borrowed_by = library.get_user(data.get('borrowed_by'))
    else:
      borrowed_by = None
    return cls(
      item_id=data['item_id'],
      title=data['title'],
      author=data['author'],
      issue_number=data.get('issue_number'),
      available=data.get('available', True),
      borrowed_by=borrowed_by,
    )