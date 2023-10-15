#6 - Faça um algoritmo para ler um vetor de 20 números. Após isto, deverá ser lido mais um número qualquer 
# e verificar se esse número existe no vetor ou não. 
# Se existir, o algoritmo deve gerar um novo vetor sem esse número. (Considere que não haverão números repetidos no vetor).
from random import _inst
def ler_numero():
    while True:
        try:
            numero = int(input("Digite um vetor para a matriz: "))
            if numero >= 0:
                return numero
            elif numero < 0:
                return numero
        except ValueError:
            print("Entrada inválida. Por favor, digite um número válido.")
vetor = [0] * 20
for i in range(20):
    vetor[i] = ler_numero()
print (vetor)
