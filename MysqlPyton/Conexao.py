import mysql.connector

usuario = 'root'
senha = ''
servidor = 'localhost'
nomebanco = 'aula_salomao'

conexao = mysql.connector.connect(user=usuario, password=senha, host=servidor, database=nomebanco)

comando = conexao.cursor()

query = 'SHOW TABLES'

comando.execute(query)
for tabelas in comando:
    print(tabelas)

conexao.close()

ATIVIDADE 1

import mysql.connector

usuario = 'root'
senha = ''
servidor = 'localhost'
nomebanco = 'escola'

conexao = mysql.connector.connect(user=usuario, password=senha, host=servidor, database=nomebanco)
comando = conexao.cursor()
query = 'SHOW TABLES'
query = "insert into aluno (nome, idade, materia) values ('andre', 20, 'fisica')"
query2 = "update aluno set nome = 'lud' where id_aluno = 1"
query3 = 'delete from aluno where id_aluno = 1'

comando.execute(query)
comando.execute(query2)
comando.execute(query3)
conexao.commit()






import mysql.connector


class Conexao:
    usuario = "root"
    senha = ""
    servidor = "localhost"
    nomebanco = "aula_salomao"

    def conectar(self):
        try:
            self.conexao = mysql.connector.connect(user=self.usuario, password=self.senha,host=self.servidor, database=self.nomebanco)
            print("oba!conectou...")
            self.cursor = self.conexao.cursor()
        except Exception as erro:
            print("Ops, não conectou.", erro)

    def consultar_tabelas(self):
        comando = ("SHOW TABLES")
        self.cursor.execute(comando)
        for tabela in self.cursor:
            print(tabela)

    def consultar(self, nometabela):
        # cursor=self.conexao.cursor()
        comando = ("SELECT * FROM {}".format(nometabela))
        self.cursor.execute(comando)
        for consulta in self.cursor:
            print(consulta)

    def inserir(self):
        comando = ("insert into aluno (ALUNO) VALUES ('Josiqueison Ericlisberto')")
        self.cursor.execute(comando)
        self.conexao.commit()

    def alterar(self):
        comando = ("update aluno set ALUNO ='Josiqueison Ericlisberto Nunes' where ID=36")
        self.cursor.execute(comando)
        self.conexao.commit()

    def deletar(self):
        comando = ("DELETE FROM aluno where ID=36")
        self.cursor.execute(comando)
        self.conexao.commit()

    def fechar_conexao(self):
        self.conexao.close()

        # update aluno set ALUNO ='Alberto Roberto' where ID=34


c = Conexao()
c.conectar()
c.consultar_tabelas()
c.consultar('unidade')
c.fechar_conexao()

Mysql e Python.py
Exibindo atividade - POO.py.