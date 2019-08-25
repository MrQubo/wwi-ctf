#!/usr/bin/python3

FLAG_FILE = "flag2.txt.gz"

DELAY = 'delay delay-time=0.15;'

#TWO_BIT = [
#        'beep frequency=200 length=0.1;',
#        'beep frequency=320 length=0.1;',
#        'beep frequency=512 length=0.1;',
#        'beep frequency=820 length=0.1;',
#        ]

#TWO_BIT = [
#        'beep frequency=250 length=0.1;',
#        'beep frequency=500 length=0.1;',
#        'beep frequency=1000 length=0.1;',
#        'beep frequency=2000 length=0.1;',
#        ]

TWO_BIT = [
        'beep frequency=1000 length=0.1;',
        'beep frequency=2000 length=0.1;',
        'beep frequency=4000 length=0.1;',
        'beep frequency=8000 length=0.1;',
        ]


def encode_byte(x):
    return TWO_BIT[x>>6] + DELAY \
         + TWO_BIT[(x>>4)&3] + DELAY \
         + TWO_BIT[(x>>2)&3] + DELAY \
         + TWO_BIT[(x)&3] + DELAY


with open(FLAG_FILE, 'rb') as f:
    data = f.read()
    for byte in data:
        print(encode_byte(byte))

print("# Total time =", len(data) * 0.60, "s.")
