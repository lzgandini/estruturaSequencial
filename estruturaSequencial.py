#1 Faça um Programa que mostre a mensagem "Alo mundo" na tela.

print("Olá mundo")

#2 Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número].

numero = int(input("Escolha um número: "))
print("O número informado foi {}".format(numero))

#3 Faça um Programa que peça dois números e imprima a soma.

numero2 = int(input("Escolha outro número: "))
soma = numero + numero2
print("A soma dos dois números é: {}".format(soma))

#4 Faça um Programa que peça as 4 notas bimestrais e mostre a média.

print("Agora vamos calcular tua média? (de 0 a 10)!")
nota1 = int(input("Digite a primeira nota: "))
nota2 = int(input("Digite a segunda nota: "))
nota3 = int(input("Digite a terceira nota: "))
nota4 = int(input("Digite a quarta nota: "))
media = (nota1 + nota2 + nota3 + nota4) / 4
print("A media final é: {} pontos".format(media))

#5 Faça um Programa que converta metros para centímetros.

print("Vamos converter metros para centímetros?")
metros = float(input("Digite a quantidade de metros: "))
centimetros = metros * 100
print("São {} centímetros.".format(centimetros))

#6 Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

print("Calculando a área da pizza!")
raio = float(input("Informe quantos centímetros tem o raio da pizza: "))
area = 3.14 * raio * raio
print("A pizza tem {} centímetros de área".format(area))

#7 Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

print("Calculando a área de um quadrado!")
base = float(input("Informe quantos centímetros tem a base do quadrado: "))
altura = float(input("Informe quantos centímetros tem a altura do quadrado: "))
area = base * altura
print("Duas vezes o valor da área do quadrado é {}".format(area * 2))

#8 Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês.

print("Vamos calcular o salário deste mês!")
salarioDia = float(input("Quanto você ganha por hora? "))
horasDia = float(input("E quantas horas trabalha por dia? "))
horasMes = horasDia * 20
salarioMes = salarioDia * horasMes
print("Você vai receber {} neste mês!".format(salarioMes))

#9 Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
# C = 5 * ((F-32) / 9).

print("Conversor de temperatura de Fahrenheit para graus Celsius")
fahrenheit = float(input("Informe a temperatura em Fahrenheit: "))
celsius = 5 * ((fahrenheit - 32) / 9)
print("A temperatura é {} graus Celsius".format(celsius))

#10 Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.

print("Conversor de temperatura de Celsius para graus Fahrenheit")
celsius = float(input("Informe a temperatura em Celsius: "))
fahrenheit = ((celsius - 32) * 5) / 9
print("A temperatura é {} graus Fahrenheit".format(fahrenheit))

#11 Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# a) o produto do dobro do primeiro com metade do segundo .
# b) a soma do triplo do primeiro com o terceiro.
# c) o terceiro elevado ao cubo.

numeroInt1 = int(input("Informe um número inteiro: "))
numeroInt2 = int(input("Informe outro número inteiro: "))
numeroReal = float(input("Informe um número real: "))
a = (numeroInt1 * 2) * (numeroInt2 / 2)
b = (numeroInt1 * 3) + numeroReal
c = numeroReal * numeroReal * numeroReal
print("O produto do dobro do primeiro com metade do segundo é {}".format(a))
print("A soma do triplo do primeiro com o terceiro é {}".format(b))
print("o terceiro elevado ao cubo é {}".format(c))

#12 Tendo como dados de entrada a altura de uma pessoa,
# construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58

altura = float(input("Digite sua altura: "))
pesoIdeal = (72.7 * altura) - 58
print("Seu peso ideal é {}".format(pesoIdeal))

#13 Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal,
# utilizando as seguintes fórmulas:
# a)Para homens: (72.7*h) - 58
# b)Para mulheres: (62.1*h) - 44.7

altura = float(input("Digite sua altura: "))
pesoIdeal = (62.1 * altura) - 44.7
print("Seu peso ideal é {}".format(pesoIdeal))

#14 João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho.
# Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do
# estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um
# programa que leia a variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de
# quilos além do limite e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as
# mensagens adequadas.

