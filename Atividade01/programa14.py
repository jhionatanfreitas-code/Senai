dia = int(input("Digite o dia: "))

while dia <1 or dia > 30:
    print("Dia inválido. O dia deve ser menor que 30")
    dia = int(input("Digite o dia novamente: "))
mês = int(input("Digite o mês: "))
while mês <1 or mês > 12:
    print("Mês inválido. O mês deve ser menor que 12: ")
    mês = int(input("Digite o mês:"))

    dias_passados = (mês - 1) * 30 + dia
    print("Desde o início do ano, passaram", dias_passados, "dias: ")
            

