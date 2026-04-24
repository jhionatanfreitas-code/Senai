dias = int(input("Digite a quantidade de dias sem acidentes: "))

anos = dias // 360
resto = dias % 360

meses = resto // 30
dias_restantes = resto % 30

print(f"Tempo sem acidentes: {anos} ano(s), {meses} mês(es) e {dias_restantes} dia(s)")