lista = []
contador = 1
ordem = 1

while contador <=10: #roda até chegar a 10º entrada de numero
    numero = int(input(f"Digite o {ordem}º número? ")) 
    contador = contador +1 #contador para quebrar o loop
    ordem = ordem + 1 #contador da ordem do numero digitado
    lista.append(numero)

print(f"O menor número digitado foi {min(lista)} e o maior digitado foi {max(lista)}")