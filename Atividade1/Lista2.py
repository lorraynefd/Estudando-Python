
Q1
valor1=float(input('Digite um número:'))
valor2=float(input('Digite outro número: '))
if valor1 > valor2:
    print("{} é maior que {}.".format(valor1, valor2))
elif valor1 == valor2:
    print("{} é igual a {}.".format(valor2, valor1))
else:
    print("{} é maior que {}.".format(valor2, valor1))

Q2
valor=float(input('Digite um valor: '))
if valor>0:
    print('{} é positivo'.format(valor))
else:
    print('{} é negativo'.format(valor))2

Q3
valor = float(input('Digite um número: '))
if valor%2 == 0:
    print('O número {} é par'.format(valor))
else:
    print('O número {} é impar'.format(valor))

Q4
n=float(input('Digite um número: '))
if n==int(n):
    print('O número {} é intero '.format(n))
else:
    print('O número {} é decimal'.format(n))

Q5
n1 = float(input('Digite um número: '))
n2 = float(input('Digite um número: '))
operação = input('Que tipo de operação você deseja (+ - * /): ')

if operação == '+':
    resultado = n1 + n2
    print('O resulado da adiçaõ é {}'.format(resultado))
elif operação == '-':
    resultado = n1 - n2
    print('O resultado da subtração é {}'.format(resultado))
elif operação == '*':
    resultado = n1 * n2
    print('O resultado da muliplição é {}'.format(resultado))
elif operação == '/':
    resultado = n1 / n2
    print('O resultado da divisão é {}'.format(resultado))
if  resultado % 2 == 0:
    print('O resultado é {} par'.format(resultado))
else:
    print('O resultado é {} impar '.format(resultado))
if resultado > 0:
    print('O resultado {} é positivo'.format( resultado))
elif resultado == 0:
    print('O resutado {} é neutro'.format( resultado))
else:
    print('O resultado {} é negativo'.format( resultado))
if resultado == int(resultado):
    print('O resutado {} é inteiro'.format( resultado))
else:
    print('O resultado {} é decimal'.format( resultado))

Q6
genero=str(input('Digite F para (feminino) e M para (masculino):  '))
if genero=='F':
    print('Feminino')
elif genero=='M':
    print('Masculino')
else:
    print('Sexo invalido')

Q7
letras=input('Digite uma letra: ')
if letras =='a'or letras=='e'or letras=='i'or letras=='o'or letras=='u':
    print('Vogal')
else:
    print('Consoante')

Q8
nota1=float(input('Digite sua nota: '))
nota2=float(input('Digite sua nota: '))
sum=(nota1+nota2)/2
if sum>=10:
    print('Aprovado com distinção')
elif  sum>=7:
    print('Aprovado')
else:
    print('Reprovado')

Q9
n1=float(input('Digite um numeo: '))
n2=float(input('Digite um numeo: '))
n3=float(input('Digite um numeo: '))
if n1>n2 and n1>n3:
    print('{} é maior que os outros números: '.format(n1))
elif n2>n3  and n2>n1:
    print('{} é maior que os outros números: '.format(n2))
else:
    print('{} é maior que os outros números: '.format(n3))

Q10
n1=float(input('Digite um numeo: '))
n2=float(input('Digite um numeo: '))
n3=float(input('Digite um numeo: '))
if n1>n2 and n1>n3:
    print('{} é maior que os outros números: '.format(n1))
elif n2>n3  and n2>n1:
    print('{} é maior que os outros números: '.format(n2))
else:
    print('{} é maior que os outros números: '.format(n3))
if n1<n2 and n1<n3:
    print('{} é menor que os outros números: '.format(n1))
elif n2<n3  and n2<n1:
    print('{} é menor que os outros números: '.format(n2))
else:
    print('{} é menor que os outros números: '.format(n3))

Q11
v1=float(input('Digite o valor do produto 1:'))
v2=float(input('Digite o valor do produto 2:'))
v3=float(input('Digite o valor do produto 3:'))
if v1<v2 and v1<v3:
    print('Você deve comprar o produto 1')
