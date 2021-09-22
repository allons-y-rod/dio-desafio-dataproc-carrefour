with open("resultado_part-00000.txt", encoding="utf8") as file:
    resultado = file.read().split('\n')
    resultado = resultado[:10]
    output = ""
    output = '\n'.join(resultado)
    print(output)

with open('resultado.txt', 'w') as file:
    file.write(output)