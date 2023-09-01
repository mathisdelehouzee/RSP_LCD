#!/usr/bin/python

import lcddriver
import time
import socket
import datetime

display = lcddriver.lcd()

def get_ip_address():
 ip_address = '';
 s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
 s.connect(("8.8.8.8",80))
 ip_address = s.getsockname()[0]
 s.close()
 return ip_address

print"IP adres = ",(get_ip_address())

display.lcd_display_string("Actueel IP adres:", 1)
display.lcd_display_string(get_ip_address(), 2)

time.sleep(10)

display.lcd_clear()
display.lcd_display_string("  Raspberry Pi", 1)
while True:
#    display.lcd_display_string(str(datetime.datetime.now().time()), 2)
    display.lcd_display_string(str(datetime.datetime.now()), 2)


