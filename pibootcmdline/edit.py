from pibootcmdline.load import parse_parameter


def add_parameters(cmdline, parameters_to_add):
    """
    Parameters
    ----------
    cmdline: collections.OrderedDict
        parsed command line to which to add parameters.

    parameters_to_add: list[str]
        list of string parameters.

    Returns
    -------
    collections.OrderedDict
        the cmdline now also containing the added parameters.
    """
    cmdline.update(parse_parameter(parameter) for parameter in parameters_to_add)
    return cmdline
