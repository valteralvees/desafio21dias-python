preco = float(input('Digite o preço do produto a ser conferido o desconto: R$'))
desconto = (preco * 5/100)
precocomdesconto = (preco - desconto)
print(f'Você pagará R${precocomdesconto} pelo produto.')