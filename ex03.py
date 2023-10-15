#3 - Ler um vetor Q de 20 posições (aceitar somente números positivos). Escrever a seguir:
#a) o valor do maior elemento de Q e a respectiva posição que ele ocupa no vetor;
#b) o valor do menor elemento de Q e a respectiva posição que ele ocupa no vetor;

def ler_numero_positivo():
    while True:
        try:
            numero = int(input("Digite um número positivo: "))
            if numero > 0:
                return numero
            else:
                print("Por favor, digite um número positivo.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número válido.")

Q = [0] * 20

for i in range(20):
    Q[i] = ler_numero_positivo()
print (Q)

maior_elemento = max(Q)
posicao_maior_elemento = Q.index(maior_elemento)

menor_elemento = min(Q)
posicao_menor_elemento = Q.index(menor_elemento)

print(f'\n A matriz contém {len(Q)} vetores.')
print(f'\nMaior elemento da matriz Q: {maior_elemento}, na posição: {posicao_maior_elemento+1}')
print(f'\nMenor elemento da matriz Q: {menor_elemento}, na posição: {posicao_menor_elemento+1}')
