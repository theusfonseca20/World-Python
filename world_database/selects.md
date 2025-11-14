<p align="center">
  <img src="https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExZnd2NGVoMWJ4NzZjOXBycTdpamR1YWduMDhwYnZhcmxzbmcxdXRvdCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/xTiTnxpQ3ghPiB2Hp6/giphy.gif" alt="Database GIF" width="200" style="margin-bottom: 20px;"/>
</p>

<h1 align="center">🗃️ Comandos SQL — SELECT 🔍</h1>

<p align="center">
  Aqui está um guia simples e direto dos principais comandos <strong>SELECT</strong> utilizados no dia a dia ao consultar bancos de dados SQL. <br>
  Organizado, bonitinho e pronto para o GitHub! 😄
</p>

---

### 📌 Selecionar tudo da tabela

Retorna todas as colunas e linhas da tabela.

```sql
SELECT * FROM nome_da_tabela;

SELECT * FROM clients;

🎯 Selecionar colunas específicas
Quando você precisa apenas de algumas colunas da tabela.
SELECT id, name_provider, phone 
FROM provider;

🔽 Filtrar resultados com WHERE
➤ Quantidade menor que 20
Traz apenas registros onde a quantidade é menor que 20.
SELECT * 
FROM ingredients 
WHERE quantity < 20;

➤ Categoria específica
Filtra somente registros da categoria informada.
SELECT * 
FROM ingredients 
WHERE category = 'Diversos';

➤ Duas condições ao mesmo tempo (AND)
Precisa atender a ambas as condições.
SELECT * 
FROM ingredients 
WHERE category = 'Diversos' 
  AND quantity < 25;


➤ Uma condição OU outra (OR)
Retorna registros que atendem pelo menos uma das condições.
SELECT * 
FROM ingredients 
WHERE category = 'Diversos' 
   OR category = 'Carnes';


➤ Usando IN
Filtra por uma lista de categorias ou valores.
SELECT * 
FROM ingredients 
WHERE category IN ('Carnes', 'Frutas');

🔠 Ordenação com ORDER BY
➤ Ordem alfabética do Z → A (DESC)
Ordena os resultados de forma decrescente.
SELECT * 
FROM clients 
ORDER BY name_client DESC;


➤ Ordem alfabética do A → Z (ASC)
Ordena os resultados de forma crescente.
SELECT * 
FROM clients 
ORDER BY name_client ASC;



📄 Limitar quantidade de resultados (LIMIT)
➤ Pegando apenas os 4 primeiros
SELECT * 
FROM clients 
ORDER BY name_client ASC 
LIMIT 4;


➤ Paginação usando OFFSET
Pula registros e pega o próximo bloco.
SELECT * 
FROM clients 
ORDER BY name_client ASC 
LIMIT 4 OFFSET 4;



➕ Somando valores (SUM)
Soma todos os valores da coluna quantity.
SELECT SUM(quantity) AS Total 
FROM ingredients;



🔍 Buscar por padrão (LIKE)
➤ Nomes que começam com a letra M
SELECT * 
FROM clients 
WHERE name_client LIKE 'M%';


