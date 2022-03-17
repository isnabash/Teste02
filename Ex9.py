# Leia um valor de volume em litros e apresente-o convertido em metros cúbicos.
# A fórmula de conversão é: M = L/1000, sendo L o volume em litros e M o volume em
# metros cúbicos

volume_litros = float(input("Digite um valor de volume em litros: "))

metros_cubicos = volume_litros/1000

print(f"O valor em metros cúbicos é: {metros_cubicos:.2f}")