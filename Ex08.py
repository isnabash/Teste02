# Leia um valor de volume em metros cúbicos e apresente-o convertido em litros
# A fórmula de conversão é L = 1000*M, sendo L o volume em litros e M o volume em
# metros cúbicos!

metro_cubico = float(input(" Digite um valor em Metros Cúbicos: "))

litro = 1000 * metro_cubico

print(f"O valor convertido em litro é: {litro:.1f}")