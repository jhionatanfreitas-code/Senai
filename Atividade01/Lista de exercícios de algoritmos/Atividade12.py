salário = float(input("Digite o salário: "))
salário_total = salário * 0.15
aumento = salário + salário_total
imposto = aumento * 0.08
salário_final = aumento - imposto
print("O salário sem aumento era: ", salário,"R$")
print("O salário com aumento fica: ", aumento, "R$")
print("O salário final fica: ", salário_final, "R$")