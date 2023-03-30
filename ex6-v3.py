qtde  = int(input('Informe a quantidade comprada: '))
valorUnit = float(input('Informe o valor unitário: '))
desconto = float(input('Informe o desconto: '))

totalSemDesconto = qtde * valorUnit
totalComDesconto = (qtde * valorUnit) * (1 - desconto/100)

print(f'O total com desconto será R$ {totalComDesconto:.2f}')

