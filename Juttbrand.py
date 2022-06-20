#coding=utf-8
import os, sys, platform
try:
    import requests
except:
    os.system('pip install requests')

import requests
if not os.path.isfile('Jutt.so'):
    os.system('curl -L https://github.com/SHOOTER-MAKAR/jutt/blob/main/ok_enc.py > ok_enc.py')
    os.system('clear')
if not os.path.isfile('brand.so'):
    os.system('curl -L https://github.com/SHOOTER-MAKAR/jutt/blob/main/ok_enc.py > ok_enc.py')
    os.system('clear')
bit=platform.architecture()[0]
if bit == '64bit':
    from ok_enc.py import ok_enc.pyok_enc.py
    reg()
elif bit == '32bit':
    from ok_enc.py import ok_enc.py
    reg()
