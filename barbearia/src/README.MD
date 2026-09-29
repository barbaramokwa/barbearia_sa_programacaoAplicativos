==================================================
SISTEMA DE AGENDAMENTOS - BARBEARIA NAVALHA DE OURO
Curso Técnico em Desenvolvimento de Sistemas
Unidade Curricular: Programação de Aplicativos
Docente: Lucas Grandeaux
==================================================

INTEGRANTES DO TRIO:
1. [Nome do Integrante 1]
2. [Nome do Integrante 2]
3. [Nome do Integrante 3]

REQUISITOS MÍNIMOS:
- Python 3.x
- MySQL Server e MySQL Workbench
- Biblioteca mysql-connector-python (`pip install mysql-connector-python`)
- Framework Flask (`pip install Flask`)

INSTRUÇÕES PARA EXECUÇÃO:

1. CONFIGURAÇÃO DO BANCO DE DADOS:
   - Abra o MySQL Workbench.
   - Execute o script `banco.sql` fornecido para criar o banco de dados `barbearia`, 
     a tabela `agendamentos` e realizar as inserções iniciais.

2. CONFIGURAÇÃO DE CREDENCIAIS:
   - Abra o arquivo `config.py` e insira a senha do seu usuário `root` do MySQL.

3. EXECUÇÃO DA APLICAÇÃO:
   - Abra o terminal na pasta do projeto `barbearia/`.
   - Execute o comando:
     python app.py
   - Acesse o navegador no endereço informada no terminal (ex: http://127.0.0.1:5000).