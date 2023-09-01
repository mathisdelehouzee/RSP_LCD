
#!/usr/bin/python3

import lcddriver
import time
import socket

display = lcddriver.lcd()

def get_ip_address():
    ip_address = ''
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip_address = s.getsockname()[0]
    s.close()
    return ip_address

print("IP address = ", get_ip_address())

display.lcd_display_string("IP address:", 1)
display.lcd_display_string(get_ip_address(), 2)

time.sleep(2)
