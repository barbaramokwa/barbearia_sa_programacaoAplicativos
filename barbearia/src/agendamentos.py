import mysql.connector
from banco import conectar
from models import Agendamento


def cadastrar_agendamento(agendamento):
    conexao = None
    cursor = None
    try:
        conexao = conectar()
        cursor = conexao.cursor()

        sql = "INSERT INTO agendamento (nome, email, telefone) VALUES (%s, %s, %s)"
        cursor.execute(sql, agendamento.converte_tupla())

        conexao.commit()
        print(f"'{agendamento.nome}' cadastrado com sucesso!")
    except mysql.connector.Error as erro:
        print(f"Erro ao cadastrar agendamento: {erro}")
    finally:
        if cursor:
            cursor.close()
        if conexao and conexao.is_connected():
            conexao.close()


def listar_agendamentos():
    conexao = None
    cursor = None
    lista_agendamentos = []
    try:
        conexao = conectar()
        cursor = conexao.cursor()

        sql = "SELECT id, nome, email, telefone FROM clientes ORDER BY nome ASC"
        cursor.execute(sql)
        registros = cursor.fetchall()

        for tupla in registros:
            agen = Agendamento.reverte_tupla(tupla)
            lista_agendamentos.append(agen)

    except mysql.connector.Error as erro:
        print(f"Erro ao listar agendamentos: {erro}")
    finally:
        if cursor:
            cursor.close()
        if conexao and conexao.is_connected():
            conexao.close()

    return lista_agendamentos


def buscar_por_id(id):
    conexao = None
    cursor = None
    agendamento = None
    try:
        conexao = conectar()
        cursor = conexao.cursor()

        sql = "SELECT id, nome, email, telefone FROM clientes WHERE id = %s"
        cursor.execute(sql, (id,))
        registro = cursor.fetchone()

        if registro:
            cliente = Agendamento.reverte_tupla(registro)

    except mysql.connector.Error as erro:
        print(f"Erro ao buscar cliente: {erro}")
    finally:
        if cursor:
            cursor.close()
        if conexao and conexao.is_connected():
            conexao.close()

    return cliente