def cuadrado(x, valor_opcional=23):
    return x * x

cuadrado(2)
print(cuadrado(2))

for i in range(10):
    print(f'{i} al cuadrado es {cuadrado(i)}')
    