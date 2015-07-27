class Person():
	def __init__(self,name = '',age = 0):
		self._name = name
		self._age = age 
	@property
	def age(self):
	    return self._age
	@age.setter
	def age(self, value):
	    if 0 < age <= 150:
	    	self._age = age
	def __str__(self):
		return "%s,%d" % (self._name,self._age)

p = Person('yhc',33)
print p

p.age = 55
print p.age

p.age = -4
print p.age


