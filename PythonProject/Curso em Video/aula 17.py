#EXEMPLO 1
# num = [2, 5, 9, 1]
# num[2] = 3
# num +=[7]
# num.sort(reverse = True)
# print(num)

#EXEMPLO 2
# valores = []
# valores += [5]
# valores += [9]
# valores.append(4)
# for c, v in enumerate(valores):
#     print(f'Na posição {c + 1} encontrei o valor {v}!')
# print('Cheguei ao final !')

#EXERCICIO 78
# x = 0
# lista = str(input('Digite numeros separados por virgula(,): \n'))
# L = lista.split(',')
# M = int(L[0])
# m = int(L[0])
# while x <= len(L) - 1:
#     z = int(L[x])
#     if z > M:
#         M = z
#         x +=1
#     else:
#         x +=1
# x = 0
# while x <= len(L) - 1:
#     t = int(L[x])
#     if t < m:
#         m = t
#         x +=1
#     else:
#         x +=1
# M = str(M)
# m = str(m)
# print(f'O MAIOR valor é {M} que esta na posição {L.index(M) + 1}')
# print(f'O MENOR valor é {m} que esta na posição {L.index(m) + 1}')
