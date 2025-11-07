import hashlib

#1- verificar os algoritimos disponiveis
print(hashlib.algorithms_available)

#2- ALGORIITMOS DSPONIVEIS DE ACRODO COM SO
print(hashlib.algorithms_guaranteed)

#3- Utilizando o shar256
algoritimo = hashlib.sha256() #Cria um objeto que representa o algoritmo SHA-256. Ele está pronto para receber dados, mas ainda não tem nada.

print(algoritimo.digest()) #O passoa para criptografar

menssagem = "A melhor forma de prever o futuro é criá-lo".encode() #Transforma a string em bytes, que é o formato necessário para aplicar o hash.
algoritimo.update(menssagem) #Adiciona os dados da mensagem ao objeto do algoritmo.
print(algoritimo.hexdigest()) #Imprime e Gera o hash final em formato hexadecimal


"""
SHA-256 é um algoritmo de hash criptográfico que transforma qualquer entrada (texto, arquivo, etc.) 
em uma sequência fixa de 64 caracteres hexadecimais (256 bits). Ele é irreversível — ou seja,
não dá para descobrir a mensagem original a partir do hash.
"""

#Utilizando o MD5
md5 = hashlib.md5()
md5.update(menssagem)
print(md5.hexdigest())

"""
MD5 (Message Digest 5) é um algoritmo que gera um hash de 128 bits, normalmente representado como uma sequência de 32 caracteres hexadecimais.
Ele transforma qualquer entrada (texto, arquivo, etc.) em uma “impressão digital” única.

MD5 não é recomendado para segurança, pois já foram descobertas vulnerabilidades que permitem gerar colisões (duas entradas diferentes com o mesmo hash).

"""