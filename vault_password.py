# https://github.com/Empire-of-Code-Puzzles/checkio-empire-vault-password

import re
golf=lambda r:re.match("(?=.*[A-Z])(?=.*[a-z])(?=.*\d).{10,}",r)
