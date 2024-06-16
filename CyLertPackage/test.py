
from abc import ABC, abstractmethod

class testBaseClass(ABC):

	@abstractmethod
	def testmethod(self):

		pass


class testSubClass(testBaseClass):

	def testmethod(self):
		
		return ":"
	
test_Base_Class = testSubClass()

assert isinstance(test_Base_Class, testBaseClass), "Fuck you"


	
