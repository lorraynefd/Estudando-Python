
Q1
print('Sua nota deve ser entre 0 e 10.')
nota = float(input('Digite a sua nota:  '))
if nota<0 or nota>10:
    print('Valor invalido.')
    nota=float(input('Digite a sua nota:  '))
    print(nota)
else:
    print('Valor valido.')
    print(nota)

Q2
print('Digite  a sua usuário e sua senha.')
u=input('Usuário:  ')
s=input('Senha:  ')
if u==s:
    print('ERRO')
    u = input('Usuário:  ')

Q3
nome=input('Nome:')
while len(nome)<=3:
    print('ERRO')
    nome = input('Nome:')
idade=int(input('Idade: '))
if idade<0 or idade>150:
    print('ERRO')
    idade = int(input('Idade: '))
salario=float(input('Salário: '))
if salario<0:
    print('ERRO')
    salario=float(input('Salário: '))
sexo=input('Sexo (feminino=F),(masculina=M): ')
if sexo !='F' and sexo !='M':
    print('ERRO')
    sexo = input('Sexo (feminino=F),(masculina=M): ')
e_c=input('Estado Civil (Solteio=S),(Casado=C),(Viuvo=V),(Divorciado=D):')
if e_c !='S' and e_c !='C' and e_c !='V' and e_c!='D' :
    print('ERRO')
    e_c = input('Estado Civil (Solteio=S),(Casado=C),(Viuvo=V),(Divorciado=D):')

Q4
contador=0
a=80000
b=200000
while a < b:
    contador=contador+1
    a = a + a * 0.03
    b = b + b * 0.015
# print(contador)

Q5
contador=0
print('------diite a taxa em descimal------')
taxa_a=float(input('Qual a taxa de crecimento de do pais a?'))
taxa_b=float(input('Qual a taxa de crecimento de do pais b?'))
print('------------------------------------')
populaçao_a=int(input('Qual o numero da população de a?'))
populaçao_b=int(input('Qual o numero da população de b?'))

while populaçao_a < populaçao_b:
    contador=contador+1
    populaçao_a = populaçao_a+ populaçao_a *taxa_a
    populaçao_b = populaçao_b+ populaçao_b* taxa_b

print('Apos {} anos população do país A sera de {}  o país B sera de {}'.format(contador,populaçao_a,populaçao_b))

Q6
for i in range(1, 21):
    print(i, end=' , ')
for j in range(1, 20):
    print(j)

Q7
lista=[]
for i in range(5):
    lista.append (int(input('Digite os numeros: ')))
print('O maior numero é:')
print(max(lista))

Q8
lista=[]
for i in range(5):
    lista.append(int(input('Digite os númros:')))
print('A soma dos números é:')
print(sum(lista))
print('A media é:')
media=sum(lista)/5
print(media)

Q9
lista=[]
for i in range(1, 52):
    if i % 2 != 0:
        print('{} é impar.'.format(i))

Q10
inicio = int(input('Qual o numero inicial? '))
final = int(input('Qual o numero final? '))
for i in range(inicio + 1, final):
    print(i)

Q11
inicio = int(input('Qual o numero inicial? '))
final = int(input('Qual o numero final? '))
soma = 0
for i in range(inicio + 1, final):
    print(i)
    soma = soma + i
    print(soma)

Q12
numero=int(input('Tabuada de:'))
for j in range(1,11):
    mult= numero*j
    print('{} X {} = {}'.format(numero,j,mult))

Q13
numero=int(input('Tabuada de:'))
ini=int(input('Inicial: '))
ter=int(input('termino: '))
if ter<ini:
    print('Dados incorretos.')
elif ini<ter:
     for j in range(ini,ter+1):
        mult= numero*j
        print('{} X {} = {}'.format(numero,j,mult))

Q14
base=int(input('Digite a base:'))
expoente=int(input('Digite o expoente:'))
r=1
for i in range (expoente):
    r = r * base
print(r)

Q15
lista=[]
par=[]
impar=[]
for i in range(10):
    lista.append(int(input('Digite os números:')))
    if lista[i] % 2 == 0:
        par.append(lista[i])
    else:
        impar.append(lista[i])
print('Quantidade de numeros pares:')
print(len(par))
print('Quantidade de numeros impares:')
print(len(impar))

