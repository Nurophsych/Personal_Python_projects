import random
import sys
rolling = True

def D20(dno):
        
        d20list = []
        for i in range (1, dno+1):
            d20 = random.randint(1,20)
            d20list.append(d20)
        for x in d20list:
            print(x)
        d20total = sum(d20list)
        print("Total = %s" % d20total)

def D6(dno):
        
        d6list = []
        for i in range (1, dno+1):
            d6 = random.randint(1,6)
            d6list.append(d6)
        for x in d6list:
            print(x)
        d6total = sum(d6list)
        print("Total = %s" % d6total)

def D4(dno):
        
        d4list = []
        for i in range (1, dno+1):
            d4 = random.randint(1,4)
            d4list.append(d4)
        for x in d4list:
            print(x)
        d4total = sum(d4list)
        print("Total = %s" % d4total)

def D12(dno):
        
        d12list = []
        for i in range (1, dno+1):
            d12 = random.randint(1,12)
            d12list.append(d12)
        for x in d12list:
            print(x)
        d12total = sum(d12list)
        print("Total = %s" % d12total)

def D8(dno):
        
        d8list = []
        for i in range (1, dno+1):
            d8 = random.randint(1,8)
            d8list.append(d8)
        for x in d8list:
            print(x)
        d8total = sum(d8list)
        print("Total = %s" % d8total)

def D10(dno):
        
        d10list = []
        for i in range (1, dno+1):
            d10 = random.randint(1,10)
            d10list.append(d10)
        for x in d10list:
            print(x)
        d10total = sum(d10list)
        print("Total = %s" % d10total)

def D100(dno):
        
        d8list = []
        for i in range (1, dno+1):
            d100 = random.randint(1,100)
            d100list.append(d100)
        for x in d100list:
            print(x)
        d100total = sum(d100list)
        print("Total = %s" % d100total)

print("welcome to DND dice roller")
while True:

    start = input("what dice would you like to roll?")
    if len(start) == 4:
            d = start[2] + start[3]
    elif len(start) ==3:
            d =start[2]
    
    dno = int(start[0])


    
        

    if d == '20':
            D20(dno)
    elif d == '6':
            D6(dno)
    elif d == '4':
            D4(dno)
    elif d == '12':
            D12(dno)
    elif d == '8' or d == '8':
            D8(dno)
    elif d == '10' or d == '10':
            D10(dno)
    





