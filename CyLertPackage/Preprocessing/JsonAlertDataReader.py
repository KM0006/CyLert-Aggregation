
from Preprocessing.IDataReader import IDataReader

class JsonAlertDataReader(IDataReader):

	def __init__(this):

		pass

	def LoadData(this, DataFilePath : str):

		super().LoadData(DataFilePath)
		print(DataFilePath)