Q16
anterior = 1
atual = 0
futuro=anterior+atual
n=int(input('Digite o número de termos:'))
for i in range(n):
    print(futuro)
    anterior = atual
    atual = futuro
    futuro = anterior + atual

Q17
anterior = 1
atual = 0
futuro=anterior+atual
while futuro<500:
        print(futuro)
        anterior = atual
        atual = futuro
        futuro = anterior + atual

Q18
n=int(input('Digite o número de termos:'))
for i in range(1, n):
    n = n* i
    print(n)

Q19
while True:
    n=int(input('Digite o número ou zero para sair: '))
    while n > 16:
        n = int(input('Digite o número ou zero para sair: '))

    if n == 0:
        break

    for i in range(1, n):
       n = n* i
    print(n)

Q20
valor = []
n=int(input('Digite o número de termos qeu devem aparecer:'))
for i in range(n):
    valor.append(int(input('Digite o númer:')))
print('O menor valor:')
print(min(      valor))
print('O maior valor:')
print(max(      valor))
print('A soma dos valores:')
print(sum(      valor))

Q21
valor = []
n=int(input('Digite o número de termos qeu devem aparecer:'))
for i in range(n):
    val = (int(input('Digite o número:')))
    while val < 0 or val > 1000:
        print("Valor inválido.")
        val = (int(input('Digite o número:')))
    valor.append(val)

print('O menor valor:')
print(min(      valor))
print('O maior valor:')
print(max(      valor))
print('A soma dos valores:')
print(sum(      valor))

Q22
primo = 's'
n=int(input('Digite um número:'))
for i in range(2, n):
    if n % i == 0:
        primo = 'n'

if primo == 's':
    print('Primo')
else:
    print("Nao é primo")

Q23
primo = 's'
n=int(input('Digite um número:'))
for i in range(2, n):
    if n % i == 0:
        primo = 'n'
        print(i, end=',')

if primo == 's':
    print('\nPrimo')
else:
    print("\nNao é primo")

Q24
contador=0
n=int(input('Digite um número:'))
for j in range(1, n+1):
    primo = 's'
    for i in range(2, j):
        if j % i == 0:
            contador = contador + 1
            primo = 'n'
    if primo == 's':
        print('\n{} é primo.'.format(j))
        print('\n{} vezes em que foi dividido'.format(contador))
    else:
        print('\n{} NÂO é primo.'.format(j))

Q25
nota=[]
n=int(input('Quantas notas:'))
for i in  range(n):
    nota.append(int(input('Digite a nota:')))
media=sum(nota)/n
print('{}  média aritméticadas notas'.format(media))

Q26
idades=[]
alunos=int(input('Quantidade de alunos:'))
for i in range(alunos):
    idades.append(int(input('Qual a sua idade:')))
media=sum(idades)/alunos
print('Tipo da turma:')
if media>0 and media<25:
    print('Jovem')
elif media>26 and media<60:
    print('Adulta')
elif media>60:
    print('Idosa')

Q27
print('-----ELEIÇOES 2019-----')
eleitores = int(input("Quantos eleitores: "))
salomao = 0
erick = 0
paulo = 0
print('---------------------------------------')
for i in range(eleitores):
    print('Cadidatos que estão concorendo:')
    print('Candidato Salomão n°:666')
    print('Candidato Paulo   n°:777')
    print('Candidato Erick    n°:888')
    print('-----------------------------------')
    print()
    voto = int(input("Votar: "))
    if voto == 666:
        salomao +=1
    elif voto == 777:
        erick +=1
    elif voto == 888:
        paulo +=1
print('----------------------------------------')
print('{} pessoas votaram'.format(eleitores))
print('Salomão recebeu {} votos'.format(salomao))
print('Erick recebeu {} votos'.format(erick))
print('Paulo recebeu {} votos'.format(paulo))

Q28
alunos=[]
turma=int(input('Quantas turmas existem na escola: '))
for i in range(turma):
    aluno=int(input('Ha quantos alunos nas  salas:'))
    while aluno>40:
        print('A quantidade digitada de alunos em cada sala esta invalida')
        aluno=int(input('Ha quantos alunos nas  salas:'))
    alunos.append(aluno)
media=sum(alunos)/turma
print('A quantidade media de alunos por sala é de {}.'.format(media))

