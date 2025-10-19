# Set => Conjunto
# Conjuntos são coleções não ordenadas de itens únicos. Eles são úteis quando você quer garantir que não haja duplicatas em uma coleção de itens.
# Não possibilita recuperar valores via fatiamento ou slice
# True e 1 são considerados iguais em um set 

gameSet = {"Fifa 23", "Cyberpunk 2077", "The Witcher 3", "Mario Odyssey"} # Note que "Fifa 23" está repetido
print(gameSet)
print(len(gameSet)) #improme o tamanho do set

exampleSet = {"Fifa 23", True, 1}
gameSet.update(exampleSet) #Adiciona os elementos do exampleSet ao gamesSet
print(gameSet)

gameSet.remove(True) #Remove o elemento True do set
print(gameSet)