
lista_de_compras = []


def exibir_lista():
    print("Lista de compras:")
    for item in lista_de_compras:
        print("- " + item)


def adicionar_item():
    item = input("Digite o item que deseja adicionar: ")
    lista_de_compras.append(item)
    print(item + " foi adicionado à lista de compras.")


def remover_item():
    item = input("Digite o item que deseja remover: ")
    if item in lista_de_compras:
        lista_de_compras.remove(item)
        print(item + " foi removido da lista de compras.")
    else:
        print(item + " não foi encontrado na lista de compras.")


while True:
    
    print("\nO que você gostaria de fazer?")
    print("1 - Exibir a lista de compras")
    print("2 - Adicionar um item à lista de compras")
    print("3 - Remover um item da lista de compras")
    print("4 - Sair do programa")

    
    escolha = input("Digite o número da opção desejada: ")

   
    if escolha == "1":
        exibir_lista()
    elif escolha == "2":
        adicionar_item()
    elif escolha == "3":
        remover_item()
    elif escolha == "4":
        
        print("Obrigado por usar o programa!")
        break
    else:
        print("Opção inválida. Por favor, tente novamente.")