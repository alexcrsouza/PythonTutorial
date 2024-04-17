# Imprime uma linha em branco
variavelcontrole = True

# Arquivo para salvar os dados
arquivo_banco_dados = 'basededados.txt'

# Lista de estudantes (simulando uma lista de dicionários)
listaEstudantes = []

# Função para carregar dados do arquivo para a lista de estudantes
def carregar_estudantes():
    try:
        with open(arquivo_banco_dados, 'r') as arquivo:
            for linha in arquivo:
                nome = linha.strip()  # Remove espaços em branco e quebras de linha
                listaEstudantes.append({'nome': nome})
        print("Dados carregados com sucesso!")
    except FileNotFoundError:
        print("Arquivo de banco de dados não encontrado. Criando novo arquivo.")

# Função para salvar dados da lista de estudantes para o arquivo
def salvar_estudantes():
    with open(arquivo_banco_dados, 'w') as arquivo:
        for estudante in listaEstudantes:
            arquivo.write(f"{estudante['nome']}\n")
    print("Dados salvos com sucesso!")

# Carregar dados do arquivo ao iniciar o programa
carregar_estudantes()

# Imprime o menu principal
while variavelcontrole:
    print()
    print('----- Menu Principal -----')
    print()
    print('1. Gerenciar Estudantes')
    print('2. Gerenciar Professores')
    print('3. Gerenciar Disciplinas')
    print('4. Gerenciar Turmas')
    print('5. Gerenciar Matrículas')
    print('9. Sair')
    print()

    # Solicita a opção desejada ao usuário (deve ser digitado como número)
    opcaoMenu = int(input("Informe a opção desejada: "))

    # Define o módulo baseado na opção escolhida
    if opcaoMenu == 1:
        selecaoModulo = "ESTUDANTES"
        # Loop do menu de Estudantes
        while True:
            print()
            print(f'***** {selecaoModulo} MENU DE OPERAÇÕES *****')
            print()
            print('1. Incluir')
            print('2. Listar')
            print('3. Atualizar')
            print('4. Excluir')
            print('9. Voltar ao Menu Principal')
            print()

            # Solicita a opção do menu do módulo de Estudantes
            opcaoMenuModulo = int(input("Informe a opção desejada: "))

            if opcaoMenuModulo == 1:
                # Incluir Estudante
                nomeEstudante = input("Digite o nome do Aluno: ")
                listaEstudantes.append({'nome': nomeEstudante})
                print(f"Estudante '{nomeEstudante}' incluído com sucesso.")
                # Salvar os dados após adicionar um estudante
                salvar_estudantes()

            elif opcaoMenuModulo == 2:
                # Listar Estudantes
                if len(listaEstudantes) > 0:
                    print("Lista de estudantes:")
                    for estudante in listaEstudantes:
                        print(f"Nome: {estudante['nome']}")
                else:
                    print("Nenhum estudante cadastrado.")

            elif opcaoMenuModulo == 3:
                # Atualizar Estudante
                print("Implemente a lógica de atualização de estudantes aqui.")

            elif opcaoMenuModulo == 4:
                # Excluir Estudante
                print("Implemente a lógica de exclusão de estudantes aqui.")

            elif opcaoMenuModulo == 9:
                # Voltar ao Menu Principal
                salvar_estudantes()  # Salvar os dados antes de voltar ao menu principal
                break  # Sai do loop do menu de Estudantes

    elif opcaoMenu == 2:
        selecaoModulo = "PROFESSORES"
        print(f'***** {selecaoModulo} MENU DE OPERAÇÕES *****')
        print("Implemente as operações para gerenciar professores aqui.")
    elif opcaoMenu == 3:
        selecaoModulo = "DISCIPLINAS"
        print(f'***** {selecaoModulo} MENU DE OPERAÇÕES *****')
        print("Implemente as operações para gerenciar disciplinas aqui.")
    elif opcaoMenu == 4:
        selecaoModulo = "TURMAS"
        print(f'***** {selecaoModulo} MENU DE OPERAÇÕES *****')
        print("Implemente as operações para gerenciar turmas aqui.")
    elif opcaoMenu == 5:
        selecaoModulo = "MATRÍCULAS"
        print(f'***** {selecaoModulo} MENU DE OPERAÇÕES *****')
        print("Implemente as operações para gerenciar matrículas aqui.")
    elif opcaoMenu == 9:
        print("Saindo do programa...")
        salvar_estudantes()  # Salvar os dados antes de sair
        break  # Sai do loop principal (encerra o programa)
    else:
        print("Opção inválida ou módulo não implementado.")

# Imprime uma linha em branco
print()