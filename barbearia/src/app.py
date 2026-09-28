from flask import Flask, render_template
from agendamentos import listar_agendamentos, buscar_agendamento, listar_por_status

app = Flask(__name__)

@app.route('/')
def index():
    lista = listar_agendamentos()
    return render_template('index.html', agendamentos=lista)

@app.route('/agendamentos')
def ver_agendamentos():
    lista = listar_agendamentos()
    return render_template('agendamentos.html', agendamentos=lista, filtro_atual="Todos")

@app.route('/agendamentos/status/<status>')
def ver_agendamentos_por_status(status):
    lista = listar_por_status(status)
    return render_template('agendamentos.html', agendamentos=lista, filtro_atual=status)

@app.route('/agendamento/<int:id>')
def ver_detalhe(id):
    agendamento = buscar_agendamento(id)
    return render_template('detalhe.html', agendamento=agendamento)

if __name__ == '__main__':
    app.run(debug=True)