# Leia uma distância em graus e apresente-o convertido em radianos.
# A fórmula de conversão é: R = G * Pi/180, sendo G o ângulo em graus e R em radianos
# e Pi 3.14

angulo_Graus = float(input("Digite um Ângulo em Graus: "))

angulo_Radiano = angulo_Graus * 3.14 / 180

print(f"O Ângulo em Radiano é: {angulo_Radiano:.1f}")
