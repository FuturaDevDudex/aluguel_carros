km = float(input('quantos quiometros ira percorrer ?'))
dias = int (input('Quantos dias ira precisar do automovel?'))

novo = (km * 0.15) + (dias * 60.00)

print (f'Pelos {dias} dias percorridos, ira pagar R${novo}')