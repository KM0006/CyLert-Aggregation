


def AssertParameterType(Parameter, ParameterName, ParemeterAllowedTypes):

	assert isinstance(Parameter, tuple(ParemeterAllowedTypes)), InvalidParameterTypeError(ParameterName, ParemeterAllowedTypes)


InvalidParameterTypeError = lambda ParameterName, ParemeterAllowedTypes \
	: (f"Parameter {ParameterName} allowed types are ") + (f"only {ParemeterAllowedTypes[0]}" if len(ParemeterAllowedTypes) == 1 else f"{ParemeterAllowedTypes}")