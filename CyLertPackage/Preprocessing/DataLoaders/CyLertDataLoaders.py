
from Utils.OnCallLibs import JsonLib
from Preprocessing.DataLoaders.IDataLoader import IDataLoader

class JsonDataLoader(IDataLoader):

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

class TimeLabeledDataLoader(IDataLoader):

	def LoadData(this, DataFilePath : str):

		super().LoadData(DataFilePath)

		ReadFileToken = "r"

		Dataset = []

		with open(DataFilePath, ReadFileToken) as Data:

			while(True):

				Line = Data.readline()

				if not Line:

					break

				Dataset.append(Line.split(",")[0])

		return Dataset