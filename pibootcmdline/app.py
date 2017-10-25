import argparse

from pibootcmdline.defaults import DEFAULT_BOOT_CMDLINE_FILE
from pibootcmdline.edit import add_parameters
from pibootcmdline.load import from_str
from pibootcmdline.store import to_file, to_str


def run():
    args = _parse_args()
    cmdline = from_str(args.file)
    cmdline = add_parameters(cmdline, args.parameters_to_add or [])
    if args.in_place:
        to_file(cmdline, args.file)
    else:
        print(to_str(cmdline))


def _parse_args():
    parser = argparse.ArgumentParser(description="Edit Raspbian's /boot/cmdline.txt.")

    parser.add_argument("-f", "--file", default=DEFAULT_BOOT_CMDLINE_FILE,
                        help="The cmdline file to manipulate.")
    parser.add_argument("-i", "--in-place", action='store_true', default=False,
                        help="Indicates that the cmdline file should be modified in place. By default the new content "
                             "is printed to stdout.")

    subparsers = parser.add_subparsers()

    parser_add = subparsers.add_parser("add", help="Adds a parameter to the cmdline file. "
                                                   "If the parameter already exists, it will be overwritten.")
    parser_add.add_argument("parameters_to_add", nargs='+', help="The parameter to add to the cmdline file.")

    return parser.parse_args()
