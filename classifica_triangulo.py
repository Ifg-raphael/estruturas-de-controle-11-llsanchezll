# Sua solução aqui
A = float(input("Digite o valor do lado A: "))
B = float(input("Digite o valor do lado B: "))
C = float(input("Digite o valor do lado C: "))
# Verifica se os lados formam um triângulo
if A + B <= C or A + C <= B or B + C <= A:
    print("não é um triângulo")
    exit()
if A == B == C:
    print("equilátero")
elif A == B or B == C or A == C:
    print("isósceles")
else:
    print("escaleno")
# --- IGNORE ---