#EXEMPLO 1
# def linha(x):
#     print('=-'*x)

# linha(30)
# print('Olá, mundo!!!')
# linha(20)

#EXEMPLO 2
# def globo(x, y):
#     print('=-'*x)
#     print(y)
#     print('=-'*x)
 

# v = str(input('Escreva uma frse: \n'))
# globo(30, v)

#EXEMPLO 3
# def soma(a, b):
#     s = a + b
#     print(s)


# soma(4, 5) #OU soma(a = 4, b = 5) OU Também posso trocar a ordem: soma(b = 4, a= 5)
# soma(8, 9)
# soma(2, 1)

#EXEMPLO 4
# def contador(*num):
#     l = len(num)
#     print(num, f'Tem {l} elementos')


# contador(2, 1, 7)
# contador(9, 5, 1)

#EXEMPLO 5

#TERMINAR DE VER ESSA PARTE DA AULA

def dobra(lst):
    for n in lst:
        x = lst.index(n)
        lst[x] = n * 2

L = [1, 2, 3, 4, 5]
dobra(L)
print(L)
