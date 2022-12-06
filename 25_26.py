'''
lista = ["alma","banán","cseresznye"]
print(lista)
'''
#---------------------------------------------
'''
lista = ["alma","banán","cseresznye","alma","banán"]
print(lista)
'''
#----------------------------------------------------
'''
lista = ["alma","banán","cseresznye"]
print(len(lista))
'''
#------------------------------------------------
'''
lista1 = ["alma","banán","cseresznye"]
lista2 = [1,5,7,9,3]
lista3 = [True,False,False]
'''
#--------------------------------------------------
'''
lista1 = ["abc", 34, True, 40, "férfi"]
print(lista1)
'''
#------------------------------------
'''
lista5 = ["alma", "banan", "cseresznye"]
print(type(lista5))
'''
#---------------------------------------
'''
lista = list(("alma", "banan", "cseresznye"))
print(lista)
'''
#----------------------------------------
'''
lista = ["alma","banán","cseresznye"]
print(lista[1])
'''
#--------------------------------------
'''
lista = ["alma-0", "banan-1", "cseresznye-2", "narancs-3", "kivi-4", "szőlő-5", "mangó-6"]
print(lista[1:6])
'''
#------------------------------------------
'''
lista = ["alma-0", "banan-1", "cseresznye-2", "narancs-3", "kivi-4", "szőlő-5", "mangó-6"]
print(lista[-4:])
'''
#-------------------------------------------
'''
lista = ["alma-0", "banan-1", "cseresznye-2", "narancs-3", "kivi-4", "szőlő-5", "mangó-6"]
if "banan" not in lista:
  print('A banán nincs a listába van')
'''
#-----------------------------------------
'''
lista = ["alma","banán","cseresznye"]
lista[1] = "kivi"
print(lista)
'''
#-------------------------------
'''
lista = ["alma-0", "banan-1", "cseresznye-2", "narancs-3", "kivi-4", "szőlő-5", "mangó-6"]
lista[1:3] = ["körte", "szilva"]
print(lista)
'''
#----------------------------------
'''
lista = ["alma-0", "banan-1", "cseresznye-2", "narancs-3", "kivi-4", "szőlő-5", "mangó-6"]
lista.insert(2, "körte")
print(lista)
'''
#---------------------------------

lista = ["alma","banán","cseresznye"]
lista.append("körte")
print(lista)