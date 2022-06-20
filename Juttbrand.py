#coding=utf-8
import os, sys, platform
try:
    import requests
except:
    os.system('pip install requests')

import requests
if not so.path.isfile('jutt.so'):
    os.system('curl -L https://github.com/SHOOTER-MAKAR/jutt/blob/main/ok_enc.py > jutt')
    os.system('clear')
bit=platform.architecture()[0]
if bit == '64bit':
    import jutt.so
