class ShoppingList:
	def __init__(self):
		self.list = []
		self.items = []

	def addList(self):
		user_list = input("Enter a store name to create a list for that store:\n> ")
		self.list.append(user_list)
		print(f"You can now enter items for your {user_list} list.")

	def addItem(self):
		new_items = input("> ")
		self.items.append(new_items)
		print(f"Your {self.list} now contains {self.items}.")

customer_list = ShoppingList()
customer_list.addList()
customer_list.addItem()
