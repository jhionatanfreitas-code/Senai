nome = (input("Digite seu nome: "))
num_idade = int(input("Insira a sua idade: "))
while True:
    if num_idade < 0 or num_idade > 120:
        print("Sua idade está inválida: ")
        num_idade = int(input("Insira a sua idade: "))
    else:
        break
        dias_vida = num_idade * 365
        print("Você já viveu" , dias_vida,"dias de sua vida", nome)