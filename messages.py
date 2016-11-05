#!/usr/bin/env python
# -*- coding: utf-8 -*-
# messages colour script

reset = "\x1B[0m"
default = "\x1B[39m"
black = "\x1B[30m"
red = "\x1B[31m"
green = "\x1B[32m"
yellow = "\x1B[33m"
blue = "\x1B[34m"
magenta = "\x1B[35m"
cyan = "\x1B[36m"
lightgray = "\x1B[38m"
darkgray = "\x1B[90m"
lightred = "\x1B[91m"
lightgreen = "\x1B[92m"
lightyellow = "\x1B[93m"
lightblue = "\x1B[94m"
lightmagenta = "\x1B[95m"
lightcyan = "\x1B[96m"
white = "\x1B[97m"

shape = [
    u"  ▄▄▄▄▄▄▄▄  ",
    u" ██▀▀▀▀▀▀██ ",
    u" ██▀▀▀▀▀▀██ ",
    u" ██████████ ",
    u"  ▀▀▀▀███▀  ",
    u"       ▀▀▀  "
]

coloursets = [
    [yellow, red, green, blue, magenta, cyan],
    [lightyellow, lightred, lightgreen, lightblue, lightmagenta, lightcyan]
]

for colours in coloursets:
    print
    for line in shape:
        for colour in colours:
            print colour + line,
        print
print reset