   Q1
print('Alo mundo')

   Q2
nº1=int(input('Digite um valor: '))
nº2=int(input('Digite outro valor: '))
som=nº1+nº2
print('A soma de {} mais {} é igual a {}'.format(nº1,nº2,som))

   Q3
nº1=int(input('Digite uma nota: '))
nº2=int(input('Digite uma nota: '))
nº3=int(input('Digite uma nota: '))
nº4=int(input('Digite uma nota: '))
med=(nº1+nº2+nº3+nº4)/4
print('A media das notas é igual á {}'.format(med))

   Q4
metro=float(input('Digite uma quantidade em metros: '))
converção=metro*100
print('{} metros corespone a {} centimetros'.format(metro,converção))

   Q5
raio=float(input('Digite o raio da circunferencia:'))
atO=3.14*raio**2
print('A área da circunferencia é igual a {}'.format(atO))

   Q6
aresta=float(input('Digite a aresta do quadrado:  '))
atquadrado=aresta*aresta
dobro=atquadrado*2
print('A área de quadado é {} e o dobro deça é {}'.format(atquadrado,dobro))

   Q7
dias_segundos=int(input('Digite quantos dias: '))
horas_segundos=int(input('Digite quantas horas: '))
minutos_segundos=int(input('Digite quantos minutos: '))
segudos_segundos=int(input('Digite quatos segundos: '))
converção1=minutos_segundos*60
converção2=horas_segundos *3600
converção3=dias_segundos*86400
som=converção1+converção2+converção3+segudos_segundos
print('Você ficou cerca de {} segundos'.format(som))

   Q8
distância=float(input('Digite a distâcia percorrida: '))
velocidade_média=float(input('Digite a velocidade média: '))
tempo=distância/velocidade_média
print('O tempo gasto sera de {}'.format(tempo))

   Q9
graus_celsius=float(input('Digite a temperatura em °C: '))
converção=graus_celsius*1.8+32
print('{}°C equivalem a {}°F'.format(graus_celsius,converção))

   Q10
graus_F=float(input('Digite a temperatura em °F: '))
converção=(graus_F-32)*5/9
print('{}°F equivalem a {}°C'.format(graus_F,converção))

   #Q11
q_cigarros=int(input('Quantidade de cigarros fumados: '))
q_anos=int(input('Quantos anos você fumou: '))
converção1= q_anos*365
converção2=converção1*10
converção3=converção2/60/24
print('Você perdeu {} dias de vida'.format(converção3))

   Q12
ganha_H=float(input('Quanto vc ganha or hora trabalhada: '))
horas_mês=float(input('Quantas horas vc trabalha por mês: '))
conta1=ganha_H*horas_mês
print('Vc ganha por mês {} reais '.format(conta1))

   Q13
n1=int(input('Digite um número inteiro: '))
n2=int(input('Digite um número inteiro: '))
n3=float(input('Diguite um número real: '))
conta1=n1*2*n2/2
conta2=n1*3+n3
conta3=n3*n3*n3
print('O dobro do primeiro número com a metade do segundo é {}'.format(conta1))
print('A soma do triplo primeiro com o terceiro é {}'.format(conta2))
print('O terceiro número elevado ao cubo {}'.format(conta3))

  Q14
altura=float(input('Qual é a sua altura: '))
conta=(72.7*altura)-58
print('O peso ideal para vc é {}'.format(conta))

   Q15
ganha_h=float(input('Quanrto vc ganha por hora: '))
horas_mês=float(input('quabtas horas por mês: '))
conta1=ganha_h*horas_mês
conta2_inss=conta1*0.08
conta3_sind=conta1*0.05
conta4_ir=conta1*0.11
conta5=conta2_inss+conta3_sind+conta4_ir
conta6=conta1-conta5
print("       Contra Cheque")
print('+ Salário Bruto     :R$ {}'.format(conta1))
print('- IR (11%)          :R$ {}'.format(conta4_ir))
print('-INSS (8%)          :R$ {}'.format(conta2_inss))
print('-Sindicato          :R$ {}'.format(conta4_ir))
print('=Salário liquido    :R$ {}'.format(conta6))

   Q16
metros_quadrado=int(input('Quanos metros quadrados tem de ser pintados: '))
conta1=metros_quadrado/3/18
conta2=conta1*80.00
print('Você ira usar {} de latas de tinta que custara {}R$'.format(conta1,conta2))