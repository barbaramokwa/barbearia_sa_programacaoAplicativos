import os
import sys

from flask import Flask, render_template


# ==========================================
# CAMINHO DA PASTA src
# ==========================================

base_dir = os.path.dirname(os.path.abspath(__file__))


# Garante que a pasta src esteja no caminho
# de importação do Python
if base_dir not in sys.path:
    sys.path.insert(0, base_dir)


# ==========================================
# IMPORTAÇÕES
# ==========================================

from agendamentos import (
    listar_agendamentos,
    buscar_agendamento,
    listar_por_status
)


# ==========================================
# CONFIGURAÇÃO DO FLASK
# ==========================================

app = Flask(
    __name__,
    template_folder=os.path.join(base_dir, 'templates')
)


# ==========================================
# PÁGINA INICIAL
# ==========================================

@app.route('/')
def index():

    lista = listar_agendamentos()

    return render_template(
        'index.html',
        agendamentos=lista
    )


# ==========================================
# LISTA DE AGENDAMENTOS
# ==========================================

@app.route('/agendamentos')
def ver_agendamentos():

    lista = listar_agendamentos()

    return render_template(
        'agendamentos.html',
        agendamentos=lista,
        filtro_atual='Todos'
    )


# ==========================================
# AGENDAMENTOS POR STATUS
# ==========================================

@app.route('/agendamentos/status/<status>')
def ver_agendamentos_por_status(status):

    lista = listar_por_status(status)

    return render_template(
        'agendamentos.html',
        agendamentos=lista,
        filtro_atual=status
    )


# ==========================================
# DETALHE DO AGENDAMENTO
# ==========================================

@app.route('/agendamento/<int:id>')
def ver_detalhe(id):

    agendamento = buscar_agendamento(id)

    return render_template(
        'detalhe.html',
        agendamento=agendamento
    )


# ==========================================
# EXECUTAR SERVIDOR
# ==========================================

if __name__ == '__main__':
    app.run(debug=True)