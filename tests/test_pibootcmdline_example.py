import pytest

_cmdline_before = 'console=tty1 rootfstype=ext4 modules-load=dwc2'

_cmdline_after = 'console=tty1 rootfstype=ext3 modules-load=dwc2,g_ether console=tty2'


def test_example(boot_cmdline_path):
    boot_cmdline_file = boot_cmdline_path.strpath

    # Example start
    from pibootcmdline.parse import from_file
    from pibootcmdline.write import to_file
    from pibootcmdline.edit import add_parameters, set_parameters, add_to_value

    cmdline = from_file(boot_cmdline_file)
    cmdline = set_parameters(cmdline, 'rootfstype=ext3')
    cmdline = add_parameters(cmdline, 'console=tty2')
    cmdline = add_to_value(cmdline, 'modules-load=g_ether')
    to_file(cmdline, boot_cmdline_file)
    # Example end

    assert boot_cmdline_path.read() == _cmdline_after


@pytest.fixture(scope='session')
def boot_cmdline_path(tmpdir_factory):
    fn = tmpdir_factory.mktemp('data').join('cmdline.txt')
    fn.write(_cmdline_before)
    return fn
