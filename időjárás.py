napi_max = [14, 17, 21, 15, 16, 13, 8, 11, 12, 14, 16, 16, 14, 15, 13, 14, 16, 16, 14, 12, 12, 10, 11, 13, 15, 17, 19, 17, 19, 20,]
napi_min = [8, 8, 9, 6, 7, 1, 0, 2, 3, 5, 4, 4, 3, 5, 4, 6, 8, 6, 4, 2, 1, -1, -1, 1, 3, 5, 7, 5, 7, 9,]
#Első Feladat:
def napimindb (napi_min_fv):
    darab = 0
    for szam in napi_min_fv:
        darab = darab +1
    return darab

print(napimindb(napi_min)) 

def napimaxdb (napi_max_fv):
    darab = 0
    for szam in (napi_max_fv):
        darab = darab +1
    return darab

print(napimaxdb(napi_max))        
        
#Második Feladat:
def napimaxatlag (napi_max_fv):
    lista = 0
    for szam in napi_max_fv:
        lista = lista + szam
    lista = lista /len(napi_max_fv)
    return lista
    
print(napimaxatlag(napi_max)) 



def napiminatlag (napi_min_fv):
    lista = 0
    for szam in napi_min_fv:
        lista = lista + szam
    lista = lista /len(napi_min_fv)
    return lista
    
print(napiminatlag(napi_min))        

#Harmadik feladat:
print(f'Össz átlag: {(napimaxatlag(napi_max) + napiminatlag(napi_min)) / 2}')