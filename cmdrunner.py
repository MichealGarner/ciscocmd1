#!/usr/bin/env python

"""NOTE:

This file is adapted from video's created for using Netmiko.
(https://www.youtube.com/watch?v=eiYemtNKS-M&list=PLtw40n4ybvFoHoigW7IwITNilmZn2cfNv)
This version was adapted by Micheal Garner, but all credit belongs to original author(Greg Mueller).

"""

from __future__ import absolute_import, division, print_function

import json
import mytools
import netmiko
import os
import signal
import sys

signal.signal(signal.SIGPIPE, signal.SIG_DFL)  # IOError: Broken pipe
signal.signal(signal.SIGINT, signal.SIG_DFL)  # KeyboardInterrupt: Ctrl-C


if len(sys.argv) < 3:
    print('Usage: cmdrunner.py commands.txt devices.json')
    exit()

netmiko_exceptions = (netmiko.ssh_exception.NetMikoTimeoutException,
                      netmiko.ssh_exception.NetMikoAuthenticationException)

username, password = mytools.get_credentials()

with open(sys.argv[1]) as cmd_file:
    commands = cmd_file.readlines()

with open(sys.argv[2]) as dev_file:
     devices = json.load(dev_file)

for device in devices:
    device['username'] = username
    device['password'] = password
    try:
        print('~' * 79)
        print('Connecting to device:', device['ip'])
        connection = netmiko.ConnectHandler(**device)
        newdir = connection.base_prompt
        try:
            os.mkdir(newdir)
        except OSError as error:
            # FileExistsError is error # 17
            if error.errno == 17:
                print('Directory', newdir, 'already exists.')
            else:
                # re-raise the exception if some other error occurred.
                raise
        for command in commands:
            filename = command.rstrip().replace(' ', '_') + '.txt'
            filename = os.path.join(newdir, filename)
            with open(filename, 'w') as out_file:
                out_file.write(connection.send_command(command) + '\n')
        connection.disconnect()
    except netmiko_exceptions as error:
        print('Failed to ', device['ip'], error)
