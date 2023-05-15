#!/usr/bin/env python
# -*- coding: utf-8 -*-


import alluxio
from alluxio import option

filepath = "/Data/test.json"
server = "localhost"
port = 39999

client = alluxio.Client(server, port)
if client.exists('/Data'):
    print('File exists')
    file_status = client.get_status(filepath)
    print('File size:', file_status.length)
    print('Permission:', file_status.permission)
else:
    print('File does not exist')

