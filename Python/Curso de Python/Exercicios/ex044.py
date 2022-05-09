v1 = float(input('QUAL O SEU PESO? (KG)'))
v2 = float(input('QUAL E A SUA ALTURA? (M)'))
v3 = v1 / (v2 * v2)

print('')
print('VOCE ESTA EM:', end=' ')

if v3 < 18.5:
    print('MAGREZA')
elif v3 >= 18.5 and v3 < 25:
    print('NORMAL')
elif v3 >= 25 and v3 < 30:
    print('SOBREPESO')
elif v3 >= 30 and v3 < 40:
    print('OBESIDADE')
elif v3 >= 40:
    print('OBESIDADE GRAVE, CUIDADO!!!')
