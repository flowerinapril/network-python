#! /usr/bin/env python3
# coding: utf-8
from multiprocessing import cpu_count
import subprocess
subprocess.call(["pwd"])
subprocess.call(["ls","-l","/"])
num_cores = cpu_count()
print("your computer has %d cores" % num_cores)