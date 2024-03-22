#solicita as notas
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
nota4 = float(input("Digite a quarta nota: "))

#calcula a média
media = (nota1 + nota2 + nota3 + nota4)/4

#verifica se está acima de 7
if media >= 7:
  print(f"Parabéns! Sua nota foi {media:.2f} e você passou!")

else:
   print(f"Lamentamos, mas sua nota foi {media:.2f} e você foi reprovado.")

#mensagem final
print(f"Nota: {media:.2f}.")