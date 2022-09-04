dias = int (input("quanto o aluguel "))
km = int(input(" quanto km que ele ja rodo  "))
pagar = (dias * 60) + (km * 0.15)
print(f'vou pagar o valor de R$ {pagar:.2f} R$' )