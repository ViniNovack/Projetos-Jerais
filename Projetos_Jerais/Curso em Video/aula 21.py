# EXEMPLO 1
# def função():
#     global n1
#     n1 = 4
#     print(f'N1 dentro vale {n1}')


# n1 = 2
# função()
# print(f'N1 fora vale {n1}')

# EXEMPLO 2
# def somar(a=0, b=0, c=0):
#     s = a + b + c
#     return s

# r1 = somar(3, 2, 5)
# r2 = somar(1, 7)
# r3 = somar(4)
# print(f'Meus cálculos deram {r1}, {r2} e {r3}!')

# EXEMPLO 3
# def fatorial(num = 1):
#     f = 1
#     for c in range(num, 0, -1):
#         f *= c
#     return f


# x = int(input('Digite um número para calcular seu fatorial: \n'))
# print(f'{fatorial(x)}')

# EXEMPLO 4
# def par(n=0):
#     if n % 2 == 0:
#         return True
#     else:
#         return False


# num = int(input('Digite um número: \n'))
# if par(num):
#     print('É PAR!')
# else:
#     print('É IMPAR!')

# EXERCICIO 101                                              !!!!!!!!!!!!!!!!!!!!!!!!!!!!(VER RESOLUÇÃO DO EXERCICIO)!!!!!!!!!!!!!!!!!!!!!!
# import datetime
# def voto(ano):
#     atual = datetime.date.today().year
#     idade = atual - ano
#     if idade < 16:
#         return f'Com {idade} anos: NÃO VOTA.'
#     elif 16 <= idade < 18 or idade > 65:
#         return f'Com {idade} anos: VOTO OPCIONAL.'
#     else:
#         return f'Com {idade} anos: VOTO OBRIGATÓRIO.'


# while True:
#     nasc = int(input('Em que ano você nasceu? (ou digite 0 para SAIR)\n'))
#     if nasc == 0:
#         break
#     else:
#         print(voto(nasc))

# print('=-'*30)
# print('FIM')

# EXERCICIO 102
