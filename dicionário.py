#dicionário
filmes = {
    1: ["Toy Story","Animação", 1996],
    2: ["Vingadores", "Ação e Aventura", 2012],
    3: ["Tron: O Legado", "Ficção Cientifica", 2010]
}

for indice in filmes:

    print (f"Filme: {filmes[indice][0]}")
    print (f"Gênero: {filmes[indice][1]}")
    print (f"Ano: {filmes[indice][2]}")
