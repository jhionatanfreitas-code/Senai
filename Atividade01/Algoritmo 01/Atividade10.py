x = float(input("Primeiro plano: Digite o valor X: "))
y = float(input("Primeiro plano: Digite o valor Y: "))
x1 = float(input("Segundo plano: Digite o valor x: "))
y2 = float(input("Segundo plano: Digite o valor y: "))

import math
xx = x - x1
yy = y - y2
potência = xx ** 2 + yy ** 2
quadrada = potência ** 0.5

print("A distáncia está em", quadrada, "unidades")