elif v2<v1 and v2<v3:
    print('Você deve comprar o produto 2')
else:
    print('Você deve comprar o produto 3')

Q12
n1=float(input('Digite um numeo: '))
n2=float(input('Digite um numeo: '))
n3=float(input('Digite um numeo: '))
if n1>n2 and n1>n3:
    if n2>n3:
        print('{},{},{}'.format(n1,n2,n3))
    else:
        print('{},{},{}'.format(n1, n3, n2))
elif n2>n1 and n2>n3:
    if n1>n3:
        print('{},{},{}'.format(n2, n1, n3))
    else:
        print('{},{},{}'.format(n2, n3, n1))
elif n3>n1 and n3>n2:
    if n1>n2:
        print('{},{},{}'.format(n3, n1, n2))
    else:
        print('{},{},{}'.format(n3, n2, n1))
Q13
turno=(input('Digite o turno em que você estuda M:manhã /V:vespertino /N:noturno ; '))
if turno=='M':
    print('Bom Dia')
elif turno=='V':
    print('Boa Tarde')
elif turno=='N':
    print('Boa Noite')
else:
    print('Valor Inválido')

Q14
salario=float(input('Digite o seu salário R$;'))
if salario<=280:
    percentual=20
    aumento=salario*0.2
    reajuste=aumento+salario
    print('O seu salario sera de R${}'.format(reajuste))
elif salario<=700:
    percentual=15
    aumento=salario*0.15
    reajuste=aumento+salario
    print('O seu salario sera de R${}'.format(reajuste))
elif salario<=1500:
    percentual=10
    aumento=salario*0.1
    reajuste=aumento+salario
    print('O seu salario sera de R${}'.format(reajuste))
elif salario >=1500:
    percentual=5
    aumento = salario * 0.05
    reajuste = aumento + salario
    print('O seu salario sera de R${}'.format(reajuste))
print('Salário antes do aumento era de {}'.format(salario))
print('O percentual de aumento aplicado foi de {}% '.format(percentual))
print('Ovalor do almento foi de {}'.format(aumento))

Q15
ganha_h=float(input('Quanto vc ganha por hora: '))
horas_mês=float(input('quantas horas por mês: '))
salario_bruto=ganha_h*horas_mês
fgts=salario_bruto*0.11
sindicato=salario_bruto*0.03
inss=salario_bruto*0.1
print('     ------Folha de pagamento------    ')
if salario_bruto < 900:
   desconto = 0
elif salario_bruto<1500:
    desconto=salario_bruto*0.05
elif salario_bruto<2500:
    desconto=0.1
elif salario_bruto>2500:
    desconto=0.2
salario_líquido=salario_bruto-desconto-inss
print('+ Salário Bruto     :R$ {}'.format(salario_bruto))
print('- IR                :R$ {}'.format(desconto))
print('FGTS (8%)           :R$ {}'.format(fgts))
print('- INSS (10%)        :R$ {}'.format(inss))
print('Sindicato (3%)      :R$ {}'.format(sindicato))
print('=Salário liquido    :R$ {}'.format(salario_líquido))

Q16
num=int(input('Digite um numero entre 1 a 7:  '))
if num==1:
   print('Doomingo')
elif num==2:
    print('Segunda')
elif num==3:
    print('Terça')
elif num==4:
     print('Quarta')
elif num==5:
    print('Quinta')
elif num==6:
    print('Sexta')
elif num==7:
    print('Sabado')
else:
    print('Valor invalido')

Q17
altura=float(input('Qual é a sua altura:'))
sexo=input('Qual e o seu sexo (masculino=M)(feminino=F): ')
peso_pessoa=float(input('Qual é o seu peso: '))
ideal_homen = (72.7* altura) - 58
ideal_mulher= (62.1* altura) - 44.7

