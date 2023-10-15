#4 - Ler um vetor A de 10 números. Após, ler mais um número e guardar em uma variável X. Armazenar em um vetor M o resultado de cada elemento de A multiplicado pelo valor X.
# Logo após, imprimir o vetor M.

def ler_numero():
    while True:
        try:
            numero = int(input("Digite um número: "))
            if numero >= 0:
                return numero
            elif numero < 0:
                return numero
        except ValueError:
            print("Entrada inválida. Por favor, digite um número válido.")
            
n = int(input("Digite o número de vetores na matriz: "))             
matriz_a = [0] * n
matriz_m = [0] * n
multiplicador = int(input("\nDigite um número para multiplicar a matriz: "))

for vetor in range (n):
    matriz_a[vetor] = ler_numero()
print(matriz_a)

for mult in range (n):
    matriz_m[mult] = ((matriz_a[mult]) * multiplicador)
print(matriz_m)
