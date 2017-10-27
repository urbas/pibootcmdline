from collections import OrderedDict

from pibootcmdline.edit import add_parameters, add_list_value


def test_add_nothing():
    assert add_parameters(OrderedDict(), []) == {}


def test_add_simple_parameter():
    assert add_parameters(OrderedDict(), ['rootwait']) == {'rootwait': None}


def test_add_keyval_parameter():
    assert add_parameters(OrderedDict([('foo', 'bar')]), ['foo=moo']) == {'foo': 'moo'}


def test_add_list_value():
    assert add_list_value(OrderedDict([('modules-load', 'dwc2')]), ['modules-load=g_ether']) == \
           {'modules-load': ['dwc2', 'g_ether']}


def test_add_first_list_value():
    assert add_list_value(OrderedDict([('modules-load', None)]), ['modules-load=g_ether']) == \
           {'modules-load': 'g_ether'}
