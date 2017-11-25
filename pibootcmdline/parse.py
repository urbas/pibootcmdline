from collections import namedtuple

from pibootcmdline.defaults import DEFAULT_BOOT_CMDLINE_FILE

Parameter = namedtuple('Parameter', ['key', 'values'])


def from_str(boot_cmdline):
    """
    Parameters
    ----------
    boot_cmdline : str
        the contents of the ``/boot/cmdline.txt`` file.

    Returns
    -------
    list[Parameter]
        a list of parameters.
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
    list[Parameter]
        a list of parameters.
    """
    with open(filename, 'r') as fh:
        return from_str(fh.read())


def parse_parameter(boot_cmdline):
    key_value = boot_cmdline.split('=', 1)
    return Parameter(key_value[0], key_value[1].split(',') if len(key_value) == 2 else [])
