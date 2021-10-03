num = float(input('Digite um numero quebrado:'))
inteiro = int(num)
print(f'você digitou {num} e o valor inteiro é {inteiro}')

#outra forma de fazer
from math import trunc

num = float(input('Digite um numero quebrado:'))
print('O valro digitado foi {} e a sua porção inteira é {}'.format(num,trunc(num)))
