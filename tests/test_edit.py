from collections import OrderedDict

from pibootcmdline.edit import update_parameters, add_list_value


def test_add_nothing():
    assert update_parameters([], []) == {}


def test_add_simple_parameter():
    assert update_parameters([], ['rootwait']) == {'rootwait': None}


def test_add_keyval_parameter():
    assert update_parameters(OrderedDict([('foo', 'bar')]), ['foo=moo']) == {'foo': 'moo'}


def test_add_list_value():
    assert add_list_value(OrderedDict([('modules-load', 'dwc2')]), ['modules-load=g_ether']) == \
           {'modules-load': ['dwc2', 'g_ether']}


def test_add_first_list_value():
    assert add_list_value(OrderedDict([('modules-load', None)]), ['modules-load=g_ether']) == \
           {'modules-load': 'g_ether'}
