
from Utils.OnCallLibs import JsonLib 
from Preprocessing.IDataReader import IDataReader

class JsonDataReader(IDataReader):

	def __init__(this):

		pass

	def LoadData(this, DataFilePath : str):

		super().LoadData(DataFilePath)

		ReadFileToken = "r"

		Dataset = []

		with open(DataFilePath, ReadFileToken) as Data:

			while(True):

				Line = Data.readline()

				if not Line:

					break

				Dataset.append(JsonLib.loads(Line))

		return Dataset