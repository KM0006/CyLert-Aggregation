
from abc import ABC, abstractmethod
from Utils.AssertionHandling import AssertParameterType

class IDataReader(ABC):

	@abstractmethod
	def LoadData(this, DataFilePath : str):
		
		AssertParameterType(DataFilePath, "DataFilePath", [str])