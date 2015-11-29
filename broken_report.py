# https://github.com/Empire-of-Code-Puzzles/checkio-empire-broken-report

import re
golf=lambda r:sum([ord(a)*9-585+int(b) for a,b in re.findall('[A-Z][1-9]',r)])
