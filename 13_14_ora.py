'''
szam1 = int(input('Kérek egy egész számot:'))
szam2 = int(input('Kérek egy másik számot:'))
if szam1 >szam2:
    print('Szám1 nagyobb mint szám2')

if szam2 > szam1:
    print('Szám2 nagyobb mint szam1')

if szam1 == szam2:
    print('Szam1 egyenlő szam2-vel')    
'''
#--------------------------------------------------------
'''
szam1 = int(input('Kérek egy egész számot:'))
szam2 = int(input('Kérek egy másik számot:'))
if szam1 > szam2:
    print('Szám1 nagyobb mint szám2')
elif szam2 > szam1:
    print('Szám2 nagyobb mint szam1')
else:
    print('Szam1 egyenlő szam2-vel')  
'''
#------------------------------------------------------------

'''
x = None
print(x)
print(type(x))

if x:
    print("Do you think none is True?")
elif x is False:
    print('Do you think None is False?')
else:
    print('None is not True, or False, None is just None...')   
'''

#----------------------------------------------------------------------
''''
# Bekérek egy osztályzatot

jegy = input('Kérek egy osztályzatot:')
if jegy == '1':
    print('elégtelen')
elif jegy == '2':
    print('elégséges')
elif jegy == '3':
    print('közepes')
elif jegy == '4':
    print('jó')
elif jegy == '5':
    print('jeles')
else:
    print('Érvénytelen osztályzatot adtál')   
'''

#-------------------------------------------------------
'''
# Bekérek egy pozitiv egész számot irasuk ki, hogy páros vagy páratlan

szam = int(input('Kérek egy pozitiv egészszámot:'))
if szam % 2 == 0:
    print('Páros')
else:
    print('Páratlan')    
'''
#----------------------------------------------------------------
'''
# Véletlen szám generátor

import random

gondolt_szam = random.randint(1,6)
print('Súgok:',gondolt_szam)
tipp = input('Gondoltam egy számra. Tippeld meg!:')
if tipp == gondolt_szam:
    print('Eltaláltad')
else:
    print('Nem jó, probáld újra')   
'''
#----------------------------------------------------------

# Generáljunk 1-1000 között egy számot és irasuk ki a számot, ha páros és kisebb mint 500 ha nem igaz azt irja ki hogy nem felelt meg a feltételeknek
from random import random


x = random.randint(1,1000)

print(x)
if x % 2 != 0 and x <= 500:
    print('A szám jó')
else:
    print('A számod nem jó.')    

