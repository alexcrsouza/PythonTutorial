"""
Aluno: Alexandre Coelho Ribeiro de Souza
Disciplina: Raciocínio Computacional (11100010563_20241_02)
Atividade: Atividade Somativa 1
Versão: 1.4
"""

# Mostra o Menu Inicial

optMain = ""
optSubMenu = ""
students = []

while optMain != "9":

    workInProgressMain = True
    print("------------------------------")
    print("|       Menu Principal       |")
    print("------------------------------")
    print("  ")
    print("1 - Gerenciar estudantes")
    print("2 - Gerenciar professores")
    print("3 - Gerenciar disciplinas")
    print("4 - Gerenciar turmas")
    print("5 - Gerenciar matrículas")
    print("9 - Sair")
    print("  ")
    print("------------------------------")

    optMain = input("selecione a opção desejada: ")
    print("  ")

    # Define o módulo

    if optMain == "1":
        selectedModule = "estudantes"
        workInProgressMain = False
    elif optMain == "2":
        selectedModule = "professores"
    elif optMain == "3":
        selectedModule = "disciplinas"
    elif optMain == "4":
        selectedModule = "turmas"
    elif optMain == "5":
        selectedModule = "matrículas"
    elif optMain == "9":
        selectedModule = "sair"
        break
    else:
        print("===== Opção inválida =====")
        print("> Informe um valor de 1 a 5 ou 9 para sair.")
        print("  ")
        continue  

    # Verifica se a opção do Menu Principal está "em desenvolvimento"

    if workInProgressMain == True:
        print(f"===== Opção selecionada: {selectedModule} =====")
        print("  ")
        print("        -> EM DESENVOLVIMENTO <- ")
        print("  ")
        print("          selecione outra opção  ")
        print("  ")
        continue

    # Exibe o sub menu do módulo
        
    while optSubMenu != "9":
        workInProgressSubMenu = True
        print(f"===== Gestão de {selectedModule} =====")
        print("  ")
        print("1 - Incluir")
        print("2 - Listar")
        print("3 - Atualizar")
        print("4 - Excluir")
        print("9 - Voltar")
        print("  ")

        optSubMenu = input("selecione a opção desejada: ")
        print("  ")

        # Define a operação

        if optSubMenu == "1":
            selectedOperation = "incluir"
            workInProgressSubMenu = False
        elif optSubMenu == "2":
            selectedOperation = "listar"
            workInProgressSubMenu = False
        elif optSubMenu == "3":
            selectedOperation = "atualizar"
        elif optSubMenu == "4":
            selectedOperation = "excluir"
        elif optSubMenu == "9":
            selectedOperation = "voltar"
            optSubMenu = ""
            break
        else:
            print("===== Opção inválida =====")
            print("> Digite uma opção válida.")
            print("  ")
            continue  

        # Verifica se a opção do Menu de Operações está "em desenvolvimento"

        if workInProgressSubMenu == True:
            print(f"===== Operação selecionada: {selectedOperation} =====")
            print("  ")
            print("        -> EM DESENVOLVIMENTO <- ")
            print("  ")
            print("        selecione outra operação  ")
            print("  ")
            continue

        # Exibe operação
        print(f"===== Operação {selectedOperation} =====")
        print("  ")

        # Inclui estudantes
        if optSubMenu == "1":
            stdName = input("Informe o nome do estudante: ")
            students.append(stdName)
            print("  ")
            print(" Estudante incluído com sucesso! ")
            print("  ")

        # Lista estudantes
        elif optSubMenu == "2":
            if len(students) >= 1:
                for i, item in enumerate(students):
                    print(f" {i+1}. {item}  ")
                print("  ")
            else:
                print(" Não há estudantes cadastrados ")
                print("  ")                  


# Finaliza a aplicação

print("===> Finalizando a aplicação... ")
print("  ")


