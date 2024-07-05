
import Utils.OnCallLibs as Libs
from Utils.AssertionHandling import AssertParameterType

class PrimitiveClassifier():

	def __init__(this, InputDim : int, NeuronsLayersCount : list, OutputDim : int, ConnectedLayersCount : int):
		
		AssertParameterType(InputDim, "Input Dim", [int])

		AssertParameterType(OutputDim, "Output Dim", [int])

		AssertParameterType(ConnectedLayersCount, "Connected Layers Count", [int])

		ModelLayers = [Libs.KerasLib.layers.Dense(InputDim, activation="relu")]

		ModelLayers.extend([Libs.KerasLib.layers.Dense(Count, activation="relu") for Count in NeuronsLayersCount])

		ModelLayers.append(Libs.KerasLib.layers.Dense(OutputDim, activation="softmax"))

		this.Classifier = Libs.KerasLib.Sequential(ModelLayers)
