#6 - Faça um algoritmo para ler um vetor de 20 números. Após isto, deverá ser lido mais um número qualquer 
# e verificar se esse número existe no vetor ou não. 
# Se existir, o algoritmo deve gerar um novo vetor sem esse número. (Considere que não haverão números repetidos no vetor).

vetor = []

for i in range(3):
    num = int(input("Digite um valor: "))
    vetor[i] = num

num_procura = int(input("Digite o numero a procurar: "))

print("O numero",num_procura,"esta no vetor? ",num_procura in vetor)
print("Fim do Programa")

