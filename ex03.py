#3 - Ler um vetor Q de 20 posições (aceitar somente números positivos). Escrever a seguir:
#a) o valor do maior elemento de Q e a respectiva posição que ele ocupa no vetor;
#b) o valor do menor elemento de Q e a respectiva posição que ele ocupa no vetor;
from random import randint
Q = [] 
for vetor in range (20):
    Q.append(randint(0, 100))

print (f"A lista de vetores é: {Q}")

maior_elemento = max(Q)
posicao_maior_elemento = Q.index(maior_elemento)

menor_elemento = min(Q)
posicao_menor_elemento = Q.index(menor_elemento)

print(f'A matriz contém {len(Q)} vetores.')
print(f'\nMaior elemento da matriz Q: {maior_elemento}, na posição: {posicao_maior_elemento+1}')
print(f'Menor elemento da matriz Q: {menor_elemento}, na posição: {posicao_menor_elemento+1}')
