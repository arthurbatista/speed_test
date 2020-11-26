import os
import time
import random

servers = {
    'am': [22139, 12562, 22498, 31008, 32474],
    'sp': [36362, 16322, 36834, 30170, 20138],
    'rj': [3065, 14612, 21549, 17508],
    'mi': [22361, 35678, 14237, 5030],
    'nw': [6166, 16888, 21016, 21313],
    'be': [28622, 28715, 27322, 17137],
    'lo': [35032, 11445, 24640, 30690],
    'jp': [28910, 20976, 24333, 15047],
    'ch': [14903, 32155, 13538, 16176],
    'as': [7318, 20912, 1491, 1270]
}

while True:
    locales = list(servers.keys())
    local = random.choice(locales)
    server = random.choice(servers[local])
    os.system(f'speedtest -s {server} -f json >> result.out')
    time.sleep(5)
    os.system(f'speedtest -s {server} -f json >> result.out')
    time.sleep(5)