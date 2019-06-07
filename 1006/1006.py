PESO_A = 2
PESO_B = 3
PESO_C = 5
nota_a = float(input(""))
nota_b = float(input(""))
nota_c = float(input(""))
media = ((nota_a * PESO_A) + (nota_b * PESO_B) + (nota_c * PESO_C)) / (
    PESO_A + PESO_B + PESO_C
)

print("MEDIA = {:.1f}".format(media))
