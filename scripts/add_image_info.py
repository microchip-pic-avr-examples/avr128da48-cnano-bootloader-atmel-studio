#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# © 2019 Microchip Technology Inc. and its subsidiaries.
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

# Serial bootloader for Microchip  AVR DA series MCUs
#     - convert hex file to bin file and add information for the bootloader  
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

def addInfo(hex_file, flash_size, VMajor, Vminor):
	# Load application hex file and convert to byte array
	# The hex file must have a start address corresponding to BOOTSIZE*512
	# Array size is increased to multiples of Flash page size and is padded with 0xFF
	# Information is added at the beginning of file
	flashsize = flash_size				
	ih = IntelHex()
	fileextension = hex_file[-3:]
	ih.loadfile(hex_file, format=fileextension)
	append = ih.maxaddr()
	if (append > flashsize):
		print ("Error: Flashsize input: %#06x, " % (flashsize) +
			   "Minimum size needed: %#06x." % (append))
		sys.exit(1)
	appstart = ih.minaddr()
	print ("\n","Start Address: %#06x" % (appstart ))
	flashsize = ((append & 0xFFFFFE00) + 0x200)						# Round to multiple page number and add 0x200
  
	# Pack integers in a binary string
	start_address = struct.pack("<i", appstart) 		        	# Start address of the application image
	app_image_size = struct.pack("<i", flashsize-appstart) 			# Length of the application image
	version = (VMajor<<16)+Vminor
	app_image_version = struct.pack("<i", version) 					# Version of the application image

	start_app = ih.tobinarray(end=flashsize-1)
	bin_start_file = os.path.splitext(hex_file)[0] + ".bin"
	
	# Save original file
	fq = open(bin_start_file, 'wb')
	fq.write(start_app)
	fq.close()
	
	# Add info to file, new flashsize = flashsize + 0x200

	app = ih.tobinarray(end=flashsize-1)
	bin_file = os.path.splitext(hex_file)[0] + "_w_info.bin"

	# Save to bin file
	f = open(bin_file, 'wb')

	# Write the information section
	f.write(b"INFO")
	f.write(start_address)
	f.write(app_image_size)
	f.write(app_image_version)
	
	# Round to page size (512) and fill with 0xFF 	
	counter = 0
	while counter<112:   	# 128B(page size) - 16B(information section size)  
		counter += 1
		f.write(b"\xFF")

	f.write(b"STX0")
	f.write(app)
	
	f.close()


	

