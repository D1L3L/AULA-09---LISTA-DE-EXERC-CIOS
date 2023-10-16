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