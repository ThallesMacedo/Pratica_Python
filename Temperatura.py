listavaziatemperatura = [] # lista que vai guardar apenas as temperaturas acima da média
listavaziameses = [] # lista que guarda todas as temperaturas digitadas
listavaziames = [] # lista que guarda os meses correspondentes às temperaturas acima da média
listaordem = [] # lista que guarda a ordem (números) dos meses acima da média
contadormes = 1 # contador para saber quantos meses já foram usados no cálculo da média
contador = 0 # contador para numerar os meses que ficaram acima da média

for i in range(12): # repete 12 vezes (pode ser trocado pelo número de meses desejados)
    temperatura = float(input("Digite a temperatura média do mes: "))
    mes = str(input("Digite o mes referente: "))
    listavaziameses.append(temperatura)
    mediaanual = sum(listavaziameses) / contadormes # calcula a média parcial até agora
    contadormes = contadormes + 1  # incrementa o contador de meses (para próxima média)

    if temperatura > mediaanual:# verifica se a temperatura atual é maior que a média calculada
        listavaziatemperatura.append(temperatura)
        listavaziames.append(mes)
        contador= contador + 1 # incrementa o contador de meses acima da média
        listaordem.append(contador)

# junta número e mês (ex: "1 - Fevereiro / 2 - Março") usando zip
resultado = " / ".join(f"{num} - {mes}" for num, mes in zip(listaordem, listavaziames))
print(f"Os meses com tempertura mais alta que a média de {mediaanual}º é: {resultado}")
