class Pokemon:
	sound="sound"
	running="run"
	swimming="swim"
	flying="fly"
	def __init__(self,name,level=1):
		if len(str(name))==0:
			raise ValueError("name cannot be empty")
		else:
			self._name=name
		if level<=0:
			raise ValueError("level should be > 0")
		else:
			self._level=level
	def __str__(self):
		return "{} - Level {}".format(self.name,self.level)
	
	@property
	def name(self):
		return self._name
	@property
	def level(self):
		return self._level
	@classmethod
	def make_sound(cls):
		print(cls.sound)
	@classmethod
	def run(cls):
		print(cls.running)
	@classmethod
	def swim(cls):
		print(cls.swimming)
	@classmethod
	def fly(cls):
		print(cls.flying)

	
class Pikachu(Pokemon):
	sound="Pika Pika"
	running="Pikachu running..."
	def attack(self):
		print("Electric attack with {} damage".format(self._level*10))
		
class Squirtle(Pokemon):
	sound="Squirtle...Squirtle"
	running="Squirtle running..."
	swimming="Squirtle swimming..."
	def attack(self):
		print("Water attack with {} damage".format(self._level*9))
		
class Pidgey(Pokemon):
	sound="Pidgey...Pidgey"
	flying="Pidgey flying..."
	def attack(self):
		print("Air attack with {} damage".format(self._level*5))
		
class Swanna(Pokemon):
	sound="Swanna...Swanna"
	flying="Swanna flying..."
	swimming="Swanna swimming..."
	def attack(self):
		print("Water attack with {} damage".format(self._level*9))
		print("Air attack with {} damage".format(self._level*5))
		
class Zapdos(Pokemon):
	sound="Zap...Zap"
	flying="Zapdos flying..."
	def attack(self):
		print("Electric attack with {} damage".format(self._level*10))
		print("Air attack with {} damage".format(self._level*5))







class Island(Pokemon):
	li_g=[]
	
	def __init__(self,name,max_no_of_pokemon,total_food_available_in_kgs,pokemon_left_to_catch=0):
		self._name=name
		self._max_no_of_pokemon=max_no_of_pokemon
		self._total_food_available_in_kgs=total_food_available_in_kgs
		self._pokemon_left_to_catch=pokemon_left_to_catch
		self.li=[]
		self.li_g.append("{} - {} pokemon - {} food".format(self._name,self._pokemon_left_to_catch,self._total_food_available_in_kgs))
	
	def __str__(self):
		return "{} - {} pokemon - {} food".format(self._name,self._pokemon_left_to_catch,self._total_food_available_in_kgs)
	
	@property
	def name(self):
		return self._name
	@property
	def max_no_of_pokemon(self):
		return self._max_no_of_pokemon
	@property
	def total_food_available_in_kgs(self):
		return self._total_food_available_in_kgs
	@property
	def pokemon_left_to_catch(self):
		return self._pokemon_left_to_catch
		
	def add_pokemon(self,objpokemon):
		if self._pokemon_left_to_catch<self._max_no_of_pokemon:
			self._pokemon_left_to_catch+=1
			self.li.append(objpokemon)
		else:
			print("Island at its max pokemon capacity")
			
	@classmethod
	def get_all_islands(cls):
		return 
	
	

class Trainer(Island):
	def __init__(self,name="none"):
		self._name=name
		self._food_in_bag=0
		self._experience=100
		self._max_food_in_bag=10*self._experience
		self._current_island="none"
		self.move=0
		
	def __str__(self):
		return "{}".format(self._name)
		
	@property
	def name(self):
		return self._name
	@property
	def food_in_bag(self):
		return self._food_in_bag
	@property
	def experience(self):
		return self._experience
	@property
	def max_food_in_bag(self):
		return self._max_food_in_bag
	
	def move_to_island(self,island_name):
			self._current_island=island_name
			self.move+=1
	@property
	def current_island(self):
		if self.move!=0:
			print(self._current_island)
		else:
			print("You are not on any island")
	
	def collect_food(self):
		if self.move==0:
			print("Move to an island to collect food")
		elif self._total_food_available_in_kgs<self.max_food_in_bag:
			self._food_in_bag=self._total_food_available_in_kgs
			self._total_food_available_in_kgs=0
		elif self._food_in_bag!=self._max_food_in_bag:
			self._total_food_available_in_kgs-=self._max_food_in_bag
			self._food_in_bag=self._max_food_in_bag
		else:
			pass
	def catch(self,poke):
		if self._experience>=100*poke.level:
			self._experience+=poke.level*20
			print("you caught {}".format(poke.name))
		
			
			
		
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
		
		
		
	






















trainer=Trainer(name="bot")		
island = Island(name="Island1", max_no_of_pokemon=5, total_food_available_in_kgs=10000)
#island = Island(name="Island2", max_no_of_pokemon=5, total_food_available_in_kgs=10000)
#island = Island(name="Island3", max_no_of_pokemon=5, total_food_available_in_kgs=10000)
#island = Island(name="Island4", max_no_of_pokemon=5, total_food_available_in_kgs=10000)
#print(Island.get_all_islands())
trainer.move_to_island(island)
print(trainer.current_island==island)
print(trainer.current_island)

