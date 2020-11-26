import os
import time

wifis = ['tutuca', 'old_tutuca']
current = 0

while True:
    wifi = wifis[current]
    current = 0 if current == 1 else 1
    print(f'change wifi to {wifi}')
    os.system(f'nmcli device wifi connect {wifi}')
    time.sleep(300)