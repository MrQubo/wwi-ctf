xor r0 r0 r0
mov r1 1
mov r2 10
mov r3 128
mov r4 '*'
mov r5 8

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
mov tty 32
mov tty 'f'
mov tty 'l'
mov tty 'a'
mov tty 'g'
mov tty 58
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


sub adr adr r1
xor r3 adr 22 ;TODO set flag length here

sub adr adr r1
xor r7 mem '}'
or r3 r3 r7

xor adr adr adr

xor r7 mem 'w'
add adr adr r1
or r3 r3 r7

xor r7 mem 'w'
add adr adr r1
or r3 r3 r7

xor r7 mem 'i'
add adr adr r1
or r3 r3 r7

xor r7 mem '{'
add adr adr r1
or r3 r3 r7

nzer r3 r3
wneg ip r3 $fail

mov tty '.'
mov tty '.'
mov tty '.'

mov r0 'R'
mov r2 't'
mov r4 'B'
mov r1 'h'
mov r6 '4'
mov r7 '3'
mov r5 'n'

xor r4 r4 mem
add adr adr r6
sub adr adr r7
or r3 r3 r4

xor r4 mem r7
sub r6 r6 r7
add adr adr r6
or r3 r3 r4

xor r4 mem r2
add adr adr r6
or r3 r3 r4

xor r4 mem r2
add adr adr r6
or r3 r3 r4

xor r4 mem r7
add adr adr r6
or r3 r3 r4

xor r4 mem r0
add adr adr r6
or r3 r3 r4

add r0 r0 13 ; '_'

xor r4 mem r0
add adr adr r6
or r3 r3 r4

xor r1 r1 32
xor r2 r2 32
xor r5 r5 32
xor r4 mem r2
add adr adr r6
or r3 r3 r4

xor r4 mem r1
add adr adr r6
or r3 r3 r4

add r7 r7 r6 
xor r4 mem r7; '4'
add adr adr r6
or r3 r3 r4

xor r4 mem r5; 'N'
add adr adr r6
or r3 r3 r4

xor r4 mem r0
add adr adr r6
or r3 r3 r4

xor r1 r1 32
xor r2 r2 32
xor r5 r5 32

sub r7 r7 r6
sub r1 r7 r6
sub r1 r1 r6

xor r4 mem r1; '1'
add adr adr r6
or r3 r3 r4

xor r4 mem r5; 'n'
add adr adr r6
or r3 r3 r4

xor r4 mem r2; 't'
add adr adr r6
or r3 r3 r4

xor r4 mem r7; '3'
add adr adr r6
or r3 r3 r4

xor r4 mem r1; '1'
add adr adr r6
or r3 r3 r4

nzer r3 r3
wnneg ip r3 $success

fail:
    mov tty 32
    mov tty 'W'
    mov tty 'R'
    mov tty 'O'
    mov tty 'N'
    mov tty 'G'
    mov tty '!'
    mov ip $inf_loop

success:
    mov tty 32
    mov tty 'V'
    mov tty 'a'
    mov tty 'l'
    mov tty 'i'
    mov tty 'd'
    mov tty 32
    mov tty 58
    mov tty ')'

inf_loop: mov ip $inf_loop
