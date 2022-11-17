# network usage per process

from scapy.all import *
import psutil
from collections import defaultdict
import os
from threading import Thread
import pandas as pd

# get the all network adapter's MAC addresses
all_macs = {iface.mac for iface in ifaces.values()}
print(all_macs)
# a dictionary to map each connection to its corresponding process ID (PID)
connection2pid = {}
# a dictionary to map each process ID (PID) to total upload (0) and download (1) traffic
pid2traffic = defaultdict(lambda: [0,0])
print(pid2traffic)
# the global pandas dataframe that's used to track previous traffic stats
global_df = None
# global boolean for status of the program
is_program_running = True

# function with body - function declaration
#function with body - function definition
#function abstraction - declare the func + func [complete/partial] body/defn - implementor

def get_size(bytes):
    """
    Returns size of bytes in a nice format
    """
    for unit in ['', 'K', 'M', 'G', 'T', 'P']:
        if bytes<1024:
            return f"{bytes:.2f}{unit}B"
            bytes /= 1024

