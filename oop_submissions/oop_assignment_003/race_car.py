import math
from car import Car
class RaceCar(Car):
	sound='Peep Peep\nBeep Beep'
	def __init__(self,max_speed,acceleration,tyre_friction,color):
		super().__init__(max_speed,acceleration,tyre_friction,color)
		self._nitro=0
	def apply_brakes(self):
		if self._current_speed>self._max_speed//2:
			self._nitro+=10
		super().apply_brakes()
	def accelerate(self):
		if self._nitro!=0:
			self._current_speed+=math.ceil(0.3*self._acceleration)
			self._nitro-=10
		super().accelerate()
	@property
	def nitro(self):
		return self._nitro
		
