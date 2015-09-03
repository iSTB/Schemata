__author__ = "Jack McKay Fletcher"
__copyright__ = "Copyright 2015, Plymouth University "
__credits__ = ["Thomas Wenneker"]
__license__ = "GPL"
__version__ = "0.0.1"
__maintainer__ = "Jack McKay Fletcher"
__email__ = "jack.mckayfletcher@plymouth.ac.uk"
__status__ = "Production"
import itertools

class schema(object):
	"""
	The schema class
	"""
	def __init__(self, string = ''):
		self.string = string
		self.alphabet = []

	def __str__(self):
		return self.string

	def __repr__(self):
		return self.string


	def __ge__(self,other):

		if type(other) != type(self):
			raise TypeError("Cannot call >= on type " + type(self) +" and " + type(other))
		
		return join(self,other) == self


	def __eq__(self,other):
		return self.string == other.string 


	
	def get_length(self):
		return len(self.string)	


	def get_anti_order(self):
		return self.string.count('*')

	def get_def_length(self):
		#TODO write this.
		return -1			

	def get_order(self):
		return self.get_length() - self.get_anti_order()

	def set_string(self,string):

		if type(x) != str:
			raise ValueError("set_string() must take a str as input")

		self.string = string 

	def set_alphabet(self,alpha):
		if type(alpha) != list:
			raise ValueError("set_alphabet only can take be a list of chars or strings as inputs" ) 

		for char in alpha:
			if type(char) != str:		
				raise ValueError("set_alphabet only can take be a list of chars or strings as inputs" ) 


		self.alphabet = alpha


	def expansion(self):
		""" 
		Expands the schema.
		Note: The alphabet of the schema needs to be set first, use set_alphabet().

		Example:
		>>>s = schemata.schema('1*0')
		>>>s.set_alphabet(['1','0'])
		>>>s.expansion()
		>>>['110','101']
		"""
		
		if self.alphabet == []:
			raise ValueError('exansion() cannot be called when the alphabet not set, use set_alphabet()')
			return None

		expanded_set = []
			

def __all_eq_lens(xs):
	"""
	Checks if all items in a list are of the same length.

	Keyword arguments:

	xs -- a list whose elements are of the same type and have the method len()	
	"""

	if len(xs) == 0:
		raise ValueError("__all_eq_lens() cannot be called on the empty list")

	list_type = type(xs[0])
	same_type = True

	for x in xs:
		if type(x) != list_type:
			same_type = False
			break 

	if same_type == False:
		raise ValueError("__all_eq_lens() can only be called on a list whose elements are of the same type")

	try:
		len(xs[0])
	except Exception:
		raise ValueError("__all_eq_lens() can only be called on a list whose elements have len()")


	if len(xs) == 1:
		return True
	
	lens = map(len,xs)
	first = lens[0]

	all_eq = True

	for l in lens:
		if l != first:
			all_eq = False
			break
	return all_eq


def __check_type(x):
	"""
	Checks if a variable x is of type schema or string.
	"""

	s = schema()

	if type(x) == type(s) or type(x) == str:
		return True

	return False


def join(s1,s2):	
	if __check_type(s1) != True:
		raise ValueError(str(s1) + " not of type string or schema")
	
	if __check_type(s2) != True:
		raise ValueError(str(s2) + " not of type string or schema")

	if type(s1) == str:
		s1 = schema(s1)

	if type(s2) == str:
		s2 = schema(s2)

	if s1.get_length() != s2.get_length():
		if s1.string != '' and s2.string != '': 
			raise ValueError("join can only be performed on schema or strings of the same length")

	new = ''

	if s1.string == '':
		return s2
	if s2.string == '':
		return s1
	
	for i in xrange(len(s1.string)):
		if s1.string[i] == s2.string[i]:
			new +=s1.string[i] 
		else:
			new+='*'
	return schema(new)	



def complete(base):
	new = []
	for pair in itertools.product(base, repeat=2):
		if pair[0] != pair[1]:
			j = join(pair[0],pair[1])
			if j not in base+new:
				new.append(j)
	if new == []:
		return base + ['']

	else: return base+findschema1(new)


	

		


 
