class Animals:
	food_value=0
	breath="breathe"
	sound="sound"
	def __init__(self,age_in_months,breed,required_food_in_kgs):
		if age_in_months!=1:
			raise ValueError("Invalid value for field age_in_months: {}".format(age_in_months))
		self._age_in_months=age_in_months
		self._breed=breed
		if required_food_in_kgs<=0:
			raise ValueError("Invalid value for field required_food_in_kgs: {}".format(required_food_in_kgs))
		self._required_food_in_kgs=required_food_in_kgs
	def grow(self):
		self._age_in_months+=1
		self._required_food_in_kgs+=self.food_value
	@property
	def age_in_months(self):
		return self._age_in_months
	@property
	def breed(self):
		return self._breed
	@property
	def required_food_in_kgs(self):
		return self._required_food_in_kgs
	@classmethod
	def breathe(cls):
		print(cls.breath)
	@classmethod
	def make_sound(cls):
		print(cls.sound)
def hunting(park,hunt_animal):
		c1=0
		c2=0
		for animal in park.animal_list:
			if animal.__class__==Deer:
				c1+=1
				park.animal_list.remove(animal)
			if animal.__class__==GoldFish:
				c2+=1
				park.animal_list.remove(animal)
		
		if c1==0 and hunt_animal=="deer":
			print("No deers to hunt")
		if c2==0 and hunt_animal=="goldfish":
			print("No GoldFish to hunt")
		
class LandAnimals(Animals):
	breath="Breathe in air"
class WaterAnimals(Animals):
	breath="Breathe oxygen from water"
class Deer(LandAnimals,Animals):
	sound="Buck Buck"
	food_value=2
class Lion(LandAnimals,Animals):
	sound="Roar Roar"
	food_value=4
	def hunt(self,hunt_1):
		hunt_animal="deer"
		hunting(hunt_1,hunt_animal)
class Shark(WaterAnimals,Animals):
	sound="Shark Sound"
	food_value=8
	def hunt(self,hunt_1):
		hunt_animal="goldfish"
		hunting(hunt_1,hunt_animal)
class GoldFish(WaterAnimals,Animals):
	sound="Hum Hum"
	food_value=0.2
class Snake(LandAnimals,Animals):
	sound="Hiss Hiss"
	food_value=0.5
	def hunt(self,hunt_1):
		hunt_animal="deer"
		hunting(hunt_1,hunt_animal)
class Zoo(Animals):
	animal_list_for_all_zoos=[]
	def __init__(self,reserved_food_in_kgs=0):
		self._reserved_food_in_kgs=reserved_food_in_kgs
		self.animal_list=[]
	def count_animals(self):
		return len(self.animal_list)
	def add_animal(self,animal):
		self.animal_list.append(animal)
		self.animal_list_for_all_zoos.append(animal)
	def add_food_to_reserve(self,food):
		self._reserved_food_in_kgs+=food
	def feed(self,hungry_animal):
		if self._reserved_food_in_kgs>0:
			self._reserved_food_in_kgs-=hungry_animal._required_food_in_kgs
			hungry_animal.grow()
	@property
	def reserved_food_in_kgs(self):
		return self._reserved_food_in_kgs
	@classmethod
	def count_animals_in_all_zoos(cls):
		return len(cls.animal_list_for_all_zoos)
	@staticmethod
	def count_animals_in_given_zoos(zoo_name):
		c=0
		for animal in zoo_name:
			c+=animal.count_animals()
		return c
		

	
	