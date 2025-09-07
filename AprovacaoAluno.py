assiduidade = float(input("Qual foi a porcentagem de presença nas aulas? "))
nota = float(input("Qual foi sua nota do teste? "))

if assiduidade > 100 or assiduidade <0 or nota >20: #lógica booleana para identificar erros na processo de aprovação do aluno
    print("ERRO DE SISTEMA, TENTE NOVAMENTE")

if assiduidade < 75:
    print("VOCE FOI REPROVADO")

if assiduidade >= 75 and nota <5:
    print("VOCE FOI REPROVADO")

if assiduidade >= 75 and nota <9.5:
    print("VOCE FICOU DE EXAME")

if assiduidade >= 75 and nota <=20:
    print("VOCE FOI APROVADO")