
from htdp_pt_br.list import *


x1 = VAZIA

x2 = criar_lista(3,5,6,9)

x3 = criar_lista(2,7,1)

print(x1)

print(x2)

print(x2.reverte())

print(x2.primeiro)

print(x2.resto)

print(x2.concat(x3))

print(x1.concat(x2))
print(x1.concat(x3))

print(x1.reverte())

#funcoes
print(reverte(x2))

print(primeiro(x2))

print(resto(x2))

print(concat(x2,x3))

print(concat(x1, x2))
print(concat(x1,x3))

print(reverte(x1))

