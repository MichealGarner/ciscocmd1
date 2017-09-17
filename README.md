# Running Cisco commands with Python using Netmiko

This project was created to test Netmiko with Cisco Switches and Routers.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

This project is based on netmiko.
You will need a working copy of netmiko to use these files.

Installing netmiko:

Netmiko can be found on GitHub at https://github.com/ktbyers/netmiko.

You can install it from source:
```
$ git clone https://github.com/ktbyers/netmiko.git
$ cd netmiko
$ python setup.py install
```
You can also use pip:
```
$ pip install netmiko
```

### Installing

First make a local copy of the files in this repository

```
$ git clone https://github.com/MichealGarner/ciscocmd1
```

## Running the tests

Once you have a local copy of the files, you can use the script as follows:

To run the commands listed in the router_commands.txt file...

Usage:
```
python cmdrunner.py router_commands.txt routers.json
```
add the commands you want to run to the router_commands.txt file.
add the devices you want to run the commands on in the routers.json file.

To run the commands listed in the switch_commands.txt file...

Usage:
```
python cmdrunner.py switch_commands.txt switches.json
```
add the commands you want to run to the switch_commands.txt file.
add the devices you want to run the commands on in the switches.json file.

## Authors

* **Micheal Garner** - https://github.com/MichealGarner


## Acknowledgments

* This script is based entirely on the work of Greg Mueller
https://www.youtube.com/channel/UCsB_qVfDBlkejpg_y3Ltgqw
