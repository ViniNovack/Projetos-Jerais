#EXEMPLOS
# for c in range(1, 11):
#     print(c)
# print('Fim')
            #OR
# c = 1
# while c < 11:
#     print(c)
#     c +=1
# print('Fim')
#__________________________________________________________________________________________________________
# r = 'S'
# while r == 'S':
#     n = int(input('Digite um valor: \n'))
#     r = str(input('Quer continuar? [S/N] ')).upper()
# print('FIM')

#EXERCICIO 58
# import random
# x = 0
# while True:
#     n = random.randrange(1, 10)
#     p = int(input('Digite um numero entre 1 e 10: \n'))
#     if n == p:
#         break
#     else:
#         print(f'Voce erou a letra coreta era {n}')
#         x +=1
#
# print(f'PARABENS!!!!, Voce acertou a letra coreta era {n}, mas voce preciso de {x} tentativas')

#EXERCICIO 60
# while True:
#     z = 1
#     x = 1
#     n = int(input('Digite o numero que voce quer seu fatorial (Ou escreva 0 para encerar): \n'))
#     if n == 0:
#         break
#     else:
#         while x <= n:
#             z = z * x
#             x +=1
#         print(f'O fatorial de {n} é {z}')
# print('FIM')

#EXERCICIO 63
# L = []
# while True:
#     numero = int(input('Digite a quantidade de numeros de Sequencia de Fibonacci que voce deseja (Escreva 0 para sair): \n'))
#     if numero == 0:
#         break
#     else:
#         x = 3
#         v = 0
#         y = 0
#         z = 1
#         L.append(y)
#         L.append(z)
#         while x <= numero:
#             v = y + z
#             L.append(v)
#             y = z
#             z = v
#             x +=1
#         print(L)
# print('FIM')

#EXERCICIO 65
# M = 0
# W = 0
# x = 0
# s = 0
# while True:
#     n = int(input('Digite um numero (Ou digite 0 para SAIR): \n'))
#     if n == 0:
#         break
#     else:
#         s = s + n
#         x +=1
#         if x == 1:
#             M = n
#             W = n
#         else:
#             if n > M:
#                 M = n
#             if n < W:
#                 W = n
# m = s / x
# print(f'Voce digitou {x} numeros, portanto a média dos valores é {m}, sendo o maior numero {M} e o menor numero {W}')