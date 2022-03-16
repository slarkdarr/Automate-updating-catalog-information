#!/usr/bin/env python3

import psutil
import socket
import emails

# Define threshold variables
max_cpu_usage_percentage = 80
max_disk_avail_percentage = 20
max_memory_avail_mb = 500
check_local_host_ip = "127.0.0.1"

# Check if CPU usage percentage exceeds max threshold
def checkCPU():
    cpu_usage_percentage = psutil.cpu_percent(interval=3)
    return cpu_usage_percentage > max_cpu_usage_percentage

# Check if disk usage percentage exceeds max threshold
def checkDisk():
    max_disk_usage_percentage = 100 - max_disk_avail_percentage
    dsk_usage_percentage = psutil.disk_usage("/").percent
    return dsk_usage_percentage > max_disk_usage_percentage

# Check if memory usage exceeds max threshold
def checkMemory():
    one_mb = 2 ** 20
    max_memory_avail = one_mb * max_memory_avail_mb
    memory_avail = psutil.virtual_memory().available
    return memory_avail < max_memory_avail

# Check if hostname "localhost" cannot be resolved
def checkConnection():
    local_host_ip = socket.gethostbyname("localhost")
    return local_host_ip != check_local_host_ip

def main():
    alert = None
    if checkCPU():
        alert = f"Error - CPU usage is over {max_cpu_usage_percentage}%"
    elif checkDisk():
        alert = f"Error - Available disk space is less than {max_disk_avail_percentage}%"
    elif checkMemory():
        alert = f"Error - Available memory is less than {max_memory_avail_mb}MB"
    elif checkConnection():
        alert = f"Error - localhost cannot be resolved to {check_local_host_ip}"
    
    if alert:
        args = {
            'sender': "automation@example.com",
            'recipient': "student-01-af05aba7d1c6@example.com",
            'subject': alert,
            'body': "Please check your system and resolve the issue as soon as possible."
        }
        message = emails.generate_email(**args)
        emails.send_email(message)

if __name__ == '__main__':
    main()
