import pytest

from pibootcmdline.parse import from_str, from_file
from pibootcmdline.write import to_str, to_file

_cmdline_rootwait = 'rootwait'

_cmdline_keyvalue = 'console=tty1'

_mixed_cmdline_loaded = [('console', 'tty1'), ('rootwait', None)]

_cmdline_complex = 'dwc_otg.lpm_enable=0 console=tty1 root=PARTUUID=c0ff14d9-02 rootfstype=ext4 elevator=deadline ' \
                   'fsck.repair=yes rootwait modules-load=dwc2,g_ether'


def test_load_and_store_keyvalue():
    assert to_str(from_str(_cmdline_keyvalue)) == _cmdline_keyvalue


def test_load_and_store_rootwait():
    assert to_str(from_str(_cmdline_rootwait)) == _cmdline_rootwait


def test_load_and_complex():
    assert to_str(from_str(_cmdline_complex)) == _cmdline_complex


def test_store_file(empty_file):
    to_file(_mixed_cmdline_loaded, empty_file)
    assert from_file(empty_file) == _mixed_cmdline_loaded


@pytest.fixture(scope='session')
def empty_file(tmpdir_factory):
    fn = tmpdir_factory.mktemp('data').join('cmdline.txt')
    return fn.strpath
