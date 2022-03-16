# Leia uma velocidade em m/s (metros por segundo) e apresente-a convertida em km/h
# (quilômetros por hora). A fórmula de conversão é: K = M * 3.6, sendo K a velocidade
# em km/h e M em m/s

velocidade_Metros = float(input('Digite a velocidade em metros: '))

velocidade_KM = (velocidade_Metros * 3.6)

print(f'A velocidade em KM é: {velocidade_KM:.0f}')
