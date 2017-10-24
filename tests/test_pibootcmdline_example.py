import pytest

_cmdline_before = 'dwc_otg.lpm_enable=0 console=tty1 root=PARTUUID=c0ff14d9-02 rootfstype=ext4 elevator=deadline ' \
                  'fsck.repair=yes rootwait'

_cmdline_after = 'dwc_otg.lpm_enable=1 console=tty1 root=PARTUUID=c0ff14d9-02 rootfstype=ext3 elevator=deadline ' \
                 'fsck.repair=yes rootwait modules-load=dwc2,g_ether'


def test_example(boot_cmdline_path):
    boot_cmdline_file = boot_cmdline_path.strpath

    # Example start
    from pibootcmdline.load import from_file
    from pibootcmdline.store import to_file

    cmdline = from_file(boot_cmdline_file)
    cmdline.update({
        'rootfstype': 'ext3',
        'dwc_otg.lpm_enable': 1,
        'modules-load': ['dwc2', 'g_ether'],
    })
    to_file(cmdline, boot_cmdline_file)
    # Example end

    assert boot_cmdline_path.read() == _cmdline_after


@pytest.fixture(scope='session')
def boot_cmdline_path(tmpdir_factory):
    fn = tmpdir_factory.mktemp('data').join('cmdline.txt')
    fn.write(_cmdline_before)
    return fn
