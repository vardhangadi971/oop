class Deer:
	def __init__(self,age_in_months,breed,required_food_in_kgs):
		if age_in_months>1:
			raise ValueError("Invalid value for field age_in_months: {}".format(age_in_months))
		else:
			self._age_in_months=age_in_months
		self._breed=breed
		if required_food_in_kgs==0:
			raise ValueError("Invalid value for field required_food_in_kgs: 0")
		elif required_food_in_kgs<0:
			raise ValueError("Invalid value for field required_food_in_kgs: {}".format(required_food_in_kgs))
		else:
			self._required_food_in_kgs=required_food_in_kgs
	@classmethod
	def make_sound(cls):
		print("Buck Buck")
	def grow(self):
		self._required_food_in_kgs+=2
		self._age_in_months+=1
	@classmethod
	def breathe(cls):
		print("Breathe in air")
	@property
	def age_in_months(self):
		return self._age_in_months
	@property
	def breed(self):
		return self._breed
	@property
	def required_food_in_kgs(self):
		return self._required_food_in_kgs
	
class Lion(Deer):
	def __init__(self,age_in_months,breed,required_food_in_kgs):
		super().__init__(age_in_months,breed,required_food_in_kgs)
	@classmethod
	def make_sound(cls):
		print("Roar Roar")
	def grow(self):
		self._required_food_in_kgs+=4
		self._age_in_months+=1
	@classmethod
	def breathe(cls):
		print("Breathe in air")
	def hunt(self,park):
		c1=0
		for animal in park.li:
			if animal.__class__==Deer:
				c1+=1
				park.li.remove(animal)
		if c1==0:
			print("No deers to hunt")
			
class Shark(Deer):
	def __init__(self,age_in_months,breed,required_food_in_kgs):
		super().__init__(age_in_months,breed,required_food_in_kgs)
	@classmethod
	def make_sound(cls):
		print("Shark Sound")
	def grow(self):
		self._required_food_in_kgs+=8
		self._age_in_months+=1
	@classmethod
	def breathe(cls):
		print("Breathe oxygen from water")
	def hunt(self,park):
		c2=0
		for animal in park.li:
			if animal.__class__==GoldFish:
				c2+=1
				park.li.remove(animal)
		if c2==0:
			print("No GoldFish to hunt")
	
class GoldFish(Deer):
	def __init__(self,age_in_months,breed,required_food_in_kgs):
		super().__init__(age_in_months,breed,required_food_in_kgs)
	@classmethod
	def make_sound(cls):
		print("Hum Hum")
	def grow(self):
		self._required_food_in_kgs+=0.2
		self._age_in_months+=1
	@classmethod
	def breathe(cls):
		print("Breathe oxygen from water")
class Snake(Deer):
	def __init__(self,age_in_months,breed,required_food_in_kgs):
		super().__init__(age_in_months,breed,required_food_in_kgs)
	@classmethod
	def make_sound(cls):
		print("Hiss Hiss")
	def grow(self):
		self._required_food_in_kgs+=0.5
		self._age_in_months+=1
	@classmethod
	def breathe(cls):
		print("Breathe in air")
	def hunt(self,park):
		c3=0
		for animal in park.li:
			if animal.__class__==Deer:
				c3+=1
				park.li.remove(animal)
		if c3==0:
			print("No deers to hunt")
			
class Zoo:
	li_g=[]
	def __init__(self,reserved_food_in_kgs=0):
		if reserved_food_in_kgs<0:
			raise ValueError("Invalid value for field required_food_in_kgs: {}".format(reserved_food_in_kgs))
		else:
			self._reserved_food_in_kgs=reserved_food_in_kgs
		self.li=[]
	def add_animal(self,animal):
		self.li.append(animal)
		self.li_g.append(animal)
	def add_food_to_reserve(self,food):
		self._reserved_food_in_kgs+=food
	def feed(self,anim):
		if self._reserved_food_in_kgs!=0 and self._reserved_food_in_kgs>=anim.required_food_in_kgs:
			self._reserved_food_in_kgs-=anim.required_food_in_kgs
			anim.grow()
	def count_animals(self):
		return len(self.li)
	@property
	def reserved_food_in_kgs(self):
		return self._reserved_food_in_kgs
	@classmethod
	def count_animals_in_all_zoos(cls):
		return len(cls.li_g)
	@staticmethod
	def count_animals_in_given_zoos(zoo):
		c=0
		for animal in zoo:
			c+=animal.count_animals()
		return c
		
'''			
zoo=Zoo()
gold_fish = GoldFish(age_in_months=1, breed="Nemo", required_food_in_kgs=0.5)
zoo.add_animal(gold_fish)
nehru_zoological_park = Zoo()
lion = Lion(age_in_months=1, breed="African Lion", required_food_in_kgs=15)
nehru_zoological_park.add_animal(lion)
lion = Lion(age_in_months=1, breed="African Lion", required_food_in_kgs=15)
nehru_zoological_park.add_animal(lion)
print(Zoo.count_animals_in_all_zoos())
print(Zoo.count_animals_in_given_zoos([nehru_zoological_park]))
'''
		
		
'''		
zoo = Zoo()
#zoo.reserved_food_in_kgs
zoo.add_food_to_reserve(10000000)
#print(zoo.reserved_food_in_kgs)
gold_fish = GoldFish(age_in_months=1, breed="Nemo", required_food_in_kgs=0.5)
zoo.add_animal(gold_fish)
zoo.feed(gold_fish)
#print(zoo.reserved_food_in_kgs)
#print(gold_fish.age_in_months)
shark = Shark(age_in_months=1, breed="Hunter Shark", required_food_in_kgs=10)
zoo.add_animal(shark)
zoo.feed(shark)
#print(zoo.reserved_food_in_kgs)
#print(shark.age_in_months)
print(zoo.count_animals())'''




