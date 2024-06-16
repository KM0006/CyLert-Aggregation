
import IDataReader
import Utils.AssertionHandling


class DataHandler:

	def __init__(this, DataReader):
		
		Utils.AssertionHandling.AssertParameterType(DataReader, "DataReader", [IDataReader])