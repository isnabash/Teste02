# Leia um valor de massa em quilograma e apresente-o convertido em libras.
# A fórmula de conversão é: L = K/0.45, sendo K a massa em quilograma e L massa em libras

massa_kilo = float(input("Digite um valor em kilograma: "))

libras = massa_kilo/0.45

print(f"O valor convertido em libras é: {libras:.2f}")
