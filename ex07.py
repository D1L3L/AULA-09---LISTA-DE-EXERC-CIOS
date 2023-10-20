#Faça um algoritmo para ler dois vetores V1 e V2 de 10 números cada.
#Calcular e escrever a quantidade de vezes que V1 e V2 possuem os mesmos 
#números e nas mesmas posições.

from random import randint

# Cria dois vetores V1 e V2 de 10 números aleatórios cada
V1 = [randint(0, 10) for i in range(10)]
V2 = [randint(0, 10) for i in range(10)]

# Calcula a quantidade de vezes que V1 e V2 possuem os mesmos números e nas mesmas posições
count = 0
print (f" V1 = {V1} \n V2 = {V2}")
contagemv1 = len(V1)
contagemv2 = len(V2) 
maior = contagemv2
if contagemv1 >= contagemv2:
    maior = contagemv1
else:
    maior = contagemv2
for i in range(maior):
    if V1[i] == V2[i]:
        count += 1

# Escreve a quantidade de vezes que V1 e V2 possuem os mesmos números e nas mesmas posições
print(count)