
fazenda = []

def menuPrincipal():
    print("\n\nOlá, Seja Bem-vindo(a) ao Fish Manager!")
    print("Escolha a opção que mais faz sentido para você!")
    print("1- Procuro dicas para começar!")
    print("2- Quero gerenciar a minha produção!")
    print("0- Sair")
    op = int(input("Digite a opção: "))
    return op

def menuDicas():
    while True:
        print("\n\n1- Qual espécies recomendamos para iniciar")
        print("2- Como acomodá-las?")
        print("3- O que você precisa ter para começar?")
        print("0- Sair")
        op = int(input("Digite a opção: "))
        while(op <0 or op>3):
            op= int(input("Opção inválida. Tente novamente: "))
        if op == 0:
            break 
        match op:
            case 1:
                print("\n\tPara começar, recomendamos:\n Tilápia, Tambaqui, Pintado e Pacu\n")
                
            case 2:
                print("\n\tÉ necessário tanques e condições ambientais\n de acordo com as normas regulamentadoras\n")
                
            case 3:
                print("\n\tUma infraestrutura adequada e estar disposto a investir seu tempo!\n")
               
                


def MenuGerenciamento():
    while True:
        print("\n\n1- Adicionar um novo criadouro.")
        print("2- Visualizar todos os criadouros.")
        print("3- Registrar a alimentação.")
        print("0- Sair")
        op = int(input("Digite a opção: "))
        while(op<0 or op>3):
            op = int(input("Opção Inválida. Tente Novamente: "))
        if op == 0:
            break
        match op:
            case 1:
                addCriadouro()
            case 2:
                print("\n")
                print(fazenda)
            case 3:
                alim = addAlim()
                print("\n")
                print(alim)
    


def addCriadouro():
    nome_peixe = input("\n\nDigite o nome da espécie: ")
    qntd = int(input("Digite a quantidade de alevinos: "))
    mes_inicio = int(input("Digite o mes de inicio: "))
    ano = int(input("Digite o ano de início: "))

    criadouro ={
        "Espécie" : nome_peixe,
        "Quantidade" : qntd,
        "Data de início" : f"{mes_inicio}/{ano}"
    }
    fazenda.append(criadouro)



def addAlim():
    qntd = float (input("\n\nDigite a quantidade em KG: "))
    criad = input("Para qual criadouro?: ")
    hora = int(input("Qual a hora? (00 às 23) :"))

    alim = {
        "Quantidade" : qntd,
        "Criadouro" : criad,
        "Hora" : hora
    }
    return alim




while True:
    op1 = menuPrincipal()
    if op1 == 0:
        print("Encerrando...")
        break
    match op1:
        case 1:
            menuDicas()
        case 2:
            MenuGerenciamento()
        case _:
            print("Opção inválida!")
    

