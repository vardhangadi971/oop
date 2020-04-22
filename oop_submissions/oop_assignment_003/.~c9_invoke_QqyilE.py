class Car:
	def __init__(self,max_speed,acceleration,tyre_friction,color="none"):
		self._color=color
		self._max_speed=max_speed
		if self._max_speed<0:
			raise ValueError("Invalid value for max_speed")
		
		self._acceleration=acceleration
		if self._acceleration<0:
			raise ValueError("Invalid value for acceleration")
		
		self._tyre_friction=tyre_friction
		if self._tyre_friction<0:
			raise ValueError("Invalid value for tyre_friction")
		
		
		self._current_speed=0
		self._is_engine_started=False
				
	def start_engine(self):
		self._is_engine_started=True
	def accelerate(self):
		if self._is_engine_started==True:
			if self._current_speed+self._acceleration<self._max_speed:
				self._current_speed+=self._acceleration
			else:
				self._current_speed=self._max_speed
		else:
			#self._is_engine_started=False
			print("Start the engine to accelerate")
	def apply_brakes(self):
		if self._current_speed>=self._tyre_friction:
				self._current_speed-=self._tyre_friction
		else:
			self._current_speed=0
			
	def sound_horn(self):
		if self._is_engine_started==True:
			 print('Beep Beep')
		else:
			print("Start the engine to sound_horn")
	def stop_engine(self):
		if self._is_engine_started:
			self._is_engine_started=False
	@property
	def color(self):
		return self._color
	@property
	def acceleration(self):
		return self._acceleration
	@property
	def tyre_friction(self):
		return self._tyre_friction
	@property
	def max_speed(self):
		return self._max_speed
	@property
	def current_speed(self):
		return self._current_speed
	@property
	def is_engine_started(self):
		return self._is_engine_started
	
class RaceCar(Car):
	def __init__(self,max_speed,acceleration,tyre_friction,color):
		super().__init__(max_speed,acceleration,tyre_friction,color)
		self._nitro=0
	def sound_horn(self):
		if self._is_engine_started==True:
			 print('Peep Peep\nBeep Beep')
		else:
			print("Start the engine to sound_horn")
	def apply(self):
		
	