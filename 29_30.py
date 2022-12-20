'''
szam = int(input('Adjál számot 5 és 10 között:'))

while not 5 <= szam and szam <= 10 and szam % 2 == 0:
    szam = int(input('Helytelen érték! Ajdjál másikat!'))
print('Rendben!')
'''
#-----------------------------------------------------
'''
szo = None
szu = ''
while szo != '':
    szo = input('Adjon meg szavakat! Ha kilépnél, a szó helyett csak egy ENTER-t üss!')
print('Program vége!')    
'''
#-----------------------------------------------------------

szo = input('Adjon meg szavakat! Ha kilépnél, a szó helyett csak egy ENTER-t üss!')
szöveg = ""
while szo != '':
    szöveg = szöveg + szo
    print(szöveg)
    szo = input('Adjon meg szavakat! Ha kilépnél, a szó helyett csak egy ENTER-t üss!')
print('Program vége!')    