from htdp_pt_br.list import *

'''
Lista<Int> é um desses:
- conj(Int, Lista<Int>)
- VAZIA
Lista de inteiros
Exemplos:
'''
L_VAZIA = VAZIA
L_1 = juntar(2, VAZIA)
L_2 = juntar(5, L_1)
L_3 = juntar(7, L_2)
L_10 = criar_lista(4, 7, 8, 2, 4, 9, 6, 3, 5, 3)

'''
#template
def fn_para_lista<int>(lista):
    if lista.vazia:
        ...
    else:
        ... lista.primeiro 
            fn_para_lista<int>(lista.resto)
'''

'''
dobra_todos: ListaInteiros -> ListaInteiros
'''


def dobra_todos(lista):
    if lista.vazia:
        return lista
    else:
        return juntar(lista.primeiro * 2,
                      dobra_todos(lista.resto))


assert dobra_todos(L_3) == criar_lista(14, 10, 4)
assert dobra_todos(L_10) == criar_lista(8, 14, 16, 4, 8, 18, 12, 6, 10, 6)

import operator

x = L_10.map(lambda x: x * 2)
assert x == criar_lista(8, 14, 16, 4, 8, 18, 12, 6, 10, 6)
x = criar_lista(*map(lambda x: x * 2, L_10))
assert x == criar_lista(8, 14, 16, 4, 8, 18, 12, 6, 10, 6)
x = criar_lista([x*2 for x in L_10])
assert x == criar_lista(8, 14, 16, 4, 8, 18, 12, 6, 10, 6)

##soma dos quadrados
y = L_10.map(lambda x: x**2).reduce(operator.add)
assert y == 309

assert L_10.filter(lambda x: x > 4) == criar_lista([7, 8, 9, 6, 5])

assert set(L_10) == set([2, 3, 4, 5, 6, 7, 8, 9])

assert L_10[-1] == 3
assert L_10[-3] == 3

try:
    print(L_10[-11])
except IndexError as i:
    print("ok")

assert L_10[:-2] == criar_lista([4, 7, 8, 2, 4, 9, 6, 3])

assert L_10.andmap(lambda x: x > 1) == True
assert L_10.andmap(lambda x: x > 3) == False
assert L_10.ormap(lambda x: x > 3) == True
assert L_10.ormap(lambda x: x > 9) == False

assert L_3.remove(5) == criar_lista(7, 2)

assert L_10.remove(3) == criar_lista([4, 7, 8, 2, 4, 9, 6, 5, 3])