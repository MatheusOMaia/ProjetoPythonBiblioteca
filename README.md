# Sistema de Biblioteca em Python

## Descrição

Este projeto consiste em um sistema de gerenciamento de biblioteca desenvolvido em Python, com o objetivo de controlar o cadastro de livros, usuários, empréstimos e devoluções.

---

## Funcionalidades

* Cadastro de livros
* Cadastro de usuários
* Realização de empréstimos
* Registro de devoluções
* Listagem de livros, usuários e empréstimos
* Controle de disponibilidade e atraso

---

## Estrutura do Projeto

```
ProjetoPython/
│
├── livro.py
├── usuario.py
├── emprestimo.py
├── biblioteca.py
└── main.py
```

---

## Tecnologias Utilizadas

* Python 3.x
---

## Como Executar

1. Clone o repositório:

```
git clone https://github.com/seu-usuario/sistema-biblioteca.git
```

2. Acesse a pasta do projeto:

```
cd sistema-biblioteca
```

3. Execute o programa:

```
python main.py
```

---

## Uso do Sistema

Ao executar o sistema, será exibido um menu interativo no terminal com as opções:

```
1. Cadastrar Livro
2. Cadastrar Usuário
3. Listar Livros
4. Listar Usuários
5. Realizar Empréstimo
6. Devolver Livro
7. Listar Empréstimos
0. Sair
```

Basta digitar o número da opção desejada.

---

## Regras de Negócio

* Um livro só pode ser emprestado se estiver disponível
* Ao ser emprestado, o livro fica indisponível
* Ao ser devolvido, o livro volta a ficar disponível
* O sistema controla prazos de devolução e atrasos

---

## Melhorias Futuras

* Persistência de dados (SQlite)

---

## Autor

* Matheus Maia
