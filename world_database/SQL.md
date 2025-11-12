-- Conhecendo a linguagem SQL

-- Criada na decada de 1970 pela IBM e posteriormente padronizada pela ANSI e ISO
-- SQL (Structured Query Language) é a linguagem padrão utilizada para gerenciar e manipular dados relacionais
-- Serve para criação de tabelas, inserção de dados, consultas e manipualções de dados, gerencimanetos de acesso, etc.
-- Exemplos de comando SQL -> CREATE DATABASE Clientes; (criando um banco) | SELECT nome, telefone, FROM Clientes; (pegando as tabelas nome e telefone da tabela clientes)

-- Categorias de comandos da linguagem sql
-- DDL (Data Definition Language)-> comando para definir a estrutura do banco de dados (criação, alteração e exclusão de tabelas)  | CREATE TABLE, ALTER TABLE, DROP TABLE
-- DML (Data Manipulation Language) -> Comandos para manipular dados (pegar informações do banco, inserir dados, atualizar e deletar dados) | SELECT, INSERT, UPDATE, DELETE
-- DCL (Data Control Language) -> Comandos para controlar o acesso aos dados | GRANT, REVOKE
-- TCL (Transaction Control Language) -> Comandos para gerenciar transações (conjuntos de comandos que dependem uns dos outros) | BEGIN, COMMIT, ROLLBACK
