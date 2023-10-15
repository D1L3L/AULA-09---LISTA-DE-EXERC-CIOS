#Um dicionário Python pode ser usado para modelar um dicionario de verdade. No entanto, para evitar confusão, chame este dicionário de glossario.
#Pense em cinco palavras relacionada à programação que você conhece nesta disciplina. Use estas palavras como chaves em seu glossário e armazene seus significados como valores.
#Mostre cada palavra e seu significado em uma saída, formate a saída de uma forma bem elegante. 
#Por exemplo: você pode exibir a palavra seguida de dois-pontos e depois o seu significado, ou apresentar a palavra em uma linha e então exibir seu significado identado em uma segunda linha.
# Utilize o caractere de quebra de linha (\n) para inserir uma linha em branco entre cada par palavra-significado em sua saída.
#Sugestões de termos: Algoritmos, Python, Webscraping, Lógica de Programação, Google Colab, Visual Studio Code

glossario = {
    'Algoritmos': {
        'significado': 'Conjunto de passos para realizar uma tarefa específica.',
        'exemplo': 'Ordenação de uma lista usando o algoritmo de ordenação rápida (quicksort).'
    },
    'Python': {
        'significado': 'Linguagem de programação de alto nível, interpretada e de propósito geral.',
        'exemplo': 'Print("Olá, mundo!")'
    },
    'Webscraping': {
        'significado': 'Extração de dados de sites na web.',
        'exemplo': 'Obter o título de uma página da web usando BeautifulSoup.'
    },
    'Commit': {
        'significado': 'Registro de alterações em um repositório de controle de versão.',
        'exemplo': 'git commit -m "Adicionando nova funcionalidade".'
    },
    'Debugar': {
        'significado': 'Processo de identificar e corrigir erros em um programa.',
        'exemplo': 'Adicionar pontos de interrupção e usar um depurador para encontrar bugs.'
    }
}
def exibir(termo):
    print(f'\n{termo}:')
    print(f'Significado: {glossario[termo]["significado"]}')
    print(f'Exemplo: {glossario[termo]["exemplo"]}\n')
    
for termo in glossario:
    exibir(termo)
