import json

#1- Strings para dicionario
pessoa = '{"nome": "Matheus", "Linguagem": ["Python", "JS", "SQL"]}'
pessoa_dic = json.loads(pessoa)
print(pessoa)
print(pessoa_dic)
print(pessoa_dic['Linguagem'])

#2- Dicionario para JSON
pessoa_json = json.dumps(pessoa_dic)
print(pessoa_json)
print(type(pessoa_json))

#3 - Formatando um json
print(json.dumps(pessoa_dic, indent=4, sort_keys=True))