📌 SELECTS no Banco de dados

SELECT * FROM [nome da tabela];
SELECT * FROM clients  (pegando tudo da tabela clientes)


SELECT id, name_provider, phone FROM provider;
Escolhendo colunas que eu quero pegar na minha tabela provider

SELECT * FROM ingredients WHERE quantity < 20;
Pegando as linhas onde a quantidade é menor de 20

SELECT * FROM ingredients WHERE category = 'Diversos';
Pegando as linhas onde temos a categoria diversos

SELECT * FROM ingredients WHERE category = 'Diversos' AND quantity < 25;
Temos duas condições a categoria e quantidade

SELECT * FROM ingredients WHERE category = 'Diversos' OR category = 'Carnes';
Vamos procurar diversos ou carnes

SELECT * FORM ingredients WHERE category IN ('Carnes', 'Fruitas');
pegamos as as catogrias de carnes e frutas

SELECT * FROM clients ORDER BY name_client DESC
Vai trazer do Z para A ordem alfabetica ao contrario

SELECT * FROM clients ORDER BY name_client ASC
Vai do a até o Z ordem alfabetico

SELECT * FROM clients ORDER BY name_client ASC LIMIT 4;
ordem alfabetica normal, mas vai pegar apenas os 4 primeiros

SELECT * FROM clients ORDER BY name_client ASC LIMIT 4 OFFSET 4;
offset vai servir para paginação

SELECT SUM(quantity) AS Total from ingredients;
Somei os ingredientes da minha tabela

SELECT * FROM clients WHERE name_client LIKE 'M%'
O LIKE vai pegar todos que começam com o M, depois não importa

