

from Preprocessing.DataFormatters.IDataFormatter import IDataFormatter

class JsonToStringFormatter(IDataFormatter):

	def FormatData(this, Record : dict):

		RecordAsStringRepresentation = ""

		for (Key, Value) in Record.items():

			RecordAsStringRepresentation += f"The {str(Key)} "
			
			if (type(Value) == dict):

				RecordAsStringRepresentation += "Consists of : \n"
				RecordAsStringRepresentation += "(\n"
				RecordAsStringRepresentation += f"{this.FormatData(Value)}"
				RecordAsStringRepresentation += ")"

			elif (type(Value) == list):

				RecordAsStringRepresentation += f"are : {str(Value)}, "
				
			else:
				
				RecordAsStringRepresentation += f"is : {str(Value)}, "

			RecordAsStringRepresentation += "\n"

		return RecordAsStringRepresentation
		