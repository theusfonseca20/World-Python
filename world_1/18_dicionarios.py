#Dicionario vazio. Temos chave e valor
dicionario = {}
print(type(dicionario))

# Dicionários são coleções não ordenadas de pares chave-valor. 
# Eles são úteis quando você quer associar valores a chaves específicas e recuperar esses valores rapidamente usando as chaves.
gameFifa = {
    "name": "Fifa 23",
    "genre": ["Esporte", "Familia", "Multiplayer"],
    "gamePrice": 299.99,
    "classification": 8.8
}

print(gameFifa)
print(len(gameFifa)) #Tamanho dicionario

print(gameFifa["genre"])#Acessando valor via chave
print(gameFifa.get("classification")) #Outra forma de acessar valor via chave
print(gameFifa.keys()) #Retorna todas as chaves do dicionario
print(gameFifa.values()) #Retorna todos os valores do dicionario
print(gameFifa.items()) #Retorna todos os itens chave e valor do diconario

gameFifa["developer"] = "EA Sports" #adiciona novo par chave-valor ao dicionario
print(gameFifa)

gameFifa.update({"gamePrice": 349.99}) #Atualiza o valor da chave gamePrice
print(gameFifa)

gameFifa.pop("classification") #Remove o par chave-valor do dicionario
print(gameFifa)