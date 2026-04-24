while True:
    prato_peso = float(input("Insira o peso do prato em Kg: "))
    if prato_peso >=0:
        break
    print("Valor inválido: ")

preço = prato_peso * 12.0
print("O valor a pagar será: ", preço, "Kg")