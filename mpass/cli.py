from getpass import getpass
from mpass import mpass, gui

def main(argv):
    if len(argv) >= 2 and argv[1] == 'gui':
        gui.main(argv)
        return

    if len(argv) == 2:
        domain = argv[1]
    else:
        domain = raw_input('Domain: @')

    master_password = getpass('Master Password: ')
    print mpass(master_password, domain)
