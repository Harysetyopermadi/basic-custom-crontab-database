import time
import os

try:
    os.remove('readme3.txt')
except:
    pass
time.sleep(5)

a=1
for h in range(5):
    with open('readme3.txt', 'a') as f:
        f.write('file 3'+str(a))
    print("Angka ke file 3 = ",a)
    a=a+1
    
    time.sleep(1.5)