<p align="center">
  <img src="https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExZnd2NGVoMWJ4NzZjOXBycTdpamR1YWduMDhwYnZhcmxzbmcxdXRvdCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/xTiTnxpQ3ghPiB2Hp6/giphy.gif" alt="Database GIF" width="200" style="margin-bottom: 20px;"/>
</p>

<h1 align="center">🔩 Tipos de Dados e Querys SQL 📅</h1>

<p align="center">
  Os <strong>Tipos de Dados</strong> definem a natureza dos valores que podem ser armazenados em uma coluna de uma tabela. <br>
  Escolher o tipo de dado correto é crucial para a <strong>eficiência</strong>, <strong>integridade</strong> e <strong>otimização</strong> do banco de dados.
</p>
<p align="center">
  ⚠️ <em>A escolha certa depende do seu projeto e do SGBD que você está usando!</em>
</p>

---

### 🔢 Tipos de Dados Numéricos

* **SMALLINT:** Inteiro de 2 bytes (alcance baixo, ex: idade).
* **INT / INTEGER:** Inteiro de 4 bytes (o mais comum para IDs).
* **BIGINT:** Inteiro de 8 bytes (para números inteiros muito grandes).
* **FLOAT / REAL:** Ponto flutuante (precisão simples/dupla, para cálculos científicos).
* **DECIMAL / NUMERIC:** Precisão fixa. **Essencial para valores monetários**, pois evita erros de arredondamento.

---

### 🔡 Tipos de Dados de Texto (String)

* **CHAR(n):** Comprimento **fixo**. (Se `CHAR(10)` e salvar "oi", armazena "oi" + 8 espaços). Útil para dados de tamanho fixo (ex: 'SP', 'RJ').
* **VARCHAR(n):** Comprimento **variável**. (Se `VARCHAR(100)` e salvar "oi", armazena só "oi"). Mais flexível e comum (ex: nomes, e-mails).
* **TEXT:** Cadeia de caracteres muito grande (ex: artigos de blog, descrições longas).

---

### 📅 Tipos de Data e Hora

* **DATE:** Armazena **apenas a data** (Ano, Mês, Dia). Ex: `2025-12-31`.
* **TIME:** Armazena **apenas a hora** (Hora, Minuto, Segundo). Ex: `14:30:00`.
* **TIMESTAMP:** Armazena **data E hora** juntas (Ano, Mês, Dia, Hora, Minuto, Segundo). Ex: `2025-12-31 14:30:00`.
* **TIMESTAMPTZ (Postgres):** Timestamp *com Timezone* (fuso horário). Essencial para aplicações globais.

---

### ⌨️ Exemplos de Querys (Usando os Tipos)

Veja como usamos esses tipos ao criar uma tabela (`CREATE TABLE`) e inserir dados (`INSERT`).

**1. Criando a tabela `produtos`:**
```sql
CREATE TABLE produtos (
    id SERIAL PRIMARY KEY,            -- (INT)
    nome VARCHAR(100) NOT NULL,     -- (VARCHAR)
    preco DECIMAL(10, 2) NOT NULL,  -- (DECIMAL para R$ 99.999.999,99)
    tipo_produto CHAR(3),              -- (CHAR fixo, ex: 'ELT', 'ALM')
    data_cadastro DATE DEFAULT NOW()  -- (DATE com data de hoje como padrão)
);