#!/usr/bin/python
# -*- coding: latin-1 -*-
#
# © 2018 Microchip Technology Inc. and its subsidiaries.
#
# Subject to your compliance with these terms, you may use Microchip software
# and any derivatives exclusively with Microchip products. It is your
# responsibility to comply with third party license terms applicable to your
# use of third party software (including open source software) that may
# accompany Microchip software.
#
# THIS SOFTWARE IS SUPPLIED BY MICROCHIP "AS IS".  NO WARRANTIES, WHETHER
# EXPRESS, IMPLIED OR STATUTORY, APPLY TO THIS SOFTWARE, INCLUDING ANY
# IMPLIED WARRANTIES OF NON-INFRINGEMENT, MERCHANTABILITY, AND FITNESS FOR A
# PARTICULAR PURPOSE. IN NO EVENT WILL MICROCHIP BE LIABLE FOR ANY INDIRECT,
# SPECIAL, PUNITIVE, INCIDENTAL OR CONSEQUENTIAL LOSS, DAMAGE, COST OR
# EXPENSE OF ANY KIND WHATSOEVER RELATED TO THE SOFTWARE, HOWEVER CAUSED,
# EVEN IF MICROCHIP HAS BEEN ADVISED OF THE POSSIBILITY OR THE DAMAGES ARE
# FORESEEABLE. TO THE FULLEST EXTENT ALLOWED BY LAW, MICROCHIP'S TOTAL
# LIABILITY ON ALL CLAIMS IN ANY WAY RELATED TO THIS SOFTWARE WILL NOT EXCEED
# THE AMOUNT OF FEES, IF ANY, THAT YOU HAVE PAID DIRECTLY TO MICROCHIP FOR
# THIS SOFTWARE.

# Serial bootloader script for Microchip tinyAVR 0-, 1-series and megaAVR 0-series MCUs
#
# Futurized to support python 2 and 3.
# Download Python from https://www.python.org/downloads/ 
#
from __future__ import print_function
try:
	import sys
	from builtins import bytes, int
	import argparse
	import struct 
	import os
	import binascii
	import base64
	import getopt
	from serial import Serial
	from intelhex import IntelHex
except ImportError:
    sys.exit("""ImportError: You are probably missing some modules.
To add needed modules, run 'python -m pip install -U future pyserial intelhex'""")

def ByteToHex( byteStr ):
     return ''.join( [ "%02X " % ord( x ) for x in byteStr ] )

# Generate help and use messages 
parser = argparse.ArgumentParser(
description='Serial bootloader script for Microchip AVR-DA family MCUs',
epilog='Example: AVR-DA_uploader.py ./App/Release/App.hex 0x20000 COM5 9600',
formatter_class=argparse.RawTextHelpFormatter)
parser.add_argument('file', help='Hex file to upload')
parser.add_argument('flashsize', help='Total device flash size')
parser.add_argument('comport', help='UART COM port')
parser.add_argument('baudrate', help='UART baud rate')

if len(sys.argv)==1:
    parser.print_help()
    sys.exit(1)
args = parser.parse_args()

# Command line arguments
file = sys.argv[1]
flashsize = int(sys.argv[2], 0)
comport = sys.argv[3]
baudrate = int(sys.argv[4], 0)

# The versions are not relevant at this moment, so hard-coded values are used
# They will be used in a future implementation
VersionMax = 1
VersionMin = 0

import add_image_info
add_image_info.addInfo(file,flashsize,VersionMax,VersionMin)

# Init serial communication
uart = Serial(comport, baudrate=baudrate, timeout=1)
print("\n",uart)
uart.reset_input_buffer()

bin_file = os.path.splitext(file)[0] + "_w_info.bin"

size = os.path.getsize(bin_file);

app = open(bin_file, 'rb+')
failed = 0
counter = 0

print ("\n","Uploading", size, "bytes...")

#send firmware  bin file
with open(bin_file, "rb") as f:
	while counter<size:
		# Do stuff with byte.
		byte = f.read(1)
		uart.write(byte)
		tmp_byte = uart.read(1)
		if (tmp_byte != byte):
			failed = 1
			break
		counter += 1
		print ("\r%.02f%%" % (float(counter)/size*100), end='')

f.close()

# Check reason for exiting loop and print debug info
if failed:
	print ("\nFailed at address %#06x" % (counter))
	tmp_byte = int.from_bytes(tmp_byte, byteorder="little")
	byte = int.from_bytes(byte, byteorder="little")
	print ("Value %#04x echoed, expected %#04x" % (tmp_byte, byte))
	sys.exit(0)
else:
    print ("\nFirmware upload OK")

sys.exit(1);

# Send application to device. Each byte is is echoed for validation.
for byte in app:
    byte = bytes([byte])
    uart.write(byte)
    tmp_byte = uart.read(1)
    if (tmp_byte != byte):
        failed = 1
        break
    counter += 1
    print ("\r%.02f%%" % (float(counter)/size*100), end='')

# Device will reset and jump to application when flash is successfully programmed,
# or it can be externally reset or power-cycled.