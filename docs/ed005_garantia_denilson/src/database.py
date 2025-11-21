import psycopg2

class Database:
    def __init__(self):
        try:
            self.conn = psycopg2.connect(
                dbname="app_garantia",
                user="postgres",
                password="100senha",
                host="127.0.0.1",
                port="5432"
            )
            print("Conectado ao banco com sucesso!")
        except Exception as e:
            print("Erro ao conectar ao banco:", e)
            self.conn = None

    def consultar(self, query):
        if not self.conn:
            print("Sem conexão com o banco.")
            return []
        try:
            cur = self.conn.cursor()
            cur.execute(query)
            rows = cur.fetchall()
            cur.close()
            return rows
        except Exception as e:
            print("Erro na consulta:", e)
            return []

    def fechar_conexao(self):
        if self.conn:
            self.conn.close()
            print("Conexão encerrada.")

