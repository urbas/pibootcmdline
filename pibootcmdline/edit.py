from pibootcmdline.load import parse_parameter


def add_parameters(cmdline, parameters_to_add):
    """
    Parameters
    ----------
    cmdline: collections.OrderedDict
        parsed command line to which to add parameters.

    parameters_to_add: list[str]
        list of string parameters. For example: 'key=value' or 'key' or 'key=value1,value2'.

    Returns
    -------
    collections.OrderedDict
        the cmdline now also containing the added parameters.
    """
    cmdline.update(parse_parameter(parameter) for parameter in parameters_to_add)
    return cmdline


def add_list_value(cmdline, parameters_to_add):
    """
    This function will append comma-separated values to already existing values of a particular parameter.
    For example, if the command line already contains the parameter ``modules-load=dwc2`` and you call `
    `add-list-value modules-load=g_ether`` then the resulting command line will contain ``modules-load=dwc2,g_ether``.

    Parameters
    ----------
    cmdline: collections.OrderedDict
        parsed command line to which to add parameters.

    parameters_to_add: list[str]
        list of string parameters. For example: 'key=value' or 'key' or 'key=value1,value2'.

    Returns
    -------
    collections.OrderedDict
        the cmdline now also containing the added parameters.
    """
    for parameter in parameters_to_add:
        key, value_to_add = parse_parameter(parameter)
        existing_value = cmdline.get(key, None)
        if existing_value is None:
            new_value = value_to_add
        else:
            new_value = [existing_value, value_to_add]
        cmdline[key] = new_value
    return cmdline
