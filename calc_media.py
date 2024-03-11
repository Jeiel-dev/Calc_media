def num_digit():
    numero = int(input("Digite um numero "))
    return numero

num_calc = int(input("Quantos numeros serão calc. a media? "))

numeros = [num_digit() for _ in range(num_calc)]
soma = sum(numeros)
media = soma / len(numeros)
print (f"A media entre {numeros} é {media}")