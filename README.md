# PYSQL - Sistema de Monitoramento de Clientes / Client Management System

Este projeto foi desenvolvido como parte do curso **"Desenvolvendo um Projeto Completo Python com Estruturas de Dados"**, ofertado pela Fundação Bradesco.  
A aplicação conecta-se ao banco de dados **SQLite** e permite realizar operações de CRUD (Create, Read, Update, Delete) para monitorar dados de clientes.

This project was developed as part of the course **"Developing a Complete Python Project with Data Structures"**, offered by Fundação Bradesco.  
The application connects to an **SQLite** database and allows CRUD operations (Create, Read, Update, Delete) to manage client data.

---

## 📖 Descrição do Curso / Course Description

**PT-BR:**  
No curso, aprendemos sobre:
- Principais bibliotecas de código aberto em Python.
- Bancos de dados relacionais e a linguagem de consulta **SQL**.
- Importância do modelo Entidade-Relacionamento na estrutura de um banco de dados.
- Criação e manipulação de tabelas via **SQLite Studio** e consultas SQL.
- Exercícios práticos para consolidar o aprendizado.

**EN:**  
In the course, we learned about:
- Main open-source Python libraries.
- Relational databases and the **SQL** query language.
- Importance of the Entity-Relationship model in database design.
- Creating and manipulating tables using **SQLite Studio** and SQL queries.
- Practical exercises to consolidate learning.

---

## 🎯 Objetivo da Aplicação / Application Goal

**PT-BR:**  
O sistema foi criado para:
- Cadastrar clientes com informações de **Nome, Sobrenome, Email e CPF**.
- Utilizar o **CPF como chave primária** para garantir unicidade dos registros.
- Permitir consultas, atualizações e exclusões de clientes de forma simples e eficiente.
- Oferecer uma interface gráfica amigável para interação com o banco de dados.

**EN:**  
The system was designed to:
- Register clients with **Name, Surname, Email, and CPF** information.
- Use **CPF as the primary key** to ensure record uniqueness.
- Allow queries, updates, and deletions of clients in a simple and efficient way.
- Provide a user-friendly graphical interface for database interaction.

---

## 🛠️ Tecnologias Utilizadas / Technologies Used

- **Python 3.13** → Main programming language.  
- **Tkinter** → GUI library for building the frontend interface.  
- **SQLite** → Lightweight relational database for storing client data.  
- **SQL** → Query language for database manipulation.  
- **MVC-like Structure** →  
  - `frontend.py`: Graphical interface.  
  - `backend.py`: Database connection and queries.  
  - `application.py`: Integration layer connecting frontend and backend.  

---

## ⚙️ Funcionalidades / Features

- **Adicionar Cliente / Add Client**  
- **Visualizar Todos / View All Clients**  
- **Buscar Cliente / Search Client**  
- **Atualizar Cliente / Update Client**  
- **Deletar Cliente / Delete Client**  
- **Interface Gráfica / Graphical Interface**  

---

## 🚀 Como Executar / How to Run

**PT-BR:**
```bash
git clone https://github.com/laissarosa/pysql-client-manager.git
cd pysql-client-manager
python aplication.py
