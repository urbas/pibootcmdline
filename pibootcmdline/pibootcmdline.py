"""Main module."""
from collections import OrderedDict


def load(boot_cmdline):
    return OrderedDict(_parse_element(element) for element in boot_cmdline.split(' '))


def store(boot_cmdline):
    return ' '.join(_print_element(key, value) for key, value in boot_cmdline.items())


def _print_element(key, value):
    return key + '=' + value if value is not None else key


def _parse_element(boot_cmdline):
    key_value = boot_cmdline.split('=', maxsplit=1)
    value = key_value[1] if len(key_value) == 2 else None
    return key_value[0], value
