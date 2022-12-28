#!/usr/bin/env python
# -*- coding: utf-8 -*-

import dxl
import os

if os.name == 'nt':
    import msvcrt
    def getch():
        return msvcrt.getch().decode()
else:
    import sys, tty, termios
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    def getch():
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

dxl.bringup(1)
dxl.setting(1, 50, 20)
init_position=dxl.read(1).call()
dxl.bringup(2)
dxl.setting(2, 50, 20)
init_position2=dxl.read(2).call()
dxl.bringup(3)
dxl.setting(3, 50, 20)
init_position3=dxl.read(3).call()
dxl.bringup(4)
dxl.setting(4, 50, 20)
init_position4=dxl.read(4).call()
dxl.bringup(5)
dxl.setting(5, 50, 20)
init_position5=dxl.read(5).call()
dxl.bringup(6)
dxl.setting(6, 50, 20)
init_position6=dxl.read(6).call()
dxl.bringup(7)
dxl.setting(7, 50, 20)
init_position7=dxl.read(7).call()
dxl.bringup(8)
dxl.setting(8, 50, 20)
init_position8=dxl.read(8).call()
dxl.bringup(9)
dxl.setting(9, 50, 20)
init_position9=dxl.read(9).call()

while 1:
    print("Press key! (w/s/x/esc)")
    direction = getch()
    if direction == chr(0x1b):
        break

    # '1' 입력 시
    elif direction == chr(0x31):
        dxl.goal(1, init_position+7500)
        
    # '2' 입력 시
    elif direction == chr(0x32):
        dxl.goal(2, init_position2+7500)

    # '3' 입력 시
    elif direction == chr(0x33):
        dxl.goal(3, init_position3+7500)

    # '4' 입력 시
    elif direction == chr(0x34):
        dxl.goal(4, init_position4+7500)

    # '5' 입력 시
    elif direction == chr(0x35):
        dxl.goal(5, init_position5+7500)

    # '6' 입력 시
    elif direction == chr(0x36):
        dxl.goal(6, init_position6+7500)
        
    # '7' 입력 시
    elif direction == chr(0x37):
        dxl.goal(7, init_position7+7500)

    # '8' 입력 시
    elif direction == chr(0x38):
        dxl.goal(8, init_position8+7500)

    # '9' 입력 시
    elif direction == chr(0x39):
        dxl.goal(9, init_position9+7500)

    # 'q' 입력 시
    elif direction == chr(0x31):
        dxl.goal(1, init_position)
        
    # 'w' 입력 시
    elif direction == chr(0x32):
        dxl.goal(2, init_position2)

    # 'e' 입력 시
    elif direction == chr(0x33):
        dxl.goal(3, init_position3)

    # 'r' 입력 시
    elif direction == chr(0x34):
        dxl.goal(4, init_position4)

    # 't' 입력 시
    elif direction == chr(0x74):
        dxl.goal(5, init_position5)

    # 'y' 입력 시
    elif direction == chr(0x79):
        dxl.goal(6, init_position6)
        
    # 'u' 입력 시
    elif direction == chr(0x75):
        dxl.goal(7, init_position7)

    # 'i' 입력 시
    elif direction == chr(0x69):
        dxl.goal(8, init_position8)

    # 'o' 입력 시
    elif direction == chr(0x6F):
        dxl.goal(9, init_position9)  

