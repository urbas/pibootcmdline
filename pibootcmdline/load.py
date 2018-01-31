from collections import OrderedDict

from pibootcmdline.defaults import DEFAULT_BOOT_CMDLINE_FILE


def from_str(boot_cmdline):
    """
    Parameters
    ----------
    boot_cmdline : str
        the contents of the ``/boot/cmdline.txt`` file.

    Returns
    -------
    list[tuple]
        a dictionary representation of the ``/boot/cmdline.txt`` file.
    """
    return [parse_parameter(element) for element in boot_cmdline.split(' ') if element.strip()]


def from_file(filename=DEFAULT_BOOT_CMDLINE_FILE):
    """

    Parameters
    ----------
    filename:str, optional
        the name of the file to load. If omitted, ``/boot/cmdline.txt`` is used.

    Returns
    -------
    list[tuple]
        a dictionary representation of the ``/boot/cmdline.txt`` file.
    """
    with open(filename, 'r') as fh:
        return from_str(fh.read())


def parse_parameter(boot_cmdline):
    key_value = boot_cmdline.split('=', 1)
    if len(key_value) == 2:
        value_list = key_value[1].split(',')
        if len(value_list) > 1:
            value = value_list
        else:
            value = value_list[0]
    else:
        value = None
    return key_value[0], value
