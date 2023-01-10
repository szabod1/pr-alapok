'''
nev = input('Adja meg a kersztnevét:')
kor = int(input('Adja meg a életkorát:'))
if kor <= 1:
    print('Csecsemő')
elif kor <= 6 and kor >= 1:
    print('Kisgyerek')  
elif kor <= 12 and kor > 6:
    print('Gyerek')  
elif kor <= 16 and kor > 12:
    print('Serdülő') 
elif kor <= 25 and kor > 16:
    print('Ifjú')
elif kor <= 65 and kor > 25:
    print('Felnőtt')
elif kor >= 65:
    print('Nyugdíjas')   
'''
#-------------------------------------------------------------------

t = [7, 8, 6, 2, 15, 1, 13, 5, 9, 11, 12, 3, 4]
print(t)
lista_hossza=len(t)
print(f"A lista hossza: {lista_hossza}")
for i in range(lista_hossza-1,0,-1):
    for j in range(0,i):
        if t[j] > t[j+1]:
            tmp= t[j+1]
            t[j+1]= t[j]
            t[j]= tmp
    print(f"{t} i = {i} j = {j}")        

   