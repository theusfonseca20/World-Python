'''
Escreva um programa que pergunte a distância que um passageiro deseja percorrer em km. Calcule o preço da passagem,
cobrando R$ 0,50 por km para viagens de até de 200 km, e R$ 0,35 para viagens mais longas.
'''

distancia = float(input("Digite a distancia da viagem em KM: "))
if distancia <= 200:
    preco = distancia * 0.50
    print(f"O preço da passagem para {distancia} KM é de R${preco:.2f}")
else:
    preco = distancia * 0.35
    print(f"O preço da passagem para {distancia} KM é de R${preco:.2f}")