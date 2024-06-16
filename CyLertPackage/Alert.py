
import Utils.AssertionHandling

class Alert:

	def __init__(this, AlertRepresentation : str | dict):

		Utils.AssertionHandling.AssertParameterType(AlertRepresentation, "AlertRepresentation", [str, dict])

		alertRepresentation = dict()

		if isinstance(AlertRepresentation, str):

			import importlib

			JsonLib = importlib.import_module("json")

			alertRepresentation = JsonLib.loads(AlertRepresentation)

		else:

			alertRepresentation = AlertRepresentation
		
		this.AlertContents = alertRepresentation