import psutil
import os
import subprocess

def get_cpu_temp():
    temp = psutil.sensors_temperatures()['cpu_thermal'][0].current
    return temp

ip = "hostname -I"
uptime = "uptime -p"

print("CPU Temperature: ", get_cpu_temp())

# IP
result_ip = subprocess.check_output(ip, shell=True, text=True)
print("IP: ", result_ip)

# Uptime
result_uptime = subprocess.check_output(uptime, shell=True, text=True)
print("Uptime: ", result_uptime)