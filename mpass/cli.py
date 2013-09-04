from getpass import getpass
from mpass import mpass

def main(argv):
    if len(argv) == 2:
        domain = argv[1]
    else:
        domain = raw_input('Domain: @')

    master_password = getpass('Master Password: ')
    print mpass(master_password, domain)
