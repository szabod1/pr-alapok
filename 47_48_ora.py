# Eljárás parameter nélkül
'''
def asd():
    print('Valami')


asd()    
'''

# Eljaras 1 parameter
'''
def koszont_nevvel(nev):
        print('Szia '+ nev +', üdv a fedélzeten!')

koszont_nevvel('Ádám')
'''
# Eljaras 2 parameter
'''
def koszont_ket_nevvel(nev1, nev2):
        print('Szia '+ nev1 + ', ' + nev2 +'!\nÜdv a fedélzeten!')

koszont_ket_nevvel('Nóra', 'Ádám')
'''



#Az argumentum (aktuális paraméter) lehet érték, kifejezés, változó is!
#Az 'x', 'y' és 'eredmeny' nevű változók LOKÁLISAK, csak az eljáráson belül érhetők el! 
'''
def osszead(x, y):
        eredmeny = x + y
        print('A két szám összege: ', eredmeny)


osszead(10, 9)
osszead(5+5, 5+4)

a = 10
b = 9
osszead(a, b)
'''


#Változók hatóköre: globális és lokális változók
'''
def kepernyore_ir():
    lokalis_valtozo = 'alma'
    print(lokalis_valtozo)
    print(globalis_valtozo)


globalis_valtozo = 'gyümölcs'
kepernyore_ir()

print(globalis_valtozo)
# a lokalis_valtozo az eljáráson KÍVŰL nem elérhető !!!
print(lokalis_valtozo) # hibát eredményez !!!
'''

#A függvény értéket állít elő
'''
def udvozles():
    return "Üdv 10.C!"

print(udvozles())    
'''
'''
udvozles_szovege = "Üdvözlet 10.c"

def udvozles(udv_szov):
    return udv_szov

print(udvozles(udvozles_szovege))    
'''