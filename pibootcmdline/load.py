from collections import OrderedDict


def from_str(boot_cmdline):
    """
    Parameters
    ----------
    boot_cmdline : str
        the contents of the ``/boot/cmdline.txt`` file.

    Returns
    -------
    OrderedDict
        a dictionary representation of the ``/boot/cmdline.txt`` file.
    """
    return OrderedDict(_parse_element(element) for element in boot_cmdline.split(' ') if element.strip())


def from_file(filename='/boot/cmdline.txt'):
    """

    Parameters
    ----------
    filename:str, optional
        the name of the file to load. If omitted, ``/boot/cmdline.txt`` is used.

    Returns
    -------
    OrderedDict
        a dictionary representation of the ``/boot/cmdline.txt`` file.
    """
    with open(filename, 'r') as fh:
        return from_str(fh.read())


def _parse_element(boot_cmdline):
    key_value = boot_cmdline.split('=', 1)
    value = key_value[1] if len(key_value) == 2 else None
    return key_value[0], value
