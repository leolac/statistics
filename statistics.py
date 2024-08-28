import statistics

def moda(notas):
    print('Moda:' + str(statistics.mode(notas)))

def media(notas):
    print('Média: '+ str(statistics.mean(notas)))

def variancia(notas):
    print('Variância: ' + str(statistics.variance(notas)))

def desviopadrao(notas):
    print('Desvio padrão: ' + str(statistics.stdev(notas)))

def maiornota(notas):
    print('Maior nota: ' + str(max(notas)))

def menornota(notas):
    print('Menor nota: ' + str(min(notas)))

notas = []
for x in range(10):
    notas.append(int(input('Digite a próxima nota do aluno de 10. ')))

moda(notas)
media(notas)
variancia(notas)
desviopadrao(notas)
maiornota(notas)
menornota(notas)
