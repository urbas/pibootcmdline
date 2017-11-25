def to_str(boot_cmdline):
    """
    Parameters
    ----------
    boot_cmdline: list[Parameter]
        a list of parameters to convert to a cmdline string.

    Returns
    -------
    str
        the cmdline string of key/values that can be writen into the ``/boot/cmdline.txt`` file.
    """
    return ' '.join(_print_parameter(parameter) for parameter in boot_cmdline)


def to_file(contents, filename='/boot/cmdline.txt'):
    """
    Parameters
    ----------
    contents: list[Parameter]
        a list of parameters to be stored into the cmdline file.
    filename: str, optional
        the name of the file to load. If omitted, ``/boot/cmdline.txt`` is used.
    """
    with open(filename, 'w') as fh:
        fh.write(to_str(contents))


def _print_parameter(parameter):
    return '{}={}'.format(parameter.key, ','.join(parameter.values)) if parameter.values else parameter.key
