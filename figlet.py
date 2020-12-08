#!/usr/bin/env python
'''Contains `get_figlet()` method which returns ASCII art title.
x1b[38;2;140;28;32m   <-- dark red
x1b[38;2;119;121;174m <-- mostly desaturated dark blue
x1b[38;2;213;122;100m <-- moderate red
'''

def get_figlet():
    '''Returns ASCII art title "Scrape Dark Sky".'''
    figlet = '''\x1b[38;2;140;28;32m
   _____                             _____             _       _____ _
  / ____|                           |  __ \           | |     / ____| |
 | (___   ___ _ __ __ _ _ __   ___  | |  | | __ _ _ __| | __ | (___ | | ___   _
  \___ \ / __| '__/ _` | '_ \ / _ \ | |  | |/ _` | '__| |/ /  \___ \| |/ / | | |\x1b[38;2;119;121;174m
  ____) | (__| | | (_| | |_) |  __/ | |__| | (_| | |  |   <   ____) |   <| |_| |
 |_____/ \___|_|  \__,_| .__/ \___| |_____/ \__,_|_|  |_|\_\ |_____/|_|\_\___, |\x1b[38;2;140;28;32m
                       | |                                                 __/ |
                       |_|                                                |___/\x1b[0m'''
    return figlet


if __name__ == '__main__':
    get_figlet()
