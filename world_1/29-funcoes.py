def wellcome():
    print("hello world")

wellcome()
wellcome()
wellcome()
wellcome()
wellcome()

def soma():
    #print(5+ 4)
    return 5 + 4
print(soma())

def create_game():
    name = input("Digite o nome do jogo: ")
    yearLaunc = int(input("Digite o ano de lançamento do jogo: "))
    gamePrice = float(input("Digite o preço do jogo: "))
    print(f"O {name} - R$ {gamePrice}")
create_game()
create_game()