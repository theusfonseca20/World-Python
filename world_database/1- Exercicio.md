<p align="center">
  <img src="https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExZnd2NGVoMWJ4NzZjOXBycTdpamR1YWduMDhwYnZhcmxzbmcxdXRvdCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/xTiTnxpQ3ghPiB2Hp6/giphy.gif" alt="Database GIF" width="200" style="margin-bottom: 20px;"/>
</p>

<h1 align="center">🍔 Script SQL: Banco de Dados da Lanchonete 🌭</h1>

<p align="center">
  Este é o script SQL original para a criação do banco de dados <strong>lanchonete_matheus</strong>. <br>
  O código abaixo reflete a primeira versão da estrutura do banco, conforme desenvolvido.
</p>

---

### 📜 Script SQL Original

O script abaixo inclui o comando de criação do banco e das tabelas `clients`, `provider`, `foods`, `orders` e `ingredients`.

```sql
CREATE DATABASE IF NOT EXISTS lanchonete_matheus;

CREATE TABLE clients (
  id SERIAL PRIMARY KEY,
  name_client VARCHAR(255) NOT NULL,
  phone VARCHAR(20),
  address VARCHAR(255),
  created_at DATE NOT NULL DEFAULT CURRENT_DATE
);

CREATE TABLE provider (
  id SERIAL PRIMARY KEY,
  name_provider VARCHAR(255) NOT NULL,
  phone VARCHAR(20) NOT NULL,
  email VARCHAR(100),
  hire_date DATE NOT NULL DEFAULT CURRENT_DATE,
  observation TEXT
  );

CREATE TABLE foods (
  id SERIAL PRIMARY KEY,
  name_food VARCHAR(255) NOT NULL,
  description TEXT,
  price DECIMAL(10,2) NOT NULL
);

CREATE TABLE orders (
  id SERIAL PRIMARY KEY,
  table_number INT NOT NULL,
  datetime_order TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  situation VARCHAR(255) NOT NULL
);

CREATE TABLE ingredients (
  id SERIAL PRIMARY KEY,
  name_ingredients VARCHAR(255) NOT NULL,
  category VARCHAR(255),
  quantity INT NOT NULL
);