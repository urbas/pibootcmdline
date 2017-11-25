import pytest

from pibootcmdline.parse import from_str, from_file, Parameter

_cmdline_rootwait = 'rootwait'

_cmdline_keyvalue = 'console=tty1'

_cmdline_mixed = 'console=tty1 rootwait'
_mixed_cmdline_loaded = [Parameter('console', ['tty1']), Parameter('rootwait', [])]

_cmdline_value_with_eq = 'root=PARTUUID=c0ff14d9-02'

_cmdline_list_value = 'modules-load=dwc2,g_ether'

_cmdline_complex = 'dwc_otg.lpm_enable=0 console=tty1 root=PARTUUID=c0ff14d9-02 rootfstype=ext4 elevator=deadline ' \
                   'fsck.repair=yes rootwait modules-load=dwc2,g_ether'

_cmdline_multi_spaces = 'foo=42  bar'


def test_from_str_positional():
    assert from_str(_cmdline_rootwait) == [Parameter('rootwait', [])]


def test_from_str_keyval():
    assert from_str(_cmdline_keyvalue) == [Parameter('console', ['tty1'])]


def test_from_str_mixed():
    assert from_str(_cmdline_mixed) == _mixed_cmdline_loaded


def test_from_str_value_equals_char():
    assert from_str(_cmdline_value_with_eq) == [Parameter('root', ['PARTUUID=c0ff14d9-02'])]


def test_from_file(cmdline_file):
    assert from_file(cmdline_file) == _mixed_cmdline_loaded


def test_from_str_multi_spaces():
    assert from_str(_cmdline_multi_spaces) == [Parameter('foo', ['42']), Parameter('bar', [])]


def test_from_str_list_value():
    assert from_str(_cmdline_list_value) == [Parameter('modules-load', ['dwc2', 'g_ether'])]


@pytest.fixture(scope='session')
def cmdline_file(tmpdir_factory):
    fn = tmpdir_factory.mktemp('data').join('cmdline.txt')
    fn.write(_cmdline_mixed)
    return fn.strpath


@pytest.fixture(scope='session')
def empty_file(tmpdir_factory):
    fn = tmpdir_factory.mktemp('data').join('cmdline.txt')
    return fn.strpath