if sexo=='M':
    if peso_pessoa > ideal_homen:
        print('Acima do peso.')
    elif peso_pessoa<ideal_homen:
        print('Abaixo do peso.')
    else:
        print('Peso idela.')

if  sexo=='F':
    if peso_pessoa>ideal_mulher:
     print('Acima do peso.')
    elif peso_pessoa<ideal_mulher:
     print('Abaixo do peso.')
    else:
        print('Peso idela.')

Q18
peso_peixe=float(input('Qual é o peso do peixe: '))
peso_excesso=peso_peixe-50
taxa_paga=peso_excesso*4
print('            ----Nota----   ')
if peso_peixe>50:
    print('Você excedeu o peso permitido')
    print('sua multa sera de;R${}'.format(taxa_paga))
else:
    print('Você não excedeu o peso permitido')
    print('sua multa sera de;R$0,00')

Q19
nota1=float(input('Sua nota : '))
nota2=float(input('Sua nota : '))
media=(nota1+nota2)/2
if media>9 :
    conceito='A'
elif media>7.5:
     conceito='B'
elif media>6:
    conceito='C'
elif media>4 :
    conceito='D'
elif  media<=0:
    conceito = 'E'
print('         Boletinho Escolar ')
print('Media de Aproveitamento      conceito')
print('          {}                    {}     '.format(media,conceito))
if conceito=='A'or conceito=='B' or conceito=='C':
   print('Aprovado')
else:
    print('Reprovado')

Q20
nota1=float(input('Digite a nota: '))
nota2=float(input('Digite a nota: '))
nota3=float(input('Digite a nota: '))
media=(nota1+nota2+nota3)/3

if media>=10:
    conceito='Aprovado com distinção'
elif   media>=7:
    conceito='Aprovado'
else:
    conceito='Reprovado'

print('       Boletinho Escolar ')
print('Media de Aprveitamento      Resultado')
print('       {}                       {}   '.format(media,conceito))

Q21
aresta1=float(input('Digite a 1º aresta: '))
aresta2=float(input('Digite a 2º aresta: '))
aresta3=float(input('Digite a 3º aresta: '))

if aresta1+aresta2>aresta3 or aresta2+aresta3>aresta1 or aresta1+aresta3>aresta2:
     print('Triângulo ')
     if aresta1 == aresta2 == aresta3:
        print('Triângulo Equilátero')
     elif aresta1 == aresta2 or aresta2 == aresta3:
        print('Triângulo Isósceles')
     elif aresta1 != aresta2 or aresta1 != aresta3:
        print('Triângulo Escaleno')
else:
    print('Não é um triângulo ')

Q22
contador=0
print('---------PERGUNTAS-----------')
print('Responda com S=sim e N=não;')
p1=input('Telefonou para a vítima? ')
if p1=='s':
    contador=contador+1
p2=input('Esteve no local do crime? ')
if p2=='s':
    contador=contador+1
p3=input('Mora perto da vítima? ')
if p3=='s':
    contador=contador+1
p4=input('Já trabalhou com a vítima?')
if p4=='s':
    contador=contador+1
p5=input('Devia pra a vítima?')
if p5=='s':
    contador=contador+1
if contador==2:
    print('Suspeito')
elif contador==3 or contador==4:
    print('Cúmplice')
elif contador==5:
    print('Assassino')
else:
    print('Inocente')

Q23
valor_min=10
valor_max=600
saque=int(input('Qual o valor do saque desejado?'))
if saque < valor_max and saque > valor_min:
    cem=saque // 100
    saque=saque%100
    cinquenta=saque // 50
    saque=saque%50
    dez = saque // 10
    saque = saque % 100
    cinco = saque // 5
    saque = saque % 5
    um = saque // 1
    print('---------- Você Recebera -----------')
    print('           {} notas de R$100'.format(cem))
    print('           {} notas de R$50'.format(cinquenta))
    print('           {} notas de R$10'.format(dez))
    print('           {} notas de R$5'.format(cinco))
    print('           {} notas de R$1'.format(um))

