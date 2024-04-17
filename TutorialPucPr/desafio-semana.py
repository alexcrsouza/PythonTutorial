while True:
    nome_aluno = input("Digite o nome do aluno (ou 'fim' para encerrar): ")
    
    if nome_aluno == 'fim':
        break
    
    total_notas = 0
    quantidade_notas = 0
    
    while True:
        nota = float(input("Digite a nota do aluno (ou -1 para encerrar): "))
        if nota == -1:
            break
        elif nota < 0 or nota > 10:
            print("Nota inválida! Digite uma nota entre 0 e 10.")
        else:
            total_notas += nota
            quantidade_notas += 1
    
    if quantidade_notas == 0:
        print("O aluno", nome_aluno, "não possui notas registradas.")
    else:
        media = total_notas / quantidade_notas
        print("A média do aluno", nome_aluno, "é:", media)
