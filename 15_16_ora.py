'''
print('Hello')
print('Hello')
'''
#-----------------------------------------
'''
a = 'hello'

print(a)
'''
#-----------------------------------------
'''
a = 'Valahol voltunk tegnap este.' 

print(a)
'''
#-----------------------------------------
'''
a = 'Hello World'

print(a[1])

print(a[4])
'''
#-----------------------------------------
'''
for x in "banana":

  print(x)

for x in "banana":

  print(x,end='')
'''
#-------------------------------------------
'''
a = "Hello, World!"

print(len(a))
print(a[len(a)-1])
print('Az utolsó index: ',len(a)-1)
'''
#------------------------------------------
'''
txt = "The best things in life are free!"

print("free" in txt)  # True
'''
#-----------------------------------------
'''
txt = "The best things in life are free!"

if "free" in txt:

  print("Yes, 'free' is present.")
'''
#----------------------------------------
'''
txt = "The best things in life are free!"

print("expensive" not in txt)
'''
#------------------------------------------
'''
txt = "The best things in life are free!"

if "expensive" not in txt:

  print("No, 'expensive' is NOT present.")
'''
#------------------------------------------
'''
b = "Hello, World!"

print(b[2:5])  # llo
'''
#---------------------------------------------
'''
b = "Hello, World!"

print(b[:5])  # Hello
'''
#---------------------------------------------

a = 'Hello World!'

szamlalo = 1
for x in a:
    if szamlalo % 2 == 0:
        print(a[szamlalo-1], end='')
    szamlalo = szamlalo + 1    