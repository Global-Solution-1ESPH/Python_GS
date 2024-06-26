#lista que armazena os criadouros
fazenda = []

#função para exibir menu principal
def menuPrincipal():
    print("\n\nOlá, Seja Bem-vindo(a) ao Fish Manager!")
    print("Escolha a opção que mais faz sentido para você!")
    print("1- Procuro dicas para começar!")
    print("2- Quero gerenciar a minha produção!")
    print("0- Sair")
    op = int(input("Digite a opção: "))
    return op

#função para exibir menu de dicas
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
               
                

# função para exibir o menu de gerenciamneto 
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
    

#função que adiciona um novo criadouro a fazenda
def addCriadouro():
    nome_peixe = input("\n\nDigite o nome da espécie: ").lower()
    qntd = int(input("Digite a quantidade de alevinos: "))
    mes_inicio = int(input("Digite o mes de inicio (1 a 12): "))
    ano = int(input("Digite o ano de início (ex. 2024): "))

    criadouro ={              #Dicionário para armazenar variáveis de diferentes tipos
        "Espécie" : nome_peixe,
        "Quantidade" : qntd,
        "Data de início" : f"{mes_inicio}/{ano}",
        "Alimentação" : []
    }
    fazenda.append(criadouro)   #utiliza a função append para adicionar


#função que registra a alimentação de cada criadouro
def addAlim():
    qntd = float (input("\n\nDigite a quantidade em Kg: "))
    criad = input("Para qual criadouro?: ").lower()
    hora = int(input("Qual a hora? (00 às 23) :"))

    alim = {
        "Quantidade" : qntd,
        "Criadouro" : criad,
        "Hora" : hora
        
    }
    addAlimtoCriad(criad,alim)
    return alim

def addAlimtoCriad(criad, alim):
    for criadouro in fazenda:
        if criadouro["Espécie"] == criad:
            criadouro["Alimentação"].append(alim)
            break
    


#parte principal do codigo
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
    

