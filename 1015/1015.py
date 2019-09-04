from math import sqrt

eixos_p1 = input()
eixos_p2 = input()

p1_x = float(eixos_p1.split()[0])
p1_y = float(eixos_p1.split()[1])

p2_x = float(eixos_p2.split()[0])
p2_y = float(eixos_p2.split()[1])


distancia = sqrt((p2_x - p1_x)**2 + (p2_y - p1_y)**2)

print('{:.4f}'.format(distancia))
