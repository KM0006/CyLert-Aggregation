
from abc import ABC, abstractmethod

class IDataReader(ABC):

	@abstractmethod
	def LoadData() : pass