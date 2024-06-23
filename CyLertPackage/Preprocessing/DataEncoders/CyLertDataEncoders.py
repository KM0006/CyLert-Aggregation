
from Utils.OnCallLibs import TorchLib
from Utils.PackageConfiguration import CySecBertModel, CySecBertTokenizer
from Preprocessing.DataEncoders.IDataEncoder import IDataEncoder

class CySecBertEncoder(IDataEncoder):

	def EncodeData(this, StringRepresentation : str):

		super().EncodeData(StringRepresentation)

		Tokens = CySecBertTokenizer(StringRepresentation, add_special_tokens = True, return_tensors = 'pt', padding = True, truncation = True)

		ModelOutputs = CySecBertModel(**Tokens)

		Embedding = ModelOutputs.last_hidden_state.mean(dim = 1)

		return Embedding