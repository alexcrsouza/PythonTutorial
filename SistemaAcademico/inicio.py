"""
Aluno: Alexandre Coelho Ribeiro de Souza
Disciplina: Raciocínio Computacional (11100010563_20241_02)
Atividade: Atividade Somativa 1
Versão: 1.4
"""

# Mostra o Menu Inicial

optMain = 0
optSubMenu = 0

while optMain != 9:

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

    optMain = int(input("selecione uma opção desejada: "))
    print("  ")

    # Define o módulo

    if optMain == 1:
        selectedModule = "estudantes"
    elif optMain == 2:
        selectedModule = "professores"
    elif optMain == 3:
        selectedModule = "disciplinas"
    elif optMain == 4:
        selectedModule = "turmas"
    elif optMain == 5:
        selectedModule = "matrículas"
    elif optMain == 9:
        selectedModule = "sair"
        break
    else:
        selectedModule = "opção inválida"   

    # Exibe o sub menu do módulo
        
    while optSubMenu != 9:
        print(f"===== Gestão de {selectedModule} =====")
        print("  ")
        print("1 - Incluir")
        print("2 - Listar")
        print("3 - Atualizar")
        print("4 - Excluir")
        print("9 - Voltar")
        print("  ")

        optSubMenu = int(input("selecione uma opção desejada: "))
        print("  ")

        # Define a operação

        if optSubMenu == 1:
            selectedOperation = "incluir"
        elif optSubMenu == 2:
            selectedOperation = "listar"
        elif optSubMenu == 3:
            selectedOperation = "atualizar"
        elif optSubMenu == 4:
            selectedOperation = "excluir"
        elif optSubMenu == 9:
            selectedOperation = "voltar"
            optSubMenu = 0
            break
        else:
            selectedOperation= "opção inválida"  

         # Exibe operação
        print(f"===== Operação {selectedOperation} =====")
        print("  ")


# Finaliza a aplicação

print("===> Finalizando a aplicação... ")
print("  ")


