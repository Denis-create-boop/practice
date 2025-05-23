import time, os

an = ('|', '/', '-', '\\')
i = 0

while True:
    print('wait...', an[i], sep='', end='\r')
    time.sleep(0.1)
    i += 1
    if i is len(an):
        i = 0
    
