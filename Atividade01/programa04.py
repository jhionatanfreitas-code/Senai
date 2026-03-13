contador  = 1
soma_notas = 0

while contador <= 4:
    nota = float(input(f"Digite a nota do {contador } bimestre: "))
    if nota < 0  or nota> 10:
        print("Nota inválida. A nota deve estar entre 0 e 10: ")
        continue 
    contador += 1 
    soma_notas += nota
media = soma_notas / 4
print("A média de notas é: ", media)

if media >= 7:
    print("O aluno está aprovado: ")
if media >= 5:
    print("O aluno está em recuperação: ")
else:
    print("O aluno está reprovado: ")

    
    
