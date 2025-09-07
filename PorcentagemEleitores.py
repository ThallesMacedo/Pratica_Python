total = int(input("Qual o total de eleitores do seu municipio? "))
vbrancos = int(input("Total de votos brancos? "))
vnulos = int(input("Total de votos nulos? "))
vvalidos = int(input("Total de votos válidos? "))

erro = vbrancos + vnulos + vvalidos
nvotou = total - erro

if erro > total:
    print(f"A conta não bate pois o numero de brancos, nulos e validos excede o total que é: {total}")
else:
    pbrancos = (vbrancos / total) * 100
    pnulos = (vnulos / total) * 100
    pvalidos = (vvalidos / total) * 100
    pnvotou = (nvotou/ total) * 100

    print(f"Porcentagem de brancos: {pbrancos}%")
    print(f"Porcentagem de nulos: {pnulos}%")
    print(f"Porcentagem de válidos: {pvalidos}%")
    print(f"Porcentagem de pessoas que não votaram: {pnvotou}%")