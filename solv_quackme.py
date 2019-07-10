#!/usr/bin/python3
# -*- coding: utf-8 -*-

import logging
import argparse

def quackme():
    key = [0x29, 0x06, 0x16, 0x4f, 0x2b, 0x35, 0x30, 0x1e, 0x51, 0x1b, 0x5b, 0x14, 0x4b, 0x08, 0x5d, 0x2b, 0x53, 0x10, 0x54, 0x51, 0x43, 0x4d, 0x5c, 0x54, 0x5d, 0x00]
    greet = "You have now entered the Duck Web, and you're in for a honkin' good time.\nCan you figure out my trick?"
    solv = []
    for i,el in enumerate(key):
        solv.append(el ^ ord(greet[i]))
    print("".join([chr(el) for el in solv]))
    # returns picoCTF{qu4ckm3_6b15c941}D

if __name__ == "__main__":
    quackme()
