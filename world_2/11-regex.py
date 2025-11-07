import re
text = "OneBitCode: Transoformando pessoas em programadores sem limites"

#1 - indice inicial e final de palavras
# r -> Estamos trabalhando com uma string bruta
match = re.search(r"pessoas em programadores", text)
print("Indice Inicial", match.start())
print("Indice Final", match.end())

#2 - Buscando o indice que possui o ponto
site = "https://onebitcode.com"
match = re.search(r"\.",site)
print(match)

#3 - Buscando uma lista de caracteres dentro de uma frase
padrao = "[a-m]"
result = re.findall(padrao, text)
print(text)
print(result)

