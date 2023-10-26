#Faça um algoritmo para ler um vetor de 30 números. 
#Após isto, ler mais um número qu alquer, 
#calcular e escrever quantas vezes esse número aparece no vetor.

from random import randint

def repete(lista, vetor):
    count = 0
    for i in lista:
        if i == vetor:
            count += 1
    return count

lista = [randint(1, 30) for _ in range(30)]
vetor = int(input("Digite um número: "))
limite = 100000
if  limite > vetor > 0:
    print (f"Os vetores são: {lista}")
    frequencia = repete(lista, vetor)
    print(f"O número {vetor} aparece {frequencia} vezes no vetor listado acima.")

else:
    print("Valor digitado não aceito")

