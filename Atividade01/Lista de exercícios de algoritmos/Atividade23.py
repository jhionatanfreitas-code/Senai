altura_pessoa = float(input("Digite sua altura: "))
sombra_pessoa = float(input("Digite o comprimento da sua sombra: "))
sompra_predio = float(input("Digite o comprimento da sombra do prédio: "))
altura_predio = float(input("Digite o comprimento da sombra do prédio: "))

altura_predio = (altura_pessoa * sompra_predio) / sombra_pessoa

print(f"A altura do prédio é: {altura_predio} em metros")