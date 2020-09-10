nome = 'Ana','Cintia','Bia','Denis'
print(nome[1])

numero = (10,5),(20,7)
print(numero [0])

numerais = (5,3,55,2,4,65,96,822,1040,325)
print(sorted(numerais))
print(sum(numerais))
print(max(numerais))
print(min(numerais))
print(len(numerais))
total = sum(numerais)
quantidade = len(numerais)
media = total/quantidade
print(media)

ATIVIDADE

1º LISTA

nome = ('douglas'),('andre'),('ludmila'),('milard'),('lucas')
print(nome[3])

liprint(lista[1][1])

numeros = (11,22,33,44,55,66)
print(sum(numeros))
print(max(numeros))
print(min(numeros))
print(len(numeros))
soma = sum(numeros)
quant = len(numeros)
media = soma/quant
print(media)

2º LISTA

lista = []
for i in range(5):
    lista.append(int(input('digite um numero: ')))
print(max(lista))
print(min(lista))
print(sum(lista))
soma = sum(lista)
quant = len(lista)
media = soma/quant
print(media)

lista = []
for i in range(6):
    lista.append(input('digite uma letra: '))
print(lista)
print(sorted(lista))
print(lista[0])
print(lista[5])
lista.pop(0)
lista.insert(0,'w')
lista.insert(7,'z')
print(lista)
print(sorted(lista))

nomes = []
for i in range(4):
    nomes.append(input('digite um nome: '))
print(nomes)
print(sorted(nomes))

letras = []
vogais = []
consoantes = []
for i in range(6):
    letras.append(input('digite uma letra: '))

for i in range(6):
    if (letras[i]) == 'a' or (letras[i]) == 'e' or (letras[i]) == 'i' or (letras[i]) == 'o' or (letras[i]) == 'u':
        vogais.append(letras[i])
    else:
        consoantes.append(letras[i])
print(letras)
print(vogais)
print(consoantes)sta = ('aa','bb','zz'),('kk','cc','dd'),('oo','ee','ff')

lista = []
par = []
impar = []
for i in range(6):
    lista.append(int(input('digite um numero: ')))
for i in range(6):
    if lista[i] %2==0:
        par.append(lista[i])
    else:
        impar.append(lista[i])
print(lista)
print(par)
print(impar)

letras = []
numeros = []
lista = ('b',4,7,'a'),(2,'f',8,'q'),(2,5,'c','n'),('h','y',1,'w')
for i in range(4):
    for j in range(4):
        if type (lista[i][j]) == int:
            numeros.append(lista[i][j])
        else:
            letras.append(lista[i][j])
print(sorted(numeros))
print(sorted(letras))

par = []
impar = []
total = []
for i in range(6):
    total.append(int(input('digite um numero: ')))
    if (total[i])%2==0:
        par.append(total[i])
    else:
        impar.append(total[i])
print(len(total))
print(sum(total))
print(len(par))
print(len(impar))

class pessoa():
    nome = None
    idade = None
    def andar(self):
        print('a pessoa andou')
pessoa1 = pessoa()
pessoa.nome = 'Douglas'
pessoa1.idade = 17
pessoa1.andar()

class calculo():
    x = None
    y = None
    def calcular(self, x, y):
        print(x+y)
calculo1 = calculo()
calculo1.calcular(8,8)

class pessoa():
    nome = None
    idade = None
    sexo = None
    def falar (self):
        print('a pessoa {} falou'.format(self.nome))
        print('o {} tem {} anos de idade'.format(self.nome, self.idade))
pessoa1 = pessoa()
pessoa1.nome = 'Douglas'
pessoa1.idade = 17
pessoa1.falar()

3° LISTA

class pessoa():
    nome = None
    idade = None
    sexo = None
    def imprimir(self):
        self.nome = input('digite o nome: ')
        self.idade = input('digite a idade: ')
        self.sexo = input('digite o sexo: ')
        print('seu nome é {}, sua idade é {}, seu sexo é {}'.format(self.nome, self.idade, self.sexo))
    def falar(self):
        print('a pessoa {} falou'.format(self.nome))

pessoa = pessoa()
pessoa.imprimir()
pessoa.falar()

class carro():
    marca = None
    modelo = None
    cor = None
    def imprimir(self):
        self.marca = input('marca do carro: ')
        self.modelo = input('modelo do carro: ')
        self.cor = input('cor do carro: ')
        print('a marca do carro é: {}, o modelo: {}, e a cor é: {}'.format(self.marca,self.modelo,self.cor))
    def ligar(self):
        print('seu carro ligou')
    def acelerar(self):
        print('seu carro acelerou')
    def parar(self):
        print('seu carro parou')
    def desligar(self):
        print('seu carro desligou')

carro = carro()
carro.imprimir()
carro.ligar()
carro.acelerar()
carro.parar()
carro.desligar()


class calculo():
    x = None
    y = None
    def calcular(self, x, y):
        print(x+y)
        print(x-y)
        print(x*y)
        print(x/y)
calculo1 = calculo()
calculo1.calcular(5,8)


class aprovacao():
    aluno = None
    disciplina = None
    nota = None
    def imprimir(self, aluno, disciplina, nota):
        self.aluno = aluno
        self.disciplina = disciplina
        self.nota = nota
        print(self.aluno, self.disciplina, self.nota)
        if self.nota >= 6:
            print('aprovado')
        else:
            print('reprovado')
a = aprovacao()
a.imprimir('douglas','matematica',7)


class carro:
    def __init__(self, marca, modelo, cor):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        print(self.marca, self.modelo, self.cor)
cor = carro('fiat', 'uno', 'azul')



