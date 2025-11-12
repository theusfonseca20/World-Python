<p align="center">
  <img src="https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExZnd2NGVoMWJ4NzZjOXBycTdpamR1YWduMDhwYnZhcmxzbmcxdXRvdCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/xTiTnxpQ3ghPiB2Hp6/giphy.gif" alt="Database GIF" width="200" style="margin-bottom: 20px;"/>
</p>

<h1 align="center">✍️ Comandos de Inserção de Dados (DML) 📝</h1>

<p align="center">
  Depois de criar a estrutura do banco (DDL), o próximo passo é populá-lo. <br>
  Usamos o comando <code>INSERT INTO</code>, que faz parte da <strong>Linguagem de Manipulação de Dados (DML)</strong>.
</p>

---


```sql
👤 1. Inserindo um Cliente
INSERT INTO clients (name_client, phone, address, created_at) 
Aqui, inserimos um registro na tabela `clients`. Note que a ordem dos `VALUES` deve seguir a ordem das colunas especificadas (`name_client`, `phone`, `address`, `created_at`).
  VALUES ('Matheus', '(84) 99703-8016', 'Alameda dos Bosques, 795', '2025-01-31');

🚚 2. Inserindo um Fornecedor
Inserindo um registro na tabela provider. Como a coluna hire_date tem um DEFAULT, poderíamos omiti-la, mas aqui especificamos os campos que queríamos preencher.
INSERT INTO provider (name_provider, phone, email, observation)
  VALUES ('ACME Inc.', '(11) 1111-1111', 'acme@email.com', 'Empresa terceirizada para realizar suporte de redes');

🍔 3. Inserindo um Lanche (Item do Cardápio)
Inserindo um item na tabela foods. O id não é necessário, pois a coluna SERIAL cuida disso automaticamente.
INSERT INTO foods (name_food, description, price)
  VALUES('Hamburguer', 'Pão, carne, alface, molho especial da casa', 15.50);

🥚 4. Inserindo Múltiplos Ingredientes
O INSERT permite inserir várias linhas (registros) de uma só vez, o que é muito mais eficiente. Basta separar os conjuntos de VALUES por vírgulas.
INSERT INTO ingredients (name_ingredients, category, quantity)
  VALUES
    ('Ovos', 'Diversos', 24),
    ('Presunto', 'Carnes', 14),
    ('Tomate', 'Frutas', 30);

<p align="center"> Com o banco populado, o próximo passo é fazer consultas (<code>SELECT</code>)! 👨‍💻 </p>