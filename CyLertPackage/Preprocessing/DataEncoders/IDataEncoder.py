
from abc import ABC, abstractmethod
from Utils.AssertionHandling import AssertParameterType

class IDataEncoder(ABC):

	@abstractmethod
	def EncodeData(this, StringRepresentation : str):
		
		AssertParameterType(StringRepresentation, "StringRepresentation", [str])