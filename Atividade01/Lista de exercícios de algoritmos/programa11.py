contador = 0
soma = 0
while contador <=5:
    salário = float(input(f"Digite o Salário do {contador} Funcionário: "))
    contador += 1
    soma += salário
media = soma / 5  
print("A média salarial dos seus funcionários é :" , media)