Q29
preco=[]
quant_cd=int(input('Quantos CDs vc tem:'))
for i in range(quant_cd):
    preco.append(float(input('Quanto custou cada  CD:')))
val_investido=sum(preco)
print('O valor investido é R${}'.format(val_investido))
media=val_investido/quant_cd
print('O valor medio gasto por CD é de R${}'.format(media))

Q30
print('Lojas Quase Dois - Tabela de preços')
for i in range(1, 51):
    print("{} - R$ {}".format(i, i * 1.99))

Q31
preco=float(input('Qual é o preço do pão?'))
for i in range(1, 51):
    print("{} - R$ {}".format(i, i * preco))

Q32
print('-----------Lojas Tabajara----------')
contador=1
total = 0
while True:
    preco=float(input('Produto {}: '.format(contador)))
    contador = contador+1
    if preco==0:
        break
    total = total + preco

print('Total:{}'.format(total))
pg=float(input('Dinheiro pago:'))
troco=pg-total
print('Troco:{}'.format(troco))

Q33

contador=1
temperaturas=[]
print('Para finalisar digite "T"')
while True:
    temperatura = (input('Temperatura {}: '.format(contador)))
    contador=contador+1
    if temperatura == 'T':
        break
    temperaturas.append(float(temperatura))
print(min(temperaturas))
print(max(temperaturas))
print(sum(temperaturas)/contador)
Q34
contador=1
print('Para finalisar digite:0')
codigo=[]
peso=[]
altura=[]
print('------------//-----------')
while True:
    teste = (int(input('Digite o seu codigo: ')))
    if teste == 0:
        break
    codigo.append(teste)
    peso.append(float(input('Seu peso: ')))
    contador=contador+1
    altura.append(float(input('Sua altura: ')))
    contador = contador + 1
    print('------------//-----------')
posicao_mina = altura.index(min(altura))
posicao_maxa = altura.index(max(altura))
posicao_maxp = peso.index(max(peso))
posicao_minp = peso.index(min(peso))
media_altura= sum(altura)/contador
media_peso= sum(peso)/contador
print('------------//-----------')
print('           ALTURA ')
print('Codigo do cliente mais alto:{}'.format(codigo[posicao_maxa]))
print('Altura  do  maior  cliente:{}'.format(max(altura)))
print('Codigo do clientie mais baixo:{}'.format(codigo[posicao_mina]))
print('Altura  do menor  cliente:{}'.format(min(altura)))
print('------------//-----------')
print('             PESO ')
print('Codigo do cliente com maior peso:{}'.format(codigo[posicao_maxp]))
print('Peso do cliente mais pesado:{}'.format(max(peso)))
print('Codigo do clientie com menor peso:{}'.format(codigo[posicao_minp]))
print('Peso do cliente menoss pesado:{}'.format(min(peso)))
print('------------//-----------')
print('             MEDIAS ')
print('A media da altura é:{}metros.'.format(media_altura))
print('A media do peso é:{}Kg.'.format(media_peso))

Q35
almento=0.015
atual=2019
ano_contrtado=int(input('Qual ano voce foi contratado? '))
salario_base=float(input('Salario base de? '))
for i in range(ano_contrtado,atual+1):
    print('Ano em que foi contratado {} salario é de:R$ {:.2f}'.format(i,salario_base))
    salario_base = salario_base + (salario_base * almento)
    almento= almento * 2

Q36
numero=[]
altura=[]
for i in range(3):
    n_aluno=int(input('Qual o numero do aluno: '))
    altura_aluno=int(input('Sua altura em centimetros: '))
    numero.append(n_aluno)
    altura.append(altura_aluno)
    print('=====================//==========================')
posicao_mina = altura.index(min(altura))
posicao_maxa = altura.index(max(altura))
print('Numero do aluno mais alto:{}'.format(numero[posicao_maxa]))
print('Altura  do  maior  aluno:{}'.format(max(altura)))
print('Numero do aluno mais baixo:{}'.format(numero[posicao_mina]))
print('Altura  do menor  aluno:{}'.format(min(altura)))

