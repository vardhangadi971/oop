from car import Car
class Truck(Car):
		sound='Honk Honk'
		def __init__(self,max_speed,acceleration,tyre_friction,color,max_cargo_weight):
			super().__init__(max_speed,acceleration,tyre_friction,color)
			self._max_cargo_weight=max_cargo_weight
			self._cargo=0
			
		def load(self,cargo_weight):
			if cargo_weight<0:
				 raise ValueError("Invalid value for cargo_weight")
			else:
				if self.current_speed>0:
					print("Cannot load cargo during motion")
				else:
					if self._cargo+cargo_weight<=self._max_cargo_weight:
						self._cargo+=cargo_weight
					else:
						print("Cannot load cargo more than max limit: {}".format(self._max_cargo_weight))
		def unload(self,cargo_weight):
			if cargo_weight<0:
				 raise ValueError("Invalid value for cargo_weight")
			else:
				if self.current_speed>0:
					print("Cannot unload cargo during motion")
				else:
					self._cargo-=cargo_weight
		@property
		def cargo(self):
			return self._cargo
		@property
		def max_cargo_weight(self):
			return self._max_cargo_weight

