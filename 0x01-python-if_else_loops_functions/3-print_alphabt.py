#!/usr/bin/python3
for alx in range(ord('a'), ord('z') + 1):
    if chr(alx) != 'q' and chr(alx) != 'e':
        print('{}'.format(chr(alx)), end='')
