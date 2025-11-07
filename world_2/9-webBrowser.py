import webbrowser
done = False

while not done:
    print("O que você deseja fazer? ")
    print("1. Aprender python")
    print("2. Aprender sobre módulos")
    print("3. Aprender python, Full Stak JS, ingles e No Code")
    print("4. Sair")
    escolha = input(">>>")
    
    if escolha == "1":
        webbrowser.open("https://www.python.org")
    elif escolha == "2":
        webbrowser.open("https://docs.python.org/3/py-modindex.html")
    elif escolha == "3":
        webbrowser.open("https://pages.onebitcode.com")
    elif escolha == "4":
        done = True
    else:
        print("Opçao inválida.... escolha novamente")