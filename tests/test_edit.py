from collections import OrderedDict

from pibootcmdline.edit import add_parameters


def test_add_nothing():
    assert add_parameters(OrderedDict(), []) == {}


def test_add_simple_parameter():
    assert add_parameters(OrderedDict(), ['rootwait']) == {'rootwait': None}
