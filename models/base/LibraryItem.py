from abc import ABC , abstractmethod

class LibraryItem(ABC):
  def __init__(self,item_id, title, author, available=True, borrowed_by=None ):
    self.item_id = item_id
    self.title = title
    self.author = author
    self._available = available # protected
    self._borrowed_by = borrowed_by # User who borrowed the item
  @abstractmethod
  def display_info(self):
    pass

  def check_availability(self):
      return self._available