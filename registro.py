# variáveis de controle
mais_pesado = ""
peso_maior = 0

mais_alto = ""
altura_maior = 0

# repetição para 2 pessoas
for i in range(2):
    nome = input("Digite o nome da pessoa: ")
    altura = float(input("Digite a altura: "))
    peso = float(input("Digite o peso: "))
    
    # verificar quem é o mais pesado
    if peso > peso_maior:
        peso_maior = peso
        mais_pesado = nome
    
    # verificar quem é o mais alto
    if altura > altura_maior:
        altura_maior = altura
        mais_alto = nome

# saída final
print("A pessoa mais pesada é:", mais_pesado)
print("A pessoa mais alta é:", mais_alto)
