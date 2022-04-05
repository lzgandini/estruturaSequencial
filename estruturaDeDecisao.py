"""
#1 Faça um Programa que peça dois números e imprima o maior deles.

numero1 = int(input("Escolha um número: "))
numero2 = int(input("Escolha outro número: "))

if (numero1 > numero2):
    maior = numero1
else:
    maior = numero2
print("O maior número é o {}".format(maior))

#2 Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.
numero = float(input("Escolha um número real: "))

if numero > 0:
    print("O número informado é positivo")
elif numero < 0:
    print("O número informado é negativo")
else:
    print("O número informado é zero e não quero orbigá-lo a ser binário!")

#3 Faça um Programa que verifique se uma letra digitada é "F" ou "M".
# Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

letra = (input("Informe o gênero: ")).upper()
if letra == "F":
    print("F - Feminino")
elif letra == "M":
    print("M - Masculino")
else:
    print("Outro")

#4 Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

letra = (input("Digite uma letra: ")).upper()

if letra == "A":
    print("Você digitou uma vogal")
elif letra == "E":
    print("Você digitou uma vogal")
elif letra == "I":
    print("Você digitou uma vogal")
elif letra == "O":
    print("Você digitou uma vogal")
elif letra == "U":
    print("Você digitou uma vogal")
else:
    print("Você digitou uma consoante")

#5 Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada
# por aluno e apresentar:
#A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
#A mensagem "Reprovado", se a média for menor do que sete;
#A mensagem "Aprovado com Distinção", se a média for igual a dez.

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media = (nota1 + nota2) / 2

if media >= 7 and media < 10:
    print("Aprovado")
elif media < 7:
    print("Reprovado")
else:
    print("Aprovado com distinção")

#6 Faça um Programa que leia três números e mostre o maior deles.
numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
numero3 = int(input("Digite o terceiro número: "))

maior = max(numero1, numero2, numero3)
print("O maior número é o {}".format(maior))

#7 Faça um Programa que leia três números e mostre o maior e o menor deles.
numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
numero3 = int(input("Digite o terceiro número: "))

maior = max(numero1, numero2, numero3)
menor = min(numero1, numero2, numero3)
print("O maior número é o {} e o menor é o {}".format(maior, menor))

#8 Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar,
# sabendo que a decisão é sempre pelo mais barato.

print("Semana da Beleza no Guanabara!")
marcas = ["Dove", "Seda", "Loreal"]
shampoo1 = float(input("Informe o preço do shampoo Dove: "))
shampoo2 = float(input("Informe o preço do shampoo Seda: "))
shampoo3 = float(input("Informe o preço do shampoo Loreal: "))

menor = min(shampoo1, shampoo2, shampoo3)

print("Hoje é dia de comprar o que custa R$ {}".format(menor))

#9 Faça um Programa que leia três números e mostre-os em ordem decrescente.

numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
numero3 = int(input("Digite o terceiro número: "))

todosOsNumeros = [numero1, numero2, numero3]
todosOsNumeros.sort(reverse=True)

print("A ordem decrescente dos números é {}, {} e {}.".format(todosOsNumeros[0], todosOsNumeros[1], todosOsNumeros[2]))

#10 Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno.
# Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

turno = (input("Digite a letra inicial do turno em que você estuda\n(M-Matutino ou V-Vespertino ou N-Noturno): ")).upper()

if turno == "M":
    print("Bom dia!")
elif turno == "V":
    print("Boa tarde!")
elif turno == "N":
    print("Boa noite!")
else:
    print("Valor inválido.")

#11 As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para
# desenvolver o programa que calculará os reajustes.
# Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
# a)salários até R$ 280,00 (incluindo) : aumento de 20%
# b)salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
# c)salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
# d)salários de R$ 1500,00 em diante : aumento de 5%
# Após o aumento ser realizado, informe na tela:
# e)o salário antes do reajuste;
# f)o percentual de aumento aplicado;
# g)o valor do aumento;
# h)o novo salário, após o aumento.

salarioInicial = float(input("Qual é o teu salário? "))

if salarioInicial <= 280:
    percentual = 0.2
    aumento = salarioInicial * percentual
    salarioAumentado = salarioInicial + aumento

elif salarioInicial > 280 and salarioInicial <= 700:
    percentual = 0.15
    aumento = salarioInicial * percentual
    salarioAumentado = salarioInicial + aumento

elif salarioInicial > 700 and salarioInicial <= 1500:
    percentual = 0.1
    aumento = salarioInicial * percentual
    salarioAumentado = salarioInicial + aumento

else:
    percentual = 0.05
    aumento = salarioInicial * percentual
    salarioAumentado = salarioInicial + aumento

print("- Seu salário era inicialmente de R$ {}.".format(salarioInicial))
print("- Você recebeu um aumento de R$ {}, que dá R$ {}".format(percentual, aumento))
print("- Seu novo salário é de R$ {}.".format(salarioAumentado))

#12 Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda,
# que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto,
# mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos.
# O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
#Desconto do IR:
#Salário Bruto até 900 (inclusive) - isento
#Salário Bruto até 1500 (inclusive) - desconto de 5%
#Salário Bruto até 2500 (inclusive) - desconto de 10%
#Salário Bruto acima de 2500 - desconto de 20%
# Imprima na tela as informações, dispostas conforme o exemplo abaixo.
# No exemplo o valor da hora é 5 e a quantidade de hora é 220.
#        Salário Bruto: (5 * 220)        : R$ 1100,00
 #       (-) IR (5%)                     : R$   55,00
  #      (-) INSS ( 10%)                 : R$  110,00
   #     FGTS (11%)                      : R$  121,00
    #    Total de descontos              : R$  165,00
     #   Salário Liquido                 : R$  935,00

valorHora = float(input("Informe quanto você ganha por hora: "))
horasDia = float(input("Informe quantas horas você trabalha por dia: "))
horasMes = horasDia * 20
salarioBruto = valorHora * horasMes

if salarioBruto <= 900:
    iR = 0
    inss = salarioBruto * 0.1
    fgts = salarioBruto * 0.11

elif salarioBruto > 900 and salarioBruto <= 1500:
    iR = salarioBruto * 0.05
    inss = salarioBruto * 0.1
    fgts = salarioBruto * 0.11

elif salarioBruto > 1500 and salarioBruto <= 2500:
    iR = salarioBruto * 0.05
    inss = salarioBruto * 0.1
    fgts = salarioBruto * 0.11

else:
    iR = salarioBruto * 0.05
    inss = salarioBruto * 0.1
    fgts = salarioBruto * 0.11

totalDeDescontos = iR + inss
salarioLiquido = salarioBruto - totalDeDescontos

print("Salário Bruto:                    : R$   {}".format(salarioBruto))
print("(-) IR (5%)                       : R$   {}".format(iR))
print("(-) INSS ( 10%)                   : R$   {}".format(inss))
print("FGTS (11%)                        : R$   {}".format(fgts))
print("Total de descontos                : R$   {}".format(totalDeDescontos))
print("Salário Liquido                   : R$   {}".format(salarioLiquido))

#13 Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.),
# se digitar outro valor deve aparecer valor inválido.

diaNumero = int(input("Digite o dia da semana conforme o número (1-Domingo, 2- Segunda, etc.): "))

if diaNumero == 1:
    print("O dia de hoje é Domingo")
elif diaNumero == 2:
    print("O dia de hoje é Segunda")
elif diaNumero == 3:
    print("O dia de hoje é Terça")
elif diaNumero == 4:
    print("O dia de hoje é Quarta")
elif diaNumero == 5:
    print("O dia de hoje é Quinta")
elif diaNumero == 6:
    print("O dia de hoje é Sexta")
elif diaNumero == 7:
    print("O dia de hoje é Sábado")
else:
    print("Valor inválido")

#14 Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre,
# e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
#  Média de Aproveitamento  Conceito
#  Entre 9.0 e 10.0        A
#  Entre 7.5 e 9.0         B
#  Entre 6.0 e 7.5         C
#  Entre 4.0 e 6.0         D
#  Entre 4.0 e zero        E
#O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o
# conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media = (nota1 + nota2) / 2

if media >= 9:
    conceito = "A"
elif media >= 7.5 and media < 9:
    conceito = "B"
elif media >= 6 and media < 7.5:
    conceito = "C"
elif media >= 4 and media < 6:
    conceito = "D"
elif media < 4:
    conceito = "E"

if conceito == "A" or conceito == "B" or conceito == "C":
    aprovacao = "APROVADO"
else:
    aprovacao = "REPROVADO"

print("Suas notas foram {} e {}".format(nota1, nota2))
print("A média final ficou em {} pontos".format(media))
print("Você obtece o conceito {} e está {}".format(conceito, aprovacao))

#15 Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo.
# Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
#Dicas:
#Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
#Triângulo Equilátero: três lados iguais;
#Triângulo Isósceles: quaisquer dois lados iguais;
#Triângulo Escaleno: três lados diferentes;

lado1 = float(input("Informe o primeiro lado do triângulo: "))
lado2 = float(input("Informe o segundo lado do triângulo: "))
lado3 = float(input("Informe o terceiro lado do triângulo: "))

if (lado1 + lado2) > lado3:
    triangulo = True
elif (lado1 + lado3) > lado2:
    triangulo = True
elif (lado2 + lado3) > lado1:
    triangulo = True
else:
    triangulo = False

if triangulo == True:
    if lado1 == lado2 == lado3:
        print("É um triângulo Equilátero!")
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print("É um triângulo Isósceles!")
    else:
        print("É um triângulo Escaleno")
else:
    print("Não é um triângulo!")

#16 Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c.
# O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:
#Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir
# os demais valores, sendo encerrado;
#Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
#Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
#Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;

import math

print("Equação de Segundo Grau")
a = float(input("Informe o valor de A: "))
b = float(input("Informe o valor de B: "))
c = float(input("Informe o valor de C: "))

if a == 0:
    print("Como não há valor de A, é uma Equação de Primeiro Grau. Não é possível continuar o cálculo.")
    #break
else:
    delta = (b * b) - (4 * a * c)
    if delta < 0:
        print("A equação não possui raízes reais. Não é possível continuar o cálculo.")
        #break
    elif delta == 0:
        print("A equação possui apenas uma raiz real, que é zero.")
    else:
        raizDelta = math.sqrt(delta)
        x1 = (-b + raizDelta) / (2 * a)
        x2 = (-b - raizDelta) / (2 * a)
        print("A equação possui duas raízes reais, {} e {}".format(x1, x2))
"""
