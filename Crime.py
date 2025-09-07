listaresposta = [] #lista para armazenar as respostas


a = str(input("Telefonou para a vítima? Responda com sim ou nao: "))
listaresposta.append(a)
b = str(input("Esteve no local do crime? Responda com sim ou nao: "))
listaresposta.append(b)
c = str(input("Mora perto da vítima? Responda com sim ou nao: "))
listaresposta.append(c)
d = str(input("Devia para a vítima? Responda com sim ou nao: "))
listaresposta.append(d)
e = str(input("Já trabalhou com a vítima? Responda com sim ou nao: "))
listaresposta.append(e)

# verifica se alguma resposta digitada não está entre as opções válidas
if a not in ("sim", "nao", "SIM", "NAO", "NÃO", "não") or \
   b not in ("sim", "nao", "SIM", "NAO", "NÃO", "não") or \
   c not in ("sim", "nao", "SIM", "NAO", "NÃO", "não") or \
   d not in ("sim", "nao", "SIM", "NAO", "NÃO", "não") or \
   e not in ("sim", "nao", "SIM", "NAO", "NÃO", "não"):
    print("Alguma resposta é inválida") # avisa se alguma resposta não é reconhecida

# conta quantas respostas "sim" foram dadas, considerando maiúsculas e minúsculas
referencia = listaresposta.count("sim") + listaresposta.count("SIM")

# verifica a quantidade de "sim" e imprime a classificação correspondente
if referencia == 2:
    print("VOCÊ É SUSPEITA")
elif referencia >=3 and referencia <=4:
    print("VOCÊ É CÚMPLICE")
elif referencia == 5:
    print("VOCÊ É ASSASSINO")
else:
    print("VOCÊ É INOCENTE")
