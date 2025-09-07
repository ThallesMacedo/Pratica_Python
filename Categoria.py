idade = int(input("Digite sua idade para saber sua categoria: "))

if idade >=5 and idade <=7: #logica booleana para saída verdadeira da condição
    print("Sua categoria é Infantil")

if idade >=8 and idade <=10:
    print("Sua categoria é Iniciado")

if idade >=11 and idade <=13:
    print("Sua categoria é Juvenil")

if idade >=14 and idade <=17:
    print("Sua categoria é Junior")

if idade >18:
    print("Sua categoria é Senior")

if idade <5:
    print("Sua categoria não está disponível")

