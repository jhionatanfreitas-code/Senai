qtd_frangos = int(input("Digite a quantidade de frangos: "))

custo_chip = 4.0
custo_alimento = 3.50

gasto_por_frango = custo_chip + (2 * custo_alimento)
gasto_total = qtd_frangos * gasto_por_frango

print("Para colocar a quantidade desejada de anéis, será gasto: ", gasto_total)