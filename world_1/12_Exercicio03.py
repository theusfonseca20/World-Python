'''
Escreva um programa Python para obter uma string de uma determinada string em que todas as
ocorrências de seu primeiro caractere foram alteradas para '$', exceto o próprio primeiro caractere
'''
name = "Fifa 23"
primeiro_caractere = name[0].lower() #Pegamos o primeiro caractere e convertemos para minúsculo
nova_string = name.replace(primeiro_caractere, '$') #A nova string vai ter o nome do jogo. Mas todas as ocorrências do f serão substituídas por $
print(primeiro_caractere + nova_string[1:])

