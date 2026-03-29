#EXEMPLO 1
# dados = {}
# dados = {'nome': 'Pedro', 'idade': 25}
# dados ['sexo'] = 'M'
# print(dados['sexo'])

#EXEMPLO 2
# filme = {'titulo': 'star wars', 'ano': 1977, 'diretor': 'George Lucas'}
# print(filme.values())
# print(filme.keys())
# print(filme.items())
# for k, v in filme.items():
#     print(f'O {k} é {v}')

#EXEMPLO 3
# filme1 = {'titulo': 'star wars', 'ano': '1977', 'diretor': 'George Lucas'}
# filme2 = {'titulo': 'avengers', 'ano': '2012', 'diretor': 'Joss Whedon'}
# filme3 = {'titulo': 'matrix', 'ano': '1999', 'diretor': 'Wachowski'}
# locadora = [filme1, filme2, filme3]
# print(locadora[0]['titulo'])

#EXEMPLO 4
# brasil = []
# estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
# estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
# brasil.append(estado1)
# brasil.append(estado2)
# print(brasil[0]['uf'])
# print(brasil[1]['uf'])

#EXEMPLO 5
# estado = {}
# brasil = []
# for c in range(0, 3):
#     estado['uf'] = str(input('Unidade Federativa: \n'))
#     estado['sigla'] = str(input('Sigla do Estado: \n'))
#     brasil.append(estado.copy())
# for e in brasil:
#     for v in e.values():
#         print(v, end=' ')
#     print()

#___________________________________________________________________________________________________________________________________________________________
#EXERCICIO 1
