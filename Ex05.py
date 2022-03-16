# Leia um ângulo em radianos e apresente-o convertido em graus. A fórmula de
# conversão é: G = R*180/Pi, sendo G o ângulo em graus e R em radianos e Pi 3.14

angulo_Radiano = float(input("Digite um Ângulo em Radiano: "))

angulo_Graus = angulo_Radiano * 180 / 3.14

print(f"O Ângulo em Graus é: {angulo_Graus:.0f}")
