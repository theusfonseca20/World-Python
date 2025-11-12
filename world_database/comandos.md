<p align="center">
  <img src="https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExZnd2NGVoMWJ4NzZjOXBycTdpamR1YWduMDhwYnZhcmxzbmcxdXRvdCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/xTiTnxpQ3ghPiB2Hp6/giphy.gif" alt="Database GIF" width="200" style="margin-bottom: 20px;"/>
</p>

<h1 align="center">⚙️ Comandos SQL e Utilitários Postgres 🐘</h1>

<p align="center">
  Um guia rápido com comandos essenciais de <strong>SQL (DDL)</strong> para manipulação da estrutura do banco <br>
  e comandos úteis do terminal <strong>Postgres (psql)</strong> para navegação.
</p>

---

### 🚀 Comandos SQL (Linguagem de Definição de Dados - DDL)

Estes comandos manipulam a *estrutura* do banco de dados (bancos, tabelas, colunas).

#### 1. Gerenciando Bancos de Dados
* **Criando um banco de dados:**
    ```sql
    CREATE DATABASE nome_banco;
    ```
* **Renomeando um banco de dados:**
    ```sql
    ALTER DATABASE meu_primeiro_database RENAME TO teste_database;
    ```
* **Excluindo um banco de dados (PERMANENTEMENTE):**
    ```sql
    DROP DATABASE meu_primeiro_database;
    ```

#### 2. Criando Tabelas
* **Criando uma tabela de `clientes`:**
    ```sql
    CREATE TABLE clientes (
        id SERIAL PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        phone VARCHAR(20) NOT NULL,
        email VARCHAR(100) UNIQUE
    );
    ```
    * **Explicação:** Tabela `clientes` com 4 colunas. O `id` é uma chave primária sequencial (`SERIAL`). `name`, `phone` e `email` são `VARCHAR` (textos).

#### 3. Alterando Tabelas (Modificando Estruturas)
* **Adicionando uma nova coluna `birthday` (aniversário):**
    ```sql
    ALTER TABLE clientes ADD COLUMN birthday DATE;
    ```
* **Obrigando o `email` a ser `NOT NULL` (não-nulo):**
    ```sql
    ALTER TABLE clientes ALTER COLUMN email SET NOT NULL;
    ```
* **Removendo a obrigatoriedade do `phone` (pode ser nulo):**
    ```sql
    ALTER TABLE clientes ALTER COLUMN phone DROP NOT NULL;
    ```
* **Renomeando uma coluna (de `phone` para `telefone`):**
    ```sql
    ALTER TABLE clientes RENAME COLUMN phone TO telefone;
    ```
* **Excluindo uma coluna (removendo `birthday`):**
    ```sql
    ALTER TABLE clientes DROP COLUMN birthday;
    ```

---

### 🐘 Comandos do Terminal Postgres (Utilitários `psql`)

Estes comandos são atalhos usados *dentro* do terminal `psql` e não fazem parte da linguagem SQL.

1.  **`\l`** (List): Lista todos os bancos de dados disponíveis no seu servidor.
2.  **`\c nome_do_banco`** (Connect): Se conecta a um outro banco de dados.
3.  **`\d`** (Describe): Lista todas as tabelas (e outras relações) no banco de dados atual.
4.  **`\q`** (Quit): Sai do terminal `psql` e volta ao seu terminal comum.

---
