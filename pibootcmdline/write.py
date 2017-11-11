def to_str(boot_cmdline):
    """
    Parameters
    ----------
    boot_cmdline: OrderedDit
        a dictionary of key-values to convert to a cmdline string.

    Returns
    -------
    OrderedDict
        the cmdline string of key/values that can be writen into the ``/boot/cmdline.txt`` file.
    """
    return ' '.join(_print_element(key, value) for key, value in boot_cmdline.items())


def to_file(contents, filename='/boot/cmdline.txt'):
    """
    Parameters
    ----------
    contents: OrderedDict
        a dictionary of key/values to be stored into the cmdline file.
    filename: str, optional
        the name of the file to load. If omitted, ``/boot/cmdline.txt`` is used.
    """
    with open(filename, 'w') as fh:
        fh.write(to_str(contents))


def _print_element(key, value):
    return '{}={}'.format(key, _print_value(value)) if value is not None else key


def _print_value(value):
    if isinstance(value, list):
        return ','.join(value)
    return value
