# Leia uma distância em kilômetros e apresente-a convertida em milhas. A fôrmula
# de conversão é: M = K/1,61, sendo K a distância em quilômetros e M em milhas

distancia_Km = float(input("Digite a distância em Km: "))

distancia_Milhas = distancia_Km / 1.61

print(f"A distancia em Milhas é: {distancia_Milhas:.0f}")
