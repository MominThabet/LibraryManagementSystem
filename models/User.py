# Create a User class with attributes like user_id, name, borrowed_items.
class User:
	def __init__(self, user_id, name,email,borrowed_items_ids ):
		self.user_id = user_id
		self.name = name
		self.email = email
		self._borrowed_items = []   # Protected: only Library modifies this
		self._borrowed_items_ids = borrowed_items_ids
		
	def borrow_item(self, item):
		self._borrowed_items.append(item)

	def return_item(self, item):
		if item in self._borrowed_items:
			self._borrowed_items.remove(item)

	def __str__(self):
		return f"User ID: {self.user_id}, Name: {self.name}, Email: {self.email},	 Borrowed Items: {self._borrowed_items}"
	
	def to_dict(self):
		return {
			"user_id": self.user_id,
			"name": self.name,
			"email": self.email,
			"borrowed_items_ids": [item.item_id for item in self._borrowed_items],
		}
	
	@classmethod
	def from_dict(cls, data):
		return cls(data["user_id"], data["name"],data["email"], data["borrowed_items_ids"])