print("Pescador High-Tech")
quilos = float(input("Informe a quantidade de quilos: "))
if quilos > 50:
    excesso = quilos - 50
    multa = excesso * 4
    print("A quantidade de quilos excedente é {}".format(excesso))
    print("Deverá ser paga a multa de {} reais".format(multa))
else:
    print("Não há quilos excedentes.")

#15 Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda,
# 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
# a)salário bruto.
# b)quanto pagou ao INSS.
# c)quanto pagou ao sindicato.
# d)o salário líquido.
# e)calcule os descontos e o salário líquido, conforme a tabela abaixo:

print("Vamos ao seu contracheque!")
salarioDia = float(input("Quanto você ganha por hora? "))
horasDia = float(input("E quantas horas trabalha por dia? "))
horasMes = horasDia * 20
salarioBruto = salarioDia * horasMes
iR = salarioBruto * 0.11
inss = salarioBruto * 0.08
sindicato = salarioBruto * 0.05
salarioLiquido = salarioBruto - iR - inss - sindicato

print("\n")
print("+ Salário Bruto: R$ {}".format(salarioBruto))
print("- IR (11%): R$ {}".format(iR))
print("- INSS (8%): R$ {}".format(inss))
print("- Sindicato (5%): R$ {}".format(sindicato))
print("= Salário Líquido: R$ {}".format(salarioLiquido))

#16 Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
# Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros,
# que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

import math

tamanho = float(input("Informe quantos metros quadrados vão ser pintados: "))
litrosPorMetro2 = tamanho / 3
litrosDaLata = 18
valorDaTinta = 80.0

totalDeLatas = math.ceil(litrosPorMetro2 / litrosDaLata)
custoTotal = totalDeLatas * valorDaTinta
print("Serão usadas {} latas de tinta e o custo total será de R$ {}".format(totalDeLatas, custoTotal))

#17 Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
# Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros,
# que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
# Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
# a)comprar apenas latas de 18 litros;
# b)comprar apenas galões de 3,6 litros;
#c) misturar latas e galões, de forma que o desperdício de tinta seja menor.
# Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

import math

tamanho = float(input("Informe quantos metros quadrados vão ser pintados: "))
litrosPorMetro2 = (tamanho / 6) + ((tamanho / 6) * 0.1)
litrosDaLata1 = 18
valorDaTinta1 = 80.0
litrosDaLata2 = 3.6
valorDaTinta2 = 25.0

#letra a
totalDeLatasA = math.ceil(litrosPorMetro2 / litrosDaLata1)
custoTotalA = totalDeLatasA * valorDaTinta1
print("Serão usadas {} latas de tinta de 18 litros e o custo total será de R$ {}, ".format(totalDeLatasA, custoTotalA))

#letra b
totalDeLatasB = math.ceil(litrosPorMetro2 / litrosDaLata2)
custoTotalB = totalDeLatasB * valorDaTinta2
print("Serão usadas {} latas de tinta de 3,6 litros e o custo total será de R$ {}, ".format(totalDeLatasB, custoTotalB))

#letra c
latasUsadasTipo1 = litrosPorMetro2 // litrosDaLata1
custoLatasTipo1 = latasUsadasTipo1 * valorDaTinta1

latasUsadasTipo2 = math.ceil(latasUsadasTipo1 % litrosDaLata2)
custoLatasTipo2 = latasUsadasTipo2 * valorDaTinta2

custoTotalC = custoLatasTipo1 + custoLatasTipo2
print("Serão usadas {} latas de tinta de 18 litros e {} latas de tinta de 3,6 litros. O custo total será de R$ {}."
      .format(latasUsadasTipo1, latasUsadasTipo2, custoTotalC))

#18 Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps),
# calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

tamanho = float(input("Digite quantos MB tem o arquivo para download: "))
velocidade = float(input("Digite quantos Mbps têm a velocidade de um link de Internet: "))

velocidadeEmMB = velocidade / 8
tempoPorSegundo = tamanho / velocidadeEmMB
tempoPorMinuto = tempoPorSegundo / 60

print("Serão necessários {} minutos para baixar este arquivo.".format(tempoPorMinuto))
