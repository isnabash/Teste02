# Leia um valor de comprimento em polegadas e apresente-o convertido em
# centímetros. A fórmula de conversão é: C = P*2,54, sendo C o comprimento em
# centímetros e P o comprimento em polegadas.

valor_Polegadas = float(input("Digite um valor em comprimento: "))

valor_Centimetros = valor_Polegadas * 2.54

print(f"O valor em Centímetros é: {valor_Centimetros:.0f}")
