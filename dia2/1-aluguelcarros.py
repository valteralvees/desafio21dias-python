diascarro = float(input('Quantos dias você ficou com o carro? '))
totaldiarias = diascarro * 60
kmrodados = float(input('Quantos KM você rodou com o carro? '))
totalkm = kmrodados * 0.15
totalapagar = totaldiarias + totalkm
print(f'O custo total do seu aluguel foi de R${totalapagar:.2f}, considerando o aluguel, que custou R${totaldiarias:.2f} e o custo por KM rodado, que ficou no valor de R${totalkm:.2f}')