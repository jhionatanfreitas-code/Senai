num_pao = float(input("Quantidade de pão vendido: "))
num_broa = float(input("Quantidade de broa vendido: "))
arrecadado = (num_pao * 0.12) + (num_broa * 1.50)
poupança = (arrecadado * 0.10)

print("total de vendas: " , arrecadado)
print("quantidade que foi para a poupança: ", poupança)      


