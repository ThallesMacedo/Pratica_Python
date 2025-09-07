ano = int(input("Digite quantos anos você tem: "))
meses = int(input("Digite os meses: "))
dias= int(input("Digite os dias: "))

diasano = ano * 365  #descobrir  total de dias referente aos anos vividos
diasmeses = meses * 30 #descobrir o total de dias referentes ao meses vividos
idadedias = dias + diasmeses + diasano #soma total de dias entre anos, meses e dias apontados pelas entradas dos usuarios

print(f"Você tem {ano} anos, {meses} meses e {dias} dias")
print(f"E seus dias totais de idade são {idadedias} dias")