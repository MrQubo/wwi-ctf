xor r0 r0 r0
mov r1 1
mov r2 10
mov r3 128

; Display greating 
mov tty 'W'
mov tty 'e'
mov tty 'l'
mov tty 'c'
mov tty 'o'
mov tty 'm'
mov tty 'e'
mov tty '!'
mov tty 10
mov tty 'I'
mov tty 'n'
mov tty 'p'
mov tty 'u'
mov tty 't'
mov tty ' '
mov tty 'f'
mov tty 'l'
mov tty 'a'
mov tty 'g'
mov tty ':'
mov tty 10

; Read flag
xor adr adr adr
readloop:
    mov mem kbd
    sub r7 mem r3
    wneg ip r7 $readloop
    xor mem mem r3
    mov kbd r0
    mov tty mem
    xor r7 mem r2
    nzer r7 r7 
    add adr adr r1
    wneg ip r7 $readloop

; Verify flag
mov tty 'V'
mov tty 'e'
mov tty 'r'
mov tty 'i'
mov tty 'f'
mov tty 'y'
mov tty 'i'
mov tty 'n'
mov tty 'g'


xor r3 adr 5 ;TODO set flag length here

sub adr adr r1
xor r7 mem '}'
or r3 r3 r7

xor adr adr adr

xor r7 mem 'w'
add mem mem r1
or r3 r3 r7

xor r7 mem 'w'
add mem mem r1
or r3 r3 r7

xor r7 mem 'i'
add mem mem r1
or r3 r3 r7

xor r7 mem '{'
add mem mem r1
or r3 r3 r7

nzer r3 r3
wneg ip r3 $fail

mov tty '.'
mov tty '.'
mov tty '.'

nzer r3 r3
wnneg ip r3 $success

fail:
    mov tty ' '
    mov tty 'W'
    mov tty 'R'
    mov tty 'O'
    mov tty 'N'
    mov tty 'G'
    mov tty '!'
    mov ip $inf_loop

success:
    mov tty ' '
    mov tty 'V'
    mov tty 'a'
    mov tty 'l'
    mov tty 'i'
    mov tty 'd'
    mov tty ' '
    mov tty ':'
    mov tty ')'

inf_loop: mov ip $inf_loop
