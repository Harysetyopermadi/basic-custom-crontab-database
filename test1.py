import time
import os

try:
    os.remove('readme1.txt')
except:
    pass
time.sleep(5)
a=1
for h in range(5):
    with open('readme1.txt', 'a') as f:
        f.write('file 1'+str(a))
    print("Angka ke file 1 = ",a)
    a=a+1
    
    time.sleep(1)