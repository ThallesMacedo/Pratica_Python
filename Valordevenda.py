vcompra = float(input("Digite o valor da compra do produto: "))

if vcompra <10:
    vadicional = (vcompra*70) / 100 #descubra o valor adicional para revenda
    vnovo = vcompra + vadicional #acrescente o valor adicional ao valor da compra
    print(f"O valor de venda deverá ser de {vnovo}R$")

if vcompra >=10 and vcompra <30:
    vadicional = (vcompra*50) / 100
    vnovo = vcompra + vadicional
    print(f"O valor de venda deverá ser de {vnovo}R$")

if vcompra >=30 and vcompra <50:
    vadicional = (vcompra*40) / 100
    vnovo = vcompra + vadicional
    print(f"O valor de venda deverá ser de {vnovo}R$")

if vcompra >=50:
    vadicional = (vcompra*30) / 100
    vnovo = vcompra + vadicional
    print(f"O valor de venda deverá ser de {vnovo}R$")