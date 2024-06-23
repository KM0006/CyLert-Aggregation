
from Utils.AssertionHandling import AssertParameterType

from Preprocessing.DataLoaders.IDataLoader import IDataLoader
from Preprocessing.DataLoaders.CyLertDataLoaders import JsonDataLoader

from Preprocessing.DataFormatters.IDataFormatter import IDataFormatter
from Preprocessing.DataFormatters.CyLertDataFormatters import JsonToStringFormatter

from Preprocessing.DataEncoders.IDataEncoder import IDataEncoder
from Preprocessing.DataEncoders.CyLertDataEncoders import CySecBertEncoder

class DataHandler:

	def __init__(this, *, DefaultDataEncoder : IDataEncoder = None, DefaultDataLoader : IDataLoader = None, DefaultDataFormatter : IDataFormatter = None):
		
		if DefaultDataLoader:
		
			AssertParameterType(DefaultDataLoader, "Default Data Loader", [IDataLoader])
			
			this.DefaultDataLoader = DefaultDataLoader

		else:

			this.DefaultDataLoader = JsonDataLoader()

		if DefaultDataFormatter:
		
			AssertParameterType(DefaultDataFormatter, "Default Data Formatter", [IDataFormatter])
			
			this.DefaultDataFormatter = DefaultDataFormatter

		else:

			this.DefaultDataFormatter = JsonToStringFormatter()

		if DefaultDataEncoder:
		
			AssertParameterType(DefaultDataEncoder, "Default Data Encoder", [IDataEncoder])
			
			this.DefaultDataEncoder = DefaultDataEncoder

		else:

			this.DefaultDataEncoder = CySecBertEncoder()

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
	
	def EncodeData(this, StringRepresentation : str, DataEncoder : IDataEncoder = None):

		if DataEncoder:

			AssertParameterType(DataEncoder, "DataEncode", [IDataEncoder])

			return DataEncoder.EncodeData(StringRepresentation)
		
		return this.DefaultDataEncoder.EncodeData(StringRepresentation)
		