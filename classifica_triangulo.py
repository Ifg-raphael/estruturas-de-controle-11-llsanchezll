# Sua solução aqui
A = float(input("Digite o valor do lado A: "))
B = float(input("Digite o valor do lado B: "))
C = float(input("Digite o valor do lado C: "))
# Verifica se os lados formam um triângulo
if A < B + C and B < A + C and C < A + B:
    if A == B == C:
        print("equilátero")
    elif A == B or B == C or A == C:
        print("isósceles")
    else:
        print("escaleno")
else:
    print("não é um triângulo")