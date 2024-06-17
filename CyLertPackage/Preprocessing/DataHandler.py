
import Utils.AssertionHandling

from IDataReader import IDataReader

class DataHandler:

	def __init__(this, DefaultDataReader : IDataReader = None ):
		
		if DefaultDataReader:
		
			Utils.AssertionHandling.AssertParameterType(DefaultDataReader, "DefaultDataReader", [IDataReader])
			
			this.DefaultDataReader = DefaultDataReader

	def LoadData(this, DataReader : IDataReader = None):

		if DataReader:

			Utils.AssertionHandling.AssertParameterType(DataReader, "DataReader", [IDataReader])

			return DataReader.LoadData()
		
		return this.DefaultDataReader.LoadData()

	

