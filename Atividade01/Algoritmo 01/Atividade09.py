pequeno = 10
médio = 12
grande = 15
valor01 = int(input("Digite a quantidade de camisas pequenas: "))
valor02 = int(input("Digite a quantidade de camisas médias: "))
valor03 = int(input("Digite a quantidade de camisas grandes: "))

total = valor01 * pequeno + valor02 * médio + valor03 * grande
print("O valor total arrecadado será de",total,"R$")
