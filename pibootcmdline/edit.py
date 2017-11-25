from pibootcmdline.parse import parse_parameter, Parameter


def add_parameters(cmdline, *parameters):
    """
    Parameters
    ----------
    cmdline: list[Parameter]
        parsed command line to which to add parameters.

    *parameters: str
        list of string parameters. For example: 'key=value' or 'key' or 'key=value1,value2'.

    Returns
    -------
    list[Parameter]
        the cmdline now also containing the added parameters.
    """
    return cmdline + [parse_parameter(parameter) for parameter in parameters]


def set_parameters(cmdline, *parameters):
    """
    Parameters
    ----------
    cmdline: list[Parameter]
        parsed command line to which to add parameters.

    *parameters: str
        list of string parameters. For example: 'key=value' or 'key' or 'key=value1,value2'.

    Returns
    -------
    list[Parameter]
        the cmdline with changed or added parameters.
    """
    new_params = [parse_parameter(param) for param in parameters]
    new_cmdline = [_set_value(to_param, new_params) for to_param in cmdline]
    for new_param in new_params:
        if _index_of_key(new_cmdline, new_param.key) is None:
            new_cmdline.append(new_param)
    return new_cmdline


def add_to_value(cmdline, *parameters):
    """
    This function will append comma-separated values to already existing values of a particular parameter.
    For example, if the command line already contains the parameter ``modules-load=dwc2`` and you call `
    `add-list-value modules-load=g_ether`` then the resulting command line will contain ``modules-load=dwc2,g_ether``.

    Parameters
    ----------
    cmdline: list[Parameter]
        parsed command line to which to add parameters.

    parameters: str
        list of string parameters. For example: 'key=value' or 'key' or 'key=value1,value2'.

    Returns
    -------
    list[Parameter]
        the cmdline now also containing the added parameters.
    """
    from_params = [parse_parameter(param) for param in parameters]
    new_cmdline = [_add_to_value(to_param, from_params) for to_param in cmdline]
    for from_param in from_params:
        if _index_of_key(new_cmdline, from_param.key) is None:
            new_cmdline.append(from_param)
    return new_cmdline


def _set_value(param, new_params):
    new_param = param
    for to_param in new_params:
        if param.key == to_param.key:
            new_param = to_param
    return new_param


def _add_to_value(to_param, from_params):
    new_param = to_param
    for from_param in from_params:
        if to_param.key == from_param.key:
            new_param = Parameter(to_param.key, new_param.values + from_param.values)
    return new_param


def _index_of_key(cmdline, key):
    for i, param in enumerate(cmdline):
        if param.key == key:
            return i
    return None
