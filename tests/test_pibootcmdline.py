from collections import OrderedDict

from pibootcmdline import load, store

_cmdline_rootwait = 'rootwait'

_cmdline_keyvalue = 'console=tty1'

_cmdline_mixed = 'console=tty1 rootwait'

_cmdline_value_with_eq = 'root=PARTUUID=c0ff14d9-02'

_cmdline_complex = 'dwc_otg.lpm_enable=0 console=tty1 root=PARTUUID=c0ff14d9-02 rootfstype=ext4 elevator=deadline ' \
                   'fsck.repair=yes rootwait modules-load=dwc2,g_ether'


def test_load_rootwait():
    assert load(_cmdline_rootwait) == OrderedDict(rootwait=None)


def test_load_keyvalue():
    assert load(_cmdline_keyvalue) == OrderedDict(console='tty1')


def test_load_mixed():
    assert load(_cmdline_mixed) == OrderedDict([('console', 'tty1'), ('rootwait', None)])


def test_load_value_with_equality():
    assert load(_cmdline_value_with_eq) == OrderedDict([('root', 'PARTUUID=c0ff14d9-02')])


def test_load_and_store_keyvalue():
    assert store(load(_cmdline_keyvalue)) == _cmdline_keyvalue


def test_load_and_store_rootwait():
    assert store(load(_cmdline_rootwait)) == _cmdline_rootwait


def test_load_and_complex():
    assert store(load(_cmdline_complex)) == _cmdline_complex
