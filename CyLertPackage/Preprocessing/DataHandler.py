
from ..Utils.AssertionHandling import AssertParameterType
from ..Preprocessing.DataLoaders.IDataLoader import IDataLoader
from ..Preprocessing.DataFormatters.IDataFormatter import IDataFormatter

class DataHandler:

	def __init__(this, DefaultDataLoader : IDataLoader = None, DefaultDataFormatter : IDataFormatter = None):
		
		if DefaultDataLoader:
		
			AssertParameterType(DefaultDataLoader, "DefaultDataLoader", [IDataLoader])
			
			this.DefaultDataLoader = DefaultDataLoader

	def LoadData(this, DataLoader : IDataLoader = None):

		if DataLoader:

			AssertParameterType(DataLoader, "DataLoader", [IDataLoader])

			return DataLoader.LoadData()
		
		return this.DefaultDataLoader.LoadData()
	
	def PreapareData(this, DataLoader : IDataLoader = None):

		if DataLoader:

			AssertParameterType(DataLoader, "DataLoader", [IDataLoader])

			return DataLoader.LoadData()
		
		return this.DefaultDataLoader.LoadData()

	

