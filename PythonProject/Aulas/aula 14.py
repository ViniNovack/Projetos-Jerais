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

#EXERCICIO