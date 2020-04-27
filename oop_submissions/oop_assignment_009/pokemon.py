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
		self._master=None
	def __str__(self):
		return "{} - Level {}".format(self.name,self.level)
	
	@property
	def master(self):
		if self._master==None:
			print("No Master")
		else:
		 return self._master
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

#Island#
class Island:
	li_g=[]
	
	def __init__(self,name,max_no_of_pokemon,total_food_available_in_kgs,pokemon_left_to_catch=0):
		self._name=name
		self._max_no_of_pokemon=max_no_of_pokemon
		self._total_food_available_in_kgs=total_food_available_in_kgs
		self._pokemon_left_to_catch=pokemon_left_to_catch
		self.li=[]
		self.li_g.append(self)
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
		else:
			print("Island at its max pokemon capacity")
			
	@classmethod
	def get_all_islands(cls):
		return cls.li_g
		
#Trainer#	
class Trainer:
	
	def __init__(self,name="none"):
		self._name=name
		self._food_in_bag=0
		self._experience=100
		self._max_food_in_bag=10*self._experience
		self._current_island=None
		self.pokemons_list=[]
		
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
	
	@property
	def current_island(self):
		if self._current_island==None:
			print("You are not on any island")
		else:
			return self._current_island
	
	def move_to_island(self,island):
			self._current_island=island
	
	def get_my_pokemon(self):
		return self.pokemons_list
	
			
	def collect_food(self):
		if self._current_island==None:
			print("Move to an island to collect food")
		elif self._current_island._total_food_available_in_kgs<self._max_food_in_bag:
			self._food_in_bag=self._current_island._total_food_available_in_kgs
			self._current_island._total_food_available_in_kgs=0
		elif self._food_in_bag!=self._max_food_in_bag:
			self._current_island._total_food_available_in_kgs-=self._max_food_in_bag
			self._food_in_bag=self._max_food_in_bag
			
	def catch(self,poke):
		if self._experience>=100*poke.level:
			self.pokemons_list.append(poke)
			print("You caught {}".format(poke.name))
			self._experience+=poke.level*20
			poke._master=self
		else:
			print("You need more experience to catch {}".format(poke.name))

		