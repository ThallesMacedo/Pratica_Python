idade = int(input("Digite uma idade (0 para parar): "))#primeira entrada pois precisava criar a variavel e depois usa-la no while
listaidade = []
listaidade.append(idade) #primeiro adicional na lista referente a primeira entrada

while idade != 0: #roda o while até ser diferente de 0
    # aqui dentro você vai acumular a soma e contar as idades
    idade = int(input("Digite uma idade (0 para parar): ")) #pergunta até ser 0
    listaidade.append(idade) #adiciona a lista todos os dados digitados

listaidade.remove(0)#remove o numero zero pois ocupava uma posição na lista e atrapalhava o calculo da média
total = sum(listaidade) #soma os valores da lista
nidades = len(listaidade)
media = total / nidades
print(f"A soma das idades é: {total} e a sua média é de {media} anos")

