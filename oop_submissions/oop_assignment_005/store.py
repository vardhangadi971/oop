class Item:
	def __init__(self,name,price,category):
		self.name=name
		if price==0:
			raise ValueError("Invalid value for price, got 0")
		if price<0:
			raise ValueError("Invalid value for price, got {}".format(price))
		self.price=price
		self.category=category
	def __str__(self):
		return "{}{}{}{}{}".format(self.name,"@",self.price,"-",self.category)
class Query:
	def __init__(self,field,operation,value):
		self.field=field
		o=["IN","GT","GTE","LT","LTE","EQ","STARTS_WITH","ENDS_WITH","CONTAINS"]
		if operation in o:
			self.operation=operation
		else:
			raise ValueError("Invalid value for operation, got {}".format(operation))
		self.value=value
	def __str__(self):
		return "{} {} {}".format(self.field,self.operation,self.value)
class Store:
	items_list=[]
	def __init__(self):
		self.items_list=[]
	def add_item(self,item):
		self.items_list.append(item)
	def __str__(self):
		if len(self.items_list)==0:
			return "No items"
		else:
			return "\n".join(map(str,self.items_list))
	def count(self):
		return len(self.items_list)
	def filter(self,query):
		filtered_list=Store()
		if query.operation=="EQ":
			for i in self.items_list:
				if query.field=="name" and query.value==i.name:
					filtered_list.add_item(i)
				if query.field=="price" and query.value==i.price:
					filtered_list.add_item(i)
				if query.field=="category" and query.value==i.category:
					filtered_list.add_item(i)
		elif query.operation=="GT":
			for i in self.items_list:
				if query.field=="price" and query.value<i.price:
					filtered_list.add_item(i)
		elif query.operation=="LT":
			for i in self.items_list:
				if query.field=="price" and query.value>i.price:
					filtered_list.add_item(i)
		elif query.operation=="GTE":
			for i in self.items_list:
				if query.field=="price" and query.value<=i.price:
					filtered_list.add_item(i)
		elif query.operation=="LTE":
			for i in self.items_list:
				if query.field=="price" and query.value>=i.price:
					filtered_list.add_item(i)
		elif query.operation=="IN":
			for i in self.items_list:
				if query.field=="name" and i.name in query.value:
					filtered_list.add_item(i)
				if query.field=="price" and i.price in query.value:
					filtered_list.add_item(i)
				if query.field=="category" and i.category in query.value:
					filtered_list.add_item(i)
		elif query.operation=="STARTS_WITH":
			for i in self.items_list:
				if query.field=="name" and i.name.startswith(query.value):
					filtered_list.add_item(i)
				if query.field=="category" and i.category.startswith(query.value):
					filtered_list.add_item(i)
		elif query.operation=="ENDS_WITH":
			for i in self.items_list:
				if query.field=="name" and i.name.endswith(query.value):
					filtered_list.add_item(i)
				if query.field=="category" and i.category.endswith(query.value):
					filtered_list.add_item(i)
		elif query.operation=="CONTAINS":
			for i in self.items_list:
				if query.field=="name" and query.value in i.name:
					filtered_list.add_item(i)
				if query.field=="category" and query.value in i.category:
					filtered_list.add_item(i)
		return filtered_list	
					
	def exclude(self,query):
		exclude_list=Store()
		include_list=self.filter(query)
		for i in self.items_list:
			if i not in include_list.items_list:
				exclude_list.add_item(i)
		return exclude_list
		
			
'''
store = Store()  
item = Item(name="Oreo Biscuits", price=30, category="Food")  
store.add_item(item)  
item = Item(name="Boost Biscuits", price=20, category="Food")  
store.add_item(item)  
item = Item(name="Butter", price=10, category="Grocery")  
store.add_item(item)  
query = Query(field="price", operation="LTE", value=20)  
#query = Query(field="name", operation="IN", value=["Oreo Biscuits", "Boost Biscuits" ])  
results = store.exclude(query)  
print(results)'''

		
		
		