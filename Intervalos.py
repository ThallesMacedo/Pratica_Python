numa = int(input("Digite o número inferior: "))
numb = int(input("Digite o número superior: "))
lista = []

numeros = list(range(numa,numb +1)) # range(inicio, fim) gera números inteiros do início até fim -1, por isso o +1 para incluir o limite superior 
# list(range(...)) transforma a sequência do range em uma lista

if numa>numb:
    print("Erro no sistema, numero inferior maior que o superior")

for n in numeros:
    if n % 2 == 0:
        lista.append(n)

total = sum(lista)
print(f"Os números pares desse conjunto de numeros são: {lista} e a soma desses números pares é de {total}")