
from abc import ABC, abstractmethod
from Utils.AssertionHandling import AssertParameterType

class IDataLoader(ABC):

	@abstractmethod
	def LoadData(this, DataFilePath : str):
		
		AssertParameterType(DataFilePath, "DataFilePath", [str])