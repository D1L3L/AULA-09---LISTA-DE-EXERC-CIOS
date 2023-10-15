#5 - Crie um vetor N que seja resultado da soma dos itens de outros dois vetores A e B. Exemplo: A[0] + B[0] deverá ser salva em N[0].

vetor_a = int(input("digite o valor do vetor A: "))
vetor_b = int(input("digite o valor do vetor B: "))
vetor_n = [vetor_a + vetor_b]
print (f"A soma dos vetores [{vetor_a}] + [{vetor_b}] restultam no vetor N = {vetor_n}")
