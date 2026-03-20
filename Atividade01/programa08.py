nome = (input("Digite seu nome: "))
num_idade = int(input("Insira a sua idade: "))


if num_idade < 0:
    print("Não pode inserir uma idade menor que zero")
elif num_idade > 120:
    print("Sua idade atingiu o limite do sistema")
else:
    dias_vida = num_idade * 365
    print("Você já viveu" , dias_vida,"dias de sua vida", nome)