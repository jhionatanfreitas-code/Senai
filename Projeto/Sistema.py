tanque = 50.0
perda_por_hora = 2
hora = 1

while tanque > 5: 
    print(f"Hora {hora}")
    print(f"Combustível restante {tanque} litros" )
    
tanque -= tanque_por_hora
hora += 1