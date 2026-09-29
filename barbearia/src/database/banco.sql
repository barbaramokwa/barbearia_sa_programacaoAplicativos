create database	barbearia;
use barbearia;

create table agendamentos(
	id int auto_increment primary key,
    cliente varchar(100) not null,
    telefone varchar(20),
    servico varchar(100),
    preco decimal(10,2),
    barbeiro varchar(50),
    data date not null,
    horario varchar(5),
    status varchar(20) default 'Agendado'
);

insert into agendamentos (cliente, telefone, servico, preco, barbeiro, data, horario, status)
values 
	('João Silva', '48999990001', 'Corte Masculino', 35.00, 'Carlos', '2026-09-11', '09:00', 'Agendado'),
    ('Pedro Santos', '48999990002', 'Barba', 25.00, 'Marcos', '2026-09-11', '10:30', 'Concluído'),
    ('Lucas Oliveira', '48999990003', 'Corte + Barba', 55.00, 'Carlos', '2026-09-12', '14:00', 'Agendado'),
    ('Gabriel Souza', '48999990004', 'Corte Masculino', 35.00, 'Rafael', '2026-09-12', '15:30', 'Cancelado'),
    ('Matheus Costa', '48999990005', 'Corte + Barba', 55.00, 'Marcos', '2026-09-13', '09:30', 'Concluído'),
    ('Felipe Almeida', '48999990006', 'Barba', 25.00, 'Rafael', '2026-09-13', '11:00', 'Agendado'),
    ('André Martins', '48999990007', 'Corte Masculino', 35.00, 'Carlos', '2026-09-14', '16:00', 'Agendado'),
    ('Bruno Ferreira', '48999990008', 'Corte + Barba', 55.00, 'Rafael', '2026-09-15', '18:00', 'Agendado')
    ('Barbara Linda', '476767676767', 'Corte+Hidratação', 150.67, 'Marcos', '2026-09-22', '18:32', 'Concluido');