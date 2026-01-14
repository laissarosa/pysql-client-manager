import sqlite3 as sql

class TransactionObject:
    database = "clients.db"
    conn = None
    cur = None
    is_connected = False

    def connect(self):
        TransactionObject.conn = sql.connect(TransactionObject.database)
        TransactionObject.cur = TransactionObject.conn.cursor()
        TransactionObject.is_connected = True

    def disconnect(self):
        TransactionObject.conn.close()
        TransactionObject.is_connected = False

    def execute(self, sql_query, params=None):
        if TransactionObject.is_connected:
            if params is None:
                TransactionObject.cur.execute(sql_query)
            else:
                TransactionObject.cur.execute(sql_query, params)
            return True
        return False

    def fetchall(self):
        return TransactionObject.cur.fetchall()

    def persist(self):
        if TransactionObject.is_connected:
            TransactionObject.conn.commit()
            return True
        return False

def initDB():
    trans = TransactionObject()
    trans.connect()
    trans.execute("""
        CREATE TABLE IF NOT EXISTS clientes (
            nome TEXT,
            sobrenome TEXT,
            email TEXT,
            cpf TEXT PRIMARY KEY
        )
    """)
    trans.persist()
    trans.disconnect()


def insert(nome, sobrenome, email, cpf):
    trans = TransactionObject()
    trans.connect()
    trans.execute("INSERT INTO clientes VALUES (?, ?, ?, ?)", (nome, sobrenome, email, cpf))
    trans.persist()
    trans.disconnect()


def view():
    trans = TransactionObject()
    trans.connect()
    trans.execute("SELECT * FROM clientes")
    rows = trans.fetchall()
    trans.disconnect()
    return rows


def search(nome='', sobrenome='', email='', cpf=''):
    trans = TransactionObject()
    trans.connect()
    trans.execute(
        "SELECT * FROM clientes WHERE nome = ? OR sobrenome = ? OR email = ? OR cpf = ?",
        (nome, sobrenome, email, cpf)
    )
    rows = trans.fetchall()
    trans.disconnect()
    return rows


def delete(cpf):
    trans = TransactionObject()
    trans.connect()
    trans.execute("DELETE FROM clientes WHERE cpf = ?", (cpf,))
    trans.persist()
    trans.disconnect()


def update(nome, sobrenome, email, cpf):
    trans = TransactionObject()
    trans.connect()
    trans.execute(
        "UPDATE clientes SET nome = ?, sobrenome = ?, email = ? WHERE cpf = ?",
        (nome, sobrenome, email, cpf)
    )
    trans.persist()
    trans.disconnect()


initDB()