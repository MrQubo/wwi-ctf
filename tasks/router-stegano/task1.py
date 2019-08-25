#!/usr/bin/python3

FLAG = "wwi{ICom31nPeac3}"

DELAY = 'delay delay-time=0.5;'

#TWO_BIT = [
#        'beep frequency=200 length=0.25;',
#        'beep frequency=320 length=0.25;',
#        'beep frequency=512 length=0.25;',
#        'beep frequency=820 length=0.25;',
#        ]

TWO_BIT = [
        'beep frequency=1000 length=0.25;',
        'beep frequency=2000 length=0.25;',
        'beep frequency=4000 length=0.25;',
        'beep frequency=8000 length=0.25;',
        ]

def encode_byte(x):
    return TWO_BIT[x>>6] + DELAY \
         + TWO_BIT[(x>>4)&3] + DELAY \
         + TWO_BIT[(x>>2)&3] + DELAY \
         + TWO_BIT[(x)&3] + DELAY

for c in FLAG:
    print(encode_byte(ord(c)))

print ("# Total time=", len(FLAG)*2, "s")