Q37
print('Estatística de acidentes de trânsito.')
cod_cidade=[]
n_vpasseio=[]
n_acidetes=[]
for i in range(5):
    codigo=int(input('Código da cidade: '))
    v_passeio=int(input('Número de veículos de passeio: '))
    acidentes=int(input(' Ìndicede acidentes: '))
    cod_cidade.append(codigo)
    n_vpasseio.append(v_passeio)
    n_acidetes.append(acidentes)
    print('=============//============')
posicao_maxaci=n_acidetes.index(max(n_acidetes))
posicao_minaci=n_acidetes.index(min(n_acidetes))
print('      Ìndice de acidentes de transito')
print('Código da cidade com maior índice de acidentes:{}'.format(cod_cidade[posicao_maxaci]))
print('Ìndice de acidentes:{}'.format(max(n_acidetes)))
print('Código da cidade com menor índice de acidentes:{}'.format(cod_cidade[posicao_minaci]))
print('Ìndice de acidentes:{}'.format(min(n_acidetes)))
print('================//================')
print('     Media de veiculos nas cidades.')
med=sum(n_vpasseio)/5
print('A media de veiculos é de {}'.format(med))
print('================//================')
soma = 0
contador = 0
for j in n_acidetes:
    if j <= 2000:
        contador += 1
        soma += i
med_acidentes= contador/soma
print('Media de acidentes nas cidades com menos de 2000 veiculos.')
print('A media de acidentes é de {}'.format(med_acidentes))

38
parcelas = 1
divida=float(input('O valor da divida: '))
juros = 0
v_divida = divida
print('---------------------------------//---------------------------------')
print('Valor da dívida     \t Valor do juros    \t N° de parcelas    \t Valor das parcelas')
print('\tR${}              \t{}%             \t{}                      \tR${:.2f}'.format(v_divida, juros,parcelas,v_divida / parcelas))
juros = 10
parcelas += 2

for j in range(4):
    v_divida = divida + (divida * juros / 100)
    print('\tR${}              \t{}%             \t{}                   \tR${:.2f}'.format(v_divida, juros, parcelas, v_divida / parcelas))
    juros += 5
    parcelas += 3

Q39
contador0=0
contador1=0
contador2=0
contador3=0
while True:
    N=int(input('diite o número: '))
    if N>=0 and N<=25:
     contador0=contador0+1
    if N>=26 and N<=50:
        contador1 = contador1 + 1
    if N>=51 and N<=75:
        contador2 = contador2 + 1
    if N>=76 and N<=100:
        contador3=contador3+1
    if N <0:
            break
print('Quantidade de numeros entre 0 e 25:')
print(contador0)
print('Quantidade de numeros entre 26 e 50:')
print(contador1)
print('Quantidade de numeros entre 51 e 75:')
print(contador2)
print('Quantidade de numeros entre 76 e 100:')
print(contador3)

Q40
contador0=0
contador1=0
contador2=0
contador3=0
contador4=0
contador5=0
print('------------------------------------------')
print('|                CARDÁOIO                |')
print('---------------------//-------------------')
print('| Especificação   |\tcódigo |\tPreço    |')
print('| Cachorro Quente |\t 100   |\tR$1.20   |')
print('| Bauru Simples   |\t 101   |\tR$1.30   |')
print('| Bauru com ovo   |\t 102   |\tR$1.50   |')
print('| Hambúrguer      |\t 103   |\tR$1.20   |')
print('| Cheeseburguer   |\t 104   |\tR$1.30   |')
print('| Refrigerante    |\t 105   |\tR$1.00   |')
print('---------------------//-------------------')
while True:
    cod=int(input('Qual o código:'))
    if cod == 0:
        break
    quant=int(input('Quantidade:'))
    if cod ==100:
        produto='Cachorro Quente'
        contador0=contador0+1*quant
        preco=quant+1*1.20
    elif cod ==101:
        produto='Bauru Simples'
        contador1=contador1+1*quant
        preco = quant * 1.30
    elif  cod ==102:
        contador2=contador2+1*quant
        preco = quant * 1.50
    elif cod == 103:
            contador3 = contador3+1 *quant
            preco = quant * 1.20
    elif cod == 104:
        contador4 = contador4+1 *quant
        preco = quant * 1.30
    elif cod == 105:
        contador5 = contador5+1*quant
        preco = quant * 1.00

print(contador0)
print(contador1)
print(contador2)
print(contador3)
print(contador4)
print(contador5)
