class Agendamento:
    def __init__(self, cliente, telefone, servico, preco, barbeiro, data, horario, status='Agendado', id=None):
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
        """Retorna os dados do agendamento formatados em uma única linha."""
        return f"ID: {self.id} | Cliente: {self.cliente} | Serviço: {self.servico} | Barbeiro: {self.barbeiro} | Data: {self.data} {self.horario} | R$ {self.preco:.2f} | Status: {self.status}"

    def converte_tupla(self):
        """Converte o objeto Agendamento em uma tupla para persistência."""
        return (self.id, self.cliente, self.telefone, self.servico, self.preco, self.barbeiro, self.data, self.horario, self.status)

    @staticmethod
    def reverte_tupla(tupla):
        """Recebe uma tupla vinda do banco de dados e constrói uma instância de Agendamento."""
        if not tupla:
            return None
        return Agendamento(
            id=tupla[0],
            cliente=tupla[1],
            telefone=tupla[2],
            servico=tupla[3],
            preco=float(tupla[4]) if tupla[4] is not None else 0.0,
            barbeiro=tupla[5],
            data=str(tupla[6]),
            horario=str(tupla[7]),
            status=tupla[8]
        )