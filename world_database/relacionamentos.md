<p align="center">
  <img src="https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExZnd2NGVoMWJ4NzZjOXBycTdpamR1YWduMDhwYnZhcmxzbmcxdXRvdCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/xTiTnxpQ3ghPiB2Hp6/giphy.gif" alt="Database GIF" width="200" style="margin-bottom: 20px;"/>
</p>

<h1 align="center">🔗 Relacionamentos em Banco de Dados 🗃️</h1>

<p align="center">
  Chamamos de <strong>associações</strong> as formas como vinculamos os dados de uma tabela aos dados de outra tabela. <br>
  Elas são a base que torna um banco de dados "relacional".
</p>

---

### ⚙️ Como funcionam os relacionamentos?

Para que os relacionamentos funcionem, eles utilizam dois conceitos de chaves:

* 🔑 **Chave Primária (Primary Key, ou PK):** Coluna (ou conjunto de colunas) que identificam unicamente cada linha de uma tabela. É o identificador exclusivo do registro.
* 🔗 **Chave Estrangeira (Foreign Key, ou FK):** Coluna (ou conjunto de colunas) em uma tabela que estabelece uma ligação com a Chave Primária de outra tabela. Ela "aponta" para o registro relacionado.

---

### 🔀 Os Três Tipos de Relacionamentos

Existem três tipos principais de associações que podemos criar no SQL:

1.  **Um para Um (1:1)**
    * **Definição:** Cada linha de uma tabela está relacionada a, no máximo, uma linha de outra tabela.
    * **Exemplo:** `Um USUÁRIO possui um ENDEREÇO e um ENDEREÇO só pode pertencer a um USUÁRIO.`

2.  **Um para Muitos (1:N)**
    * **Definição:** Cada linha de uma tabela (o lado "1") pode estar relacionada a múltiplas linhas de outra tabela (o lado "N").
    * **Exemplo:** `Um GÊNERO pode ser usado por vários FILMES, mas um FILME possui apenas um GÊNERO.`

3.  **Muitos para Muitos (N:N)**
    * **Definição:** Linhas de uma tabela podem estar relacionadas a múltiplas linhas de outra tabela, e vice-versa. (Nota: Isso geralmente requer uma "tabela associativa" para ser implementado).
    * **Exemplo:** `Um POST do blog pode ser classificado com várias TAGS e uma mesma TAG pode ser usada para classificar vários POSTS.`

---

### ✅ Por que Relacionamentos são Importantes?

Usar relacionamentos de forma correta é fundamental para:

* **Garantir a Integridade:** Assegura que os dados sejam consistentes e precisos.
* **Evitar Redundância:** Impede que a mesma informação seja repetida desnecessariamente.
* **Consultas Eficientes:** Permite combinar dados de várias tabelas de forma rápida e lógica.
* **Segurança da Informação:** Ajuda a estruturar e proteger os dados.