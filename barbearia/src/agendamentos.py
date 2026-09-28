import mysql.connector
from banco import conectar
from models import Agendamento

def listar_agendamentos():
    conexao = None
    cursor = None
    lista = []
    try:
        conexao = conectar()
        cursor = conexao.cursor()
        sql = "SELECT id, cliente, telefone, servico, preco, barbeiro, data, horario, status FROM agendamentos ORDER BY data ASC, horario ASC"
        cursor.execute(sql)
        resultados = cursor.fetchall()
        for linha in resultados:
            lista.append(Agendamento.reverte_tupla(linha))
    except mysql.connector.Error as erro:
        print(f"Erro ao listar agendamentos: {erro}")
    finally:
        if cursor:
            cursor.close()
        if conexao and conexao.is_connected():
            conexao.close()
    return lista

def buscar_agendamento(id_agendamento):
    conexao = None
    cursor = None
    agendamento = None
    try:
        conexao = conectar()
        cursor = conexao.cursor()
        sql = "SELECT id, cliente, telefone, servico, preco, barbeiro, data, horario, status FROM agendamentos WHERE id = %s"
        cursor.execute(sql, (id_agendamento,))
        linha = cursor.fetchone()
        if linha:
            agendamento = Agendamento.reverte_tupla(linha)
    except mysql.connector.Error as erro:
        print(f"Erro ao buscar agendamento ID {id_agendamento}: {erro}")
    finally:
        if cursor:
            cursor.close()
        if conexao and conexao.is_connected():
            conexao.close()
    return agendamento

def listar_por_status(status):
    conexao = None
    cursor = None
    lista = []
    try:
        conexao = conectar()
        cursor = conexao.cursor()
        sql = "SELECT id, cliente, telefone, servico, preco, barbeiro, data, horario, status FROM agendamentos WHERE status = %s ORDER BY data ASC, horario ASC"
        cursor.execute(sql, (status,))
        resultados = cursor.fetchall()
        for linha in resultados:
            lista.append(Agendamento.reverte_tupla(linha))
    except mysql.connector.Error as erro:
        print(f"Erro ao listar agendamentos por status '{status}': {erro}")
    finally:
        if cursor:
            cursor.close()
        if conexao and conexao.is_connected():
            conexao.close()
    return lista