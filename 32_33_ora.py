#1.1 Feladat
'''
x = input("Kérek egy szót:")

print(x.upper())
'''
#------------------------------

#1.2 Feladat
'''
lista_szoveg1 = ["és,alam,szo"]
lista_szoveg2 = []

for szo in lista_szoveg1:
    szo = lista_szoveg2.append(szo.upper())

print(lista_szoveg1,lista_szoveg2)    
'''
#----------------------------------------

#1.3 Feladat
'''
lista = ['és', 'alma', 'szo',]

nagy_lista = [szo.upper() for szo in lista if len(szo) > 3]

print (lista)
print(nagy_lista)    
'''   
#--------------------------------------------

#1.4 Feladat
'''
lista = ['és', 'alma', 'szo']

más_lista = [szo.swapcase() for szo in lista]

print(lista)
print(más_lista)
'''
#--------------------------------------------

#2.1 Feladat
'''
tartomany = list(range(-3, 5))

ertek = [2 * x - 3 for x in tartomany]

print('Tartomány:',tartomany)
print('Érték:', ertek)
'''
#----------------------------------------

#2.2 Feladat
'''
tartomany = list(range(-3, 5))

ertek = [2 * x - 3 for x in tartomany if x >= 0]

print('Tartomány:', tartomany)
print('Érték:', ertek)
'''


 
