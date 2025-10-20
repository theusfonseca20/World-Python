import pprint #pretty print para imprimir dicionarios de forma mais legivel

#dicionarios aninhados (dicionarios dentro de dicionarios)
gameDict = {
    "Resident Evil 4": {
      "yearLaunch": 2005,
      "classification": 8.9,
      "genre": ["Terror", "Ação", "Sobrevivência"],
    },
    "Mario Odyssey": {
      "yearLaunch": 2017,
      "classification": 9.5,
      "genre": ["Plataforma", "Aventura", "Familia"],
    },
    "Donkey Kong Country": {
      "yearLaunch": 2000,
      "classification": 9.2,
      "genre": ["Plataforma", "Aventura"],
    }
}

print(gameDict)
print(len(gameDict)) #Tamanho do dicionario
pprint.pprint(gameDict) #imprime o dicionario de forma mais legivel

print(gameDict["Mario Odyssey"]["genre"]) #Acessando valor via chave do dicionario aninhado

gameDict["Mario Odyssey"]["Developer"] = "Nitendo Switch" #Adicionando novo par chave-valor ao dicionario aninhado
print(gameDict["Mario Odyssey"])

del gameDict["Donkey Kong Country"] #Removendo o dicionario aninhado
pprint.pprint(gameDict) #imprime o dicionario de forma mais legivel