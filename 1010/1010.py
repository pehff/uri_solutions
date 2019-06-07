peca_1, num_peca_1, valor_peca_1 = input().split()
peca_1, num_peca_1, valor_peca_1 = int(peca_1), int(num_peca_1), float(valor_peca_1)

peca_2, num_peca_2, valor_peca_2 = input().split()
peca_2, num_peca_2, valor_peca_2 = int(peca_2), int(num_peca_2), float(valor_peca_2)

total = (num_peca_1 * valor_peca_1) + (num_peca_2 * valor_peca_2)

print('VALOR A PAGAR: R$ {:.2f}'.format(total))