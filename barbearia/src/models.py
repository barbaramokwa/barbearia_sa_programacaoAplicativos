class Agendamento:
    def __init__(self, cliente, telefone, servico, preco, barbeiro, data, horario, status):
        self.id = id
        self.cliente = cliente
        self.telefone = telefone
        self.servico = servico
        self.preco = preco
        self.barbeiro = barbeiro
        self.data = data
        self.horario = horario
        self.status = status

    def exibir(self):
        print(f"ID: {self.id}, Cliente: {self.cliente}, Telefone: {self.telefone}, Serviço: {self.servico}, Preço: R${self.preco}, Barbeiro: {self.barbeiro}, Data: {self.data}, Horario: {self.horario}, Status: {self.status}")

    def converte_tupla(self):
        return (self.cliente, self.telefone, self.servico, self.preco, self.barbeiro, self.data, self.horario, self.status)

