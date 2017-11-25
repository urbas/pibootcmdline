from pibootcmdline.edit import add_parameters, add_to_value
from pibootcmdline.parse import Parameter


def test_add_nothing():
    assert add_parameters([]) == []


def test_add_simple_parameter():
    assert add_parameters([], 'rootwait') == [Parameter('rootwait', [])]


def test_add_keyval_parameter():
    assert add_parameters([Parameter('foo', ['bar'])], 'foo=moo') == \
           [Parameter('foo', ['bar']), Parameter('foo', ['moo'])]


def test_add_to_value():
    assert add_to_value([Parameter('modules-load', ['dwc2'])], 'modules-load=g_ether') == \
           [Parameter('modules-load', ['dwc2', 'g_ether'])]


def test_add_first_value():
    assert add_to_value(([Parameter('modules-load', [])]), 'modules-load=g_ether') == \
           [Parameter('modules-load', ['g_ether'])]


def test_add_to_empty_cmdline():
    assert add_to_value(([]), 'modules-load=g_ether') == [Parameter('modules-load', ['g_ether'])]
