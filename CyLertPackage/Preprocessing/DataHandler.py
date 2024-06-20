
from Utils.AssertionHandling import AssertParameterType
from Preprocessing.DataLoaders.IDataLoader import IDataLoader
from Preprocessing.DataFormatters.IDataFormatter import IDataFormatter

class DataHandler:

	def __init__(this, DefaultDataLoader : IDataLoader = None, DefaultDataFormatter : IDataFormatter = None):
		
		if DefaultDataLoader:
		
			AssertParameterType(DefaultDataLoader, "Default Data Loader", [IDataLoader])
			
			this.DefaultDataLoader = DefaultDataLoader

		if DefaultDataFormatter:
		
			AssertParameterType(DefaultDataFormatter, "Default Data Formatter", [IDataFormatter])
			
			this.DefaultDataFormatter = DefaultDataFormatter

	def LoadData(this, DataFilePath : str, DataLoader : IDataLoader = None):

		if DataLoader:

			AssertParameterType(DataLoader, "DataLoader", [IDataLoader])

			return DataLoader.LoadData(DataFilePath)
		
		return this.DefaultDataLoader.LoadData(DataFilePath)
	
	def FormatData(this, Record : dict, DataFormatter : IDataFormatter = None):

		if DataFormatter:

			AssertParameterType(DataFormatter, "DataFormatter", [IDataFormatter])

			return DataFormatter.FormatData(Record)
		
		return this.DefaultDataFormatter.FormatData(Record)
		