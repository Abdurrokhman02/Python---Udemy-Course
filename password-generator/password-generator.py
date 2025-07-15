import string
import random
from csv import writer

def passgen():
    s1 = string.ascii_lowercase    
    s2 = string.ascii_uppercase    
    s3 = string.digits
    s4 = string.punctuation    
    platform = input("Masukkan nama platform: \n")
    passlen = int(input("Masukkan panjang password: \n"))
    s = []
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))
    random.shuffle(s)
    password = ''.join(s[:passlen])
    print(password)
    passdata = [platform, password]
    with open('pass.csv', 'a') as f:
        writedata = writer(f)
        writedata.writerow(passdata)
    
passgen()