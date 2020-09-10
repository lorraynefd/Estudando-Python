class contacorrente:
    nomecliente = None
    numconta = None
    saldo = None
    lnome = []
    lconta = []
    lsaldo = []

    def adicionardados(self):
        while True:
            self.nomecliente = input('Digite o nome do cliente: ')
            if self.nomecliente == '':
                break
            self.lnome.append(self.nomecliente)

            self.numconta = int(input('Digite o número da conta: '))
            self.lconta.append(self.numconta)

            self.saldo = int(input('Digite seu saldo:  '))
            self.lsaldo.append(self.saldo)

            print('_' * 30)

    def mostrardados(self):
        print(self.lnome)
        self.nome = input('qual cliente voçê quer ver o dados: ')
        self.local = self.lnome.index(self.nome)
        print('O cliente {}, conta número {}, tem R${} de saldo'.format(self.lnome[self.local], self.lconta[self.local], self.lsaldo[self.local]))
        print('_' * 30)

    def depositar(self):
        print(self.lnome)
        self.nomedepo = input(' na conta de qual cliente voçê quer fazer o deposito: ')
        self.localdepo = self.lnome.index(self.nomedepo)
        self.saldo2 = int(input('Digite quanto voçê quer depositar: '))
        print('O novo saldo do cliente {} é de R${}.00'.format(self.nomedepo, self.saldo2 + self.lsaldo[self.localdepo]))
        print('_' * 30)

    def sacar(self):
        print(self.lnome)
        self.nomesaque = input('na conta de qual cliente voçê deseja fazer o saque: ')
        self.localsaque = self.lnome.index(self.nomesaque)
        self.saque = int(input('Digite quanto voçê quer sacar: '))
        if self.saque < self.saldo2 + self.lsaldo[self.localdepo]:
            print('Seu saque foi de R${}.00, agora voçê tem R${}.00'.format(self.saque, self.saldo2 + self.lsaldo[self.localsaque] - self.saque))
        else:
            print('voçê não pode sacar esse tanto, porque voçê não tem BB')

conta = contacorrente()
conta.adicionardados()
conta.mostrardados()
conta.depositar()
conta.sacar()
#######################
class contapoupanca:
    def imprimir(self):
        self.dinheiro = int(input('Digite seu saldo:'))
        print('Seu saldo é de R${}.00'.format(self.dinheiro))
    def depositar(self):
        self.saldo3 = int(input('Digite quanto voçê quer depositar(com correção de 0,5%):'))
        co = self.saldo3*0.5/100
        print('Seu saldo era de R${}.00, com a correção, agora é R${}'. format(self.dinheiro ,self.dinheiro + co))

conta1 = contapoupanca()
conta1.imprimir()
conta1.depositar()

class funcionarios:
    nome = None
    cpf = None
    salario = None
    def mostrardados(self):
        self.nome = input('Digite seu nome: ')
        self.cpf = int(input('Digite seu CPF: '))
        self.salario = int(input('Digite seu salario: '))
        print('{} de CPF: {}, recebe R${} '.format(self.nome, self.cpf, self.salario))
    def calcular(self):
        if self.salario <= 1000:
            comissao = self.salario*15/100
            print('A comissao é: R${}'.format(comissao))
        elif self.salario >= 1000:
            comissao = self.salario*10/100
            print('A comissao é: R${}'.format(comissao))
f = funcionarios()
f.mostrardados()
f.calcular()

class gerente:
    salariog = None
    def calcular(self):
        self.salariog = int(input('Salario do gerente: '))
        if self.salariog <= 3000:
            comissaog = self.salariog*20/100
            print('a comissão do gerente é R${}'.format(comissaog))
        else:
            comissaog = self.salariog*15/100
            print('a comissão do gerente é R${}'.format(comissaog))
g = gerente()
g.calcular()