#!C:\Eluminate\System\ImageScripter\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'scapy==2.4.3','console_scripts','UTscapy'
__requires__ = 'scapy==2.4.3'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('scapy==2.4.3', 'console_scripts', 'UTscapy')()
    )
