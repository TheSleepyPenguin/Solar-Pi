#!/bin/bash
cd "/usr/local/bin/Solar Pi/Power"
./ramdisk_setup.sh
python3 "Power Daemon.py" &