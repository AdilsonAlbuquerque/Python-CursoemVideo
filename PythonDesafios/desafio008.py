m = float(input('Digita a quantidade de metros: '))
km = m * 0.001
hm = m * 0.01
dam = m * 0.1
dm = m * 10
cm = m * 100
mm = m * 1000
#print('{} metros é igual a {:.0f} centímetros ou {:.0f} milímetros'.format(m, cm, mm))
print('{} metros é igual a:\n{} Quilômetros\n{} Hectômetros\n{} Decâmetros\n{} Decímetros\n{} Centímetros\n{} Milímetros'.format(m, km, hm, dam, dm, cm, mm))
