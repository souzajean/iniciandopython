#Version: Python 3.6 -> data:24/09/2018


# coding: utf-8

estadio = "itaquerao"

print(estadio[0])
print(estadio[1])
print(estadio[2])
print(estadio[3])
print(estadio[4])
print(estadio[5])
print(estadio[6])
print(estadio[7])
print(estadio[8])

print()

print(estadio[1:4])
print(estadio[2:4])
print(estadio[3:6])

print()

print(estadio[:5])
print(estadio[2:9])
print(estadio[3:6])

print()

print(len(estadio))

print()

#Operadores

# x in y
# x not in y
# x + t
# x * y

print("a" in "itaquerao")
print("b" in "itaquerao")
print("a" not in "itaquerao")
print("b" not in "itaquerao")
print("i" + "taquerao")
print("a" * 3)
print("b" * 2)

#Imutabilidade: novas strings criadas a partir de outras string


minha_str = "Livro Python 3"
minha_str = minha_str[0:13] + "2"
print(minha_str)

minha_str = "Livro Python 3"
minha_str = minha_str.replace("3" , "2")
print(minha_str)



