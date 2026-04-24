sanduiche = int(input("Digite a qauntidade de sanduíches a serem feitos: "))
peso_queijo = 50
peso_presunto = 50
peso_carne = 100

total_queijo = (sanduiche * 2 * peso_queijo)/100
total_presunto = (sanduiche * 1 * peso_presunto)/1000
total_carne = (sanduiche * 1 * peso_carne)/1000

print(f"Para produzir {sanduiche} sanduíches, precisará de: ")
print(f"-- queijo {total_queijo}Kg")
print(f"-- presunto {total_presunto}Kg")
print(f"-- carne {total_carne}Kg")