#!/usr/bin/python3

FLAG_FILE = "Flag3-1.webp.gz.xz.lzma"

DELAY = 'delay delay-time=0.030;'

#TWO_BIT = [
#        'beep frequency=200 length=0.01;',
#        'beep frequency=320 length=0.01;',
#        'beep frequency=512 length=0.01;',
#        'beep frequency=820 length=0.01;',
#        ]

TWO_BIT = [
        '$a;',
        '$b;',
        '$c;',
        '$d;',
        ]

def encode_byte(x):
    return TWO_BIT[x>>6] + \
           TWO_BIT[(x>>4)&3] + \
           TWO_BIT[(x>>2)&3] + \
           TWO_BIT[(x)&3]


with open(FLAG_FILE, 'rb') as f:
    data = f.read()
    print(':global a do={beep frequency=1000 length=0.02;delay delay-time=0.030}')
    print(':global b do={beep frequency=2000 length=0.02;delay delay-time=0.030}')
    print(':global c do={beep frequency=4000 length=0.02;delay delay-time=0.030}')
    print(':global d do={beep frequency=8000 length=0.02;delay delay-time=0.030}')
    for byte in data:
        print(encode_byte(byte))

print("# Total time =", len(data) * 0.12, "s.")
