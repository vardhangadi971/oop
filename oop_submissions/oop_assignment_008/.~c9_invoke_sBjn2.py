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
class LandAnimals(Animals):
	breath="Breathe in air"
class WaterAnimals(Animals):
	breath="Breathe oxygen from water"
class Deer(LandAnimals):
	def __init__(self,age_in_months,breed,required_food_in_kgs)
		super().__init__(age_in_months,breed,required_food_in_kgs)
		
	
	
	
	
	
	
	
	
	
	
	
	