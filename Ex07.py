# Leia um valor de comprimento em centímetros e apresente-o convertido em polegadas.
# A fórmula de conversão é: P = C/2.54, sendo C o comprimento em centímetros e P o
# comprimento em polegadas.

comprimento_Centim = float(input("Digite o comprimento em centímetro: "))

comprimento_Polegadas = comprimento_Centim / 2.54

print(f"O comprimento em polegadas é: {comprimento_Polegadas:.1f}")