Q24
gasolina=2.50
alcool=1.90
pedido1=input('Você deseja álcool=A/gasolina=G? ')
pedido2=float(input('Quantos litros? '))

if pedido1=='A':
    if pedido2<20:
        desconto=(alcool*pedido2)*0.03
        valor_pago=(alcool*pedido2)-desconto
    elif pedido2>=20:
        desconto = (alcool * pedido2) * 0.05
        valor_pago = (alcool * pedido2) - desconto

if pedido1=='G':
    if pedido2 < 20:
        desconto = (gasolina * pedido2) * 0.04
        valor_pago = (gasolina * pedido2) - desconto
    elif pedido2 >= 20:
        desconto = (gasolina * pedido2) * 0.06
        valor_pago = (gasolina * pedido2) - desconto

print('O valor a ser pago é {}'.format(valor_pago))

Q25
pedido1=input('Você deseja morango/maçã? ')
pedido2=float(input('Quantos quilos? '))
if pedido1=='morango':
    if pedido2<=5:
        morango=2.50
        valor=pedido2*morango
        deve_pagar = valor
    elif pedido2>=5:
        morango=2.20
        valor=pedido2*morango
        deve_pagar = valor
    if pedido2 >= 8 or valor >= 25:
        desconto = valor * 0.1
        deve_pagar = valor - desconto
if pedido1=='maçã':
    if pedido2<=5:
        maçã=1.80
        valor=pedido2*maçã
        deve_pagar = valor
    elif pedido2>=5:
        maçã=1.50
        valor=pedido2*maçã
        deve_pagar = valor
    if pedido2>=8 or valor>=25:
        desconto= valor*0.1
        deve_pagar=valor-desconto
print('    --------Nota---------     ')
print('Você comprou {} Kg de {}.'.format(pedido2,pedido1))
print('   Pagara {} reais'.format(deve_pagar))

Q26
pedido1=input('Você deseja File_Duplo/Alcatra/Picanha? ')
pedido2=float(input('Quantos quilos? '))
pedido3=input('Qual sera a forma de pagamento (cartão Tabajara= T/Dinheiro=D)? ')
if pedido1=='File_Duplo':
    if pedido2<=5:
        File_Duplo=4.90
        valor = pedido2 * File_Duplo
        deve_pagar = valor
    elif pedido2>=5:
        File_Duplo=5.80
        valor=pedido2*File_Duplo
        deve_pagar = valor
if pedido1=='Alcatra':
    if pedido2<=5:
         Alcatra=5.90
         valor=pedido2*Alcatra
         deve_pagar = valor
    elif pedido2>=5:
         Alcatra=6.80
         valor=pedido2*Alcatra
         deve_pagar = valor
if pedido1=='Picanha':
    if pedido2<=5:
         Picanha=6.90
         valor=pedido2*Picanha
         deve_pagar = valor
    elif pedido2>=5:
         Picanha=7.80
         valor=pedido2*Picanha
         deve_pagar = valor
if pedido3=='T':
    desconto= valor*0.05
    deve_pagar=valor-desconto
    print('    --------Nota---------     ')
    print('-Você comprou:                {}'.format(pedido1))
    print('-Você comprou:                {} Kg.'.format(pedido2))
    print('-Valor sem desconto:          R${} '.format(valor))
    print('-Tipo de pagamento sera:      {}'.format(pedido3))
    print('-Desconto:                    R${}'.format(desconto))
    print('-Valor a Pagar:               R${}'.format(deve_pagar))
elif pedido3=='D':
    deve_pagar=valor
    print('    --------Nota---------     ')
    print('-Você comprou:                {}'.format(pedido1))
    print('-Você comprou:                {} Kg.'.format(pedido2))
    print('-Tipo de pagamento sera:      {}'.format(pedido3))
    print('-Valor a Pagar:               R${}'.format(deve_pagar))
