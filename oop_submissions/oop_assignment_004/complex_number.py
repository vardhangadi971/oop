import math
class ComplexNumber:
	def __init__(self,real_part=0,imaginary_part=0):
		if type(real_part)==str and type(imaginary_part)==str:
			raise ValueError("Invalid value for real and imaginary part")
		if type(real_part)==str:
			raise ValueError("Invalid value for real part")
		if type(imaginary_part)==str:
			raise ValueError("Invalid value for imaginary part")
		self.real_part=real_part
		self.imaginary_part=imaginary_part
	def __str__(self):
		return "{}{}{}i".format(self.real_part,"+" if self.imaginary_part>=0 else "-",abs(self.imaginary_part))
	def conjugate(self):
		return ComplexNumber(self.real_part,-self.imaginary_part)
	def __add__(self,other):
		return ComplexNumber(self.real_part+other.real_part,self.imaginary_part+other.imaginary_part)
	def __sub__(self,other):
		return ComplexNumber(self.real_part-other.real_part,self.imaginary_part-other.imaginary_part)
	def __mul__(self,other):
		return ComplexNumber((self.real_part*other.real_part-self.imaginary_part*other.imaginary_part),self.real_part*other.imaginary_part+(other.real_part*self.imaginary_part))
	def __truediv__(self,other):
		k=float(other.real_part**2+other.imaginary_part**2)
		sr=self.real_part
		oR=other.real_part
		si=self.imaginary_part
		oi=other.imaginary_part
		return ComplexNumber((sr*oR+si*oi)/k,(si*oR-sr*oi)/k)
	def __abs__(self):
		return round(math.sqrt(self.real_part**2+self.imaginary_part**2),3)
	def __eq__(self,other):
		return self.real_part==other.real_part and self.imaginary_part==other.imaginary_part
	
    	

      
		