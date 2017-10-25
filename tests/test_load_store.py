from collections import OrderedDict

import pytest

from pibootcmdline.load import from_str, from_file
from pibootcmdline.store import to_str, to_file

_cmdline_rootwait = 'rootwait'

_cmdline_keyvalue = 'console=tty1'

_cmdline_mixed = 'console=tty1 rootwait'
_mixed_cmdline_loaded = OrderedDict([('console', 'tty1'), ('rootwait', None)])

_cmdline_value_with_eq = 'root=PARTUUID=c0ff14d9-02'

_cmdline_list_value = 'modules-load=dwc2,g_ether'

_cmdline_complex = 'dwc_otg.lpm_enable=0 console=tty1 root=PARTUUID=c0ff14d9-02 rootfstype=ext4 elevator=deadline ' \
                   'fsck.repair=yes rootwait modules-load=dwc2,g_ether'

_cmdline_multi_spaces = 'foo=42  bar'


def test_load_rootwait():
    assert from_str(_cmdline_rootwait) == OrderedDict(rootwait=None)


def test_load_keyvalue():
    assert from_str(_cmdline_keyvalue) == OrderedDict(console='tty1')


def test_load_mixed():
    assert from_str(_cmdline_mixed) == _mixed_cmdline_loaded


def test_load_value_with_equality():
    assert from_str(_cmdline_value_with_eq) == OrderedDict([('root', 'PARTUUID=c0ff14d9-02')])


def test_load_and_store_keyvalue():
    assert to_str(from_str(_cmdline_keyvalue)) == _cmdline_keyvalue


def test_load_and_store_rootwait():
    assert to_str(from_str(_cmdline_rootwait)) == _cmdline_rootwait


def test_load_and_complex():
    assert to_str(from_str(_cmdline_complex)) == _cmdline_complex


def test_load_file(mixed_cmdline_file):
    assert from_file(mixed_cmdline_file) == _mixed_cmdline_loaded


def test_store_file(empty_file):
    to_file(_mixed_cmdline_loaded, empty_file)
    assert from_file(empty_file) == _mixed_cmdline_loaded


def test_load_multi_spaces():
    assert from_str(_cmdline_multi_spaces) == OrderedDict([('foo', '42'), ('bar', None)])


def test_load_list_value():
    assert from_str(_cmdline_list_value) == OrderedDict([('modules-load', ['dwc2', 'g_ether'])])


@pytest.fixture(scope='session')
def mixed_cmdline_file(tmpdir_factory):
    fn = tmpdir_factory.mktemp('data').join('cmdline.txt')
    fn.write(_cmdline_mixed)
    return fn.strpath


@pytest.fixture(scope='session')
def empty_file(tmpdir_factory):
    fn = tmpdir_factory.mktemp('data').join('cmdline.txt')
    return fn.strpath
