<p align="center">
  <img src="https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExZnd2NGVoMWJ4NzZjOXBycTdpamR1YWduMDhwYnZhcmxzbmcxdXRvdCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/xTiTnxpQ3ghPiB2Hp6/giphy.gif" alt="Database GIF" width="200" style="margin-bottom: 20px;"/>
</p>

<h1 align="center">🔩 Tipos de Dados no SQL 🔢</h1>

<p align="center">
  Os <strong>Tipos de Dados</strong> definem a natureza dos valores que podem ser armazenados em uma coluna de uma tabela. <br>
  Escolher o tipo de dado correto é crucial para a <strong>eficiência</strong>, <strong>integridade</strong> e <strong>otimização</strong> do banco de dados.
</p>
<p align="center">
  ⚠️ <em>Existem muitas discussões sobre quais tipos são melhores ou piores em cada caso, e a escolha certa depende do seu projeto!</em>
</p>

---

### 🔢 Tipos de Dados Numéricos

Usados para armazenar números, desde idades até valores monetários complexos.

1.  **SMALLINT:** Inteiro de 2 bytes. Tem um alcance baixo, ideal para números pequenos (ex: idade, número de portas).
2.  **INT / INTEGER:** Inteiro de 4 bytes. O tipo mais comum para chaves primárias (IDs) e contagens gerais.
3.  **BIGINT:** Inteiro de 8 bytes. Usado para números inteiros muito grandes (ex: população mundial, contagem de views).
4.  **FLOAT:** Número com ponto flutuante de precisão simples.
5.  **DOUBLE / REAL:** Número com ponto flutuante de precisão dupla. Usado para cálculos científicos com muitas casas decimais.
6.  **DECIMAL / NUMERIC:** Número de precisão fixa. **Essencial para valores monetários**, pois evita os erros de arredondamento dos tipos `FLOAT` e `DOUBLE`.

---

### 🔡 Tipos de Dados de Texto

Usados para armazenar nomes, descrições, endereços e qualquer tipo de caractere.

1.  **CHAR(n):** Cadeia de caracteres de comprimento **fixo**. Se você define `CHAR(10)` e salva "oi", ele armazena "oi" + 8 espaços em branco. Útil para dados de tamanho sempre igual (ex: Sigla de Estado 'SP', 'RJ').
2.  **VARCHAR(n):** Cadeia de caracteres de comprimento **variável**. Se você define `VARCHAR(100)` e salva "oi", ele armazena apenas "oi". É o tipo mais comum e flexível para textos (ex: nomes, e-mails).
3.  **TEXT:** Cadeia de caracteres muito grande. Usado para armazenar descrições longas, artigos de blog, comentários, etc., onde o `VARCHAR` não é suficiente.

---

<p align="center">
  Escolher o tipo certo economiza espaço e torna as consultas mais rápidas! 👨‍💻
</p>