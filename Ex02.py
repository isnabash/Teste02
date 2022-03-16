# Leia uma distância em milhas e apresente-a convertida em quilômetros. A fórmula de
# conversão é: K = 1,61 * M, sendo K a distância em quilômetros e M em milhas.

distancia_Milhas = float(input("Digite uma distância em Milhas: "))

distancia_KM = 1.61 * distancia_Milhas

print(f"A distância em Kilometros é: {distancia_KM:.0f}")
