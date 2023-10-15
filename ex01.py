#1 - Escreva um algoritmo que permita a leitura dos nomes de 10 clubes de futebol 
#e armazene os nomes lidos em um vetor (lista). Após isto, o algoritmo deve permitir 
#a leitura de mais 1 nome qualquer de clube e depois escrever a mensagem ACHEI, 
#se o nome estiver entre os 10 nomes lidos anteriormente (guardados no vetor), ou NÃO ACHEI caso contrário.

# Lista com 10 clubes.
clubes = ["flamengo", "Palmeiras", "Santos", "São Paulo", "Corinthians", "Grêmio", "Internacional", "Fluminense", "Cruzeiro", "Atlético Mineiro"]

# Leitura do nome do clube. obs: Capitalize é para deixar as STR com iniciais maiúsculas.
nome_clube = str.capitalize(input("Digite o nome do clube: "))

# Verificação se o clube está na lista. obs: Capitalize é para deixar as STR com iniciais maiúsculas.
if nome_clube in map (str.capitalize, clubes):
    print("ACHEI")
else:
    print("NÃO ACHEI")
