sal_fixo = float(input("Salário fixo: "))
vendas = float(input("Valor das vendas: "))

comissao = vendas * 0.04
sal_final = sal_fixo + comissao

print(f"Comissão : R$ {comissao:.2f}")
print(f"Salário final: R$ {sal_final:.2f}")