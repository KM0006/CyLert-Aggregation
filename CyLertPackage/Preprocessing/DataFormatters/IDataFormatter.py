
from abc import ABC, abstractmethod
from Utils.AssertionHandling import AssertParameterType

class IDataFormatter(ABC):

	@abstractmethod
	def FormatData(this, Record : dict):
		
		AssertParameterType(Record, "Record", [dict])
	