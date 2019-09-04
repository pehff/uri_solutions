distancia_total_percorrida = float(input())
total_combustivel_gasto = float(input())

consumo_medio = distancia_total_percorrida / total_combustivel_gasto

print('{:.3f} km/l'.format(consumo_medio))