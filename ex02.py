#2 - Escreva um algoritmo que permita a leitura das notas de uma turma de 20 alunos. 
#Calcular a média da turma e contar quantos alunos obtiveram nota acima desta média calculada. 
#Escrever a média da turma e o resultado da contagem.
lista_alunos = []
num_alunos = int(input("Digite o número de alunos: "))
nota = []
for n in range(num_alunos):
    dado_aluno = {}
    dado_aluno ['aluno'] = str.capitalize(input(f"Digite o nume do Aluno n°{(n+1)}:"))
    dado_aluno ['nota'] = float(input(f"Digite a nota de {dado_aluno['aluno']}: "))
    lista_alunos.append(dado_aluno)
    nota.append(dado_aluno ['nota'])
print("\nDados dos alunos:")
for dado_aluno in lista_alunos: 
    print(f"Aluno(a): {dado_aluno['aluno']}, Nota: {dado_aluno['nota']:.2f}")

soma = sum(nota)
mdsala = (soma/len(nota))
acimamd = 0
print (f"\nA média da turma com {num_alunos} aluno(s) foi de {mdsala:.2f}")

for dado_aluno in lista_alunos: 
    if dado_aluno ['nota'] > mdsala:
        print(f"Aluno(a): {dado_aluno['aluno']}, Nota: {dado_aluno['nota']:.2f}")
        acimamd += 1
if acimamd == 0:
    print("\nNenhum aluno ficou acima da média")
elif acimamd == 1:
    print("\nApenas 1 aluno ficou acima da média da turma:")
else:
    print(f"\nTotalizando {acimamd} alunos(s): ")

print("\nFim do cadastro de notas.")
