#calcule os estudantes aprovados e reprovados. 
grupo = 3 # 3 ou qualquer outro numero de repetições.
soma = 0
media = 0
aprovados = 0 
reprovados = 0
notas = [] #variavel dinamica (vai receber dados)

for i in range (grupo): #variavel 1 varia de 0 até 2.
    nota=float(input("Digite a nota {}: ".format(i+1)))  
    notas.append(nota)
    if (notas[i]>=7):
        aprovados+=1
    elif (notas[i]<7):
        reprovados+=1    

for i in range (grupo):
    soma+=notas[i]
    print("")
    print("A média da classe é {:.2f} ".format(soma/grupo))
    print("Aprovados: ",aprovados)
    print("reprovados:",reprovados)
    print("")
    print("notas digitadas:")

for nota in notas:
    print(nota)