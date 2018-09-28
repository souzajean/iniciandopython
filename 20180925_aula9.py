#Version: Python 3.6 -> data:25/09/2018


# coding: utf-8

#Impressão de documento

print()
#"%d dias do ano" % (365)
print("%d dias do ano" % (365))
print()

#"{} dias tem o ano".format(365)
print("{} dias tem o ano".format(365))
print()

#"{dias} dias para copa".format(dias=100)
print("{meses} meses no ano".format(meses=12))
print()

#Podemos configurar espaçamentos e alinhamentos, da seguinte forma:

#'{:<60}'.format('alinhado à esquerda, ocupando 60 posições')
print('{:<60}'.format('alinhado à direita, ocupando 60 posições'))
print()

#'{:>60}'.format('alinhado à direita, ocupando 60 posições')
print('{:>60}'.format('alinhado à direita, ocupando 60 posições'))
print()

#'{:^60}'.format('centralizado, ocupando 60 posições')
print('{:^60}'.format('centralizado, ocupando 60 posições'))
print()

#'{:.^60}'.format('centralizando ao alterar caractere')
print('{:.^60}'.format('centralizando ao alterar caractere'))