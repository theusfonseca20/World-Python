# 🎬 Projeto de Banco de Dados: Streaming

Este repositório contém os scripts SQL (PostgreSQL) para criar e popular um banco de dados de streaming, contendo tabelas para filmes e séries.

---

## 1. Tabela `filmes`

### Estrutura da Tabela (CREATE TABLE)

```sql
CREATE TABLE filmes (
  id SERIAL PRIMARY KEY,
  titulo VARCHAR(100) NOT NULL,
  diretor VARCHAR(100) NOT NULL,
  ano SMALLINT NOT NULL,
  genero VARCHAR(50),
  duracao INT,
  avaliacao DECIMAL(3,1),
  bilheteria DECIMAL(15,2),
  custo DECIMAL(15,2)
);
```

### Inserção de Dados (INSERT INTO)

```sql
INSERT INTO filmes (
  titulo, 
  diretor, 
  ano, 
  genero, 
  duracao, 
  avaliacao, 
  bilheteria, 
  custo
) 
VALUES 
  ('Mad Max: Fury Road', 'George Miller', 2015, 'Ação', 120, 8.1, 375200000.00, 150000000.00),
  ('Star Wars', 'George Lucas', 1977, 'Sci-Fi', 121, 8.6, 775398007.00, 11000000.00),
  ('Super Mario Bros', 'Aaron Horvath, Michael Jelenic', 2023, 'Animação', 92, 7.3, 1300000000.00, 100000000.00),
  ('Pride and Prejudice', 'Joe Wright', 2005, 'Romance', 129, 7.8, 121147947.00, 28000000.00),
  ('Back to the Future', 'Robert Zemeckis', 1985, 'Sci-Fi', 116, 8.5, 381109762.00, 19000000.00),
  ('The Godfather', 'Francis Ford Coppola', 1972, 'Crime', 175, 9.2, 246120974.00, 6000000.00),
  ('The Lord of the Rings: The Return of the King', 'Peter Jackson', 2003, 'Fantasia', 201, 9.0, 1146030912.00, 94000000.00),
  ('Treasure Plane', 'Ron Clements, John Musker', 2002, 'Animação', 95, 7.2, 109578115.00, 140000000.00),
  ('Jurassic Park', 'Steven Spielberg', 1993, 'Aventura', 127, 8.1, 1043580597.00, 63000000.00),
  ('About Time', 'Richard Curtis', 2013, 'Romance', 123, 7.8, 87100000.00, 12000000.00),
  ('Transformers', 'Michael Bay', 2007, 'Ação', 144, 7.0, 709709780.00, 150000000.00);
```

---

## 2. Tabela `series`

### Estrutura da Tabela (CREATE TABLE)

```sql
CREATE TABLE series (
  id SERIAL PRIMARY KEY,
  titulo VARCHAR(100) NOT NULL,
  criador VARCHAR(100) NOT NULL,
  ano SMALLINT NOT NULL,
  genero VARCHAR(50),
  temporadas SMALLINT,
  episodios SMALLINT NOT NULL,
  avaliacao DECIMAL(3,1),
  canal VARCHAR(50),
  situacao VARCHAR(50) NOT NULL
);
```

### Inserção de Dados (INSERT INTO)

```sql
INSERT INTO series (
    titulo, 
    criador, 
    ano, 
    genero, 
    temporadas, 
    episodios, 
    avaliacao, 
    canal, 
    situacao
) 
VALUES 
('Breaking Bad', 'Vince Gilligan', 2008, 'Drama', 5, 62, 9.5, 'AMC', 'Finalizada'),
('Game of Thrones', 'David Benioff, D.B. Weiss', 2011, 'Fantasia', 8, 73, 9.3, 'HBO', 'Finalizada'),
('Stranger Things', 'The Duffer Brothers', 2016, 'Sci-Fi', 4, 34, 8.7, 'Netflix', 'Em Andamento'),
('Friends', 'David Crane, Marta Kauffman', 1994, 'Comédia', 10, 236, 8.9, 'NBC', 'Finalizada'),
('The Office', 'Greg Daniels', 2005, 'Comédia', 9, 201, 8.8, 'NBC', 'Finalizada'),
('Vikings', 'Michael Hirst', 2013, 'Drama Histórico', 6, 89, 8.5, 'History Channel', 'Finalizada'),
('Lost', 'J.J. Abrams, Damon Lindelof', 2004, 'Mistério', 6, 121, 8.4, 'ABC', 'Finalizada'),
('Once Upon a Time', 'Edward Kitsis, Adam Horowitz', 2011, 'Fantasia', 7, 155, 7.7, 'ABC', 'Finalizada'),
('The Mentalist', 'Bruno Heller', 2008, 'Crime', 7, 151, 8.1, 'CBS', 'Finalizada'),
('Star Trek', 'Gene Roddenberry', 1966, 'Sci-Fi', 3, 79, 8.4, 'NBC', 'Finalizada'),
('Cobra Kai', 'Josh Heald, Jon Hurwitz, Hayden Schlossberg', 2018, 'Ação', 5, 50, 8.6, 'Netflix', 'Em Andamento');
```

---

## 3. Exemplos de Consultas (SELECTs)

### Consultar todas as tabelas
> Retorna todos os dados das tabelas `filmes` e `series`.
```sql
SELECT * FROM filmes;
SELECT * FROM series;
```

### Filmes em ordem alfabética (A-Z)
```sql
SELECT * FROM filmes ORDER BY titulo ASC;
```

### Filmes com bilheteria acima de 500 milhões
```sql
SELECT * FROM filmes WHERE bilheteria > 500000000;
```

### Colunas específicas de séries (do mais antigo para o mais novo)
```sql
SELECT id, titulo, ano, genero, temporadas, episodios, avaliacao, situacao 
FROM series 
ORDER BY ano ASC;
```

### Séries finalizadas (da pior avaliação para a melhor)
```sql
SELECT * FROM series 
WHERE situacao IN ('Finalizada') 
ORDER BY avaliacao ASC;
```

### Filmes lançados antes dos anos 2000
```sql
SELECT * FROM filmes WHERE ano < 2000;
```

### Média de avaliação por duração do filme
> Calcula a média de filmes com até 2h (120 min) e filmes com mais de 2h.
```sql
SELECT 
  AVG(CASE WHEN duracao <= 120 THEN avaliacao ELSE NULL END) AS media_ate_2_horas,
  AVG(CASE WHEN duracao > 120 THEN avaliacao ELSE NULL END) AS media_acima_2_horas 
FROM filmes;
```

## 4. Exemplos de Modificação (UPDATE / DELETE)

### Atualizar Dados (UPDATE)

> Altera o valor 'Em Andamento' para 'Em Progresso' na tabela `series`.
> *Útil para padronizar dados.*
```sql
UPDATE series 
SET situacao = 'Em Progresso' 
WHERE situacao = 'Em Andamento';
```

> Atualiza o título e o gênero de um filme específico na tabela `filmes`.
```sql
UPDATE filmes 
SET titulo = 'Star Wars: A New Hope', genero = 'Sci/fantasia' 
WHERE titulo = 'Star Wars';
```

### Apagar Dados (DELETE)

> Remove uma linha específica (a série 'The Office') da tabela `series`.
```sql
DELETE FROM series 
WHERE titulo = 'The Office';
```

> Remove todas as séries que começaram antes do ano 2000 E que tiveram mais de 5 temporadas.
```sql
DELETE FROM series 
WHERE ano < 2000 AND temporadas > 5;
```