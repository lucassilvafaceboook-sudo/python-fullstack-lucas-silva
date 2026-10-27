# 1. Define o valor inicial em graus Celsius pedido no exercício
celsius = 36.5

# 2. Aplica a fórmula de conversão para Fahrenheit: F = (C * 9/5) + 32
fahrenheit = (celsius * 9/5) + 32

# 3. Aplica a fórmula de conversão para Kelvin: K = C + 273.15
kelvin = celsius + 273.15

# 4. Exibe os três valores formatados na tela
print(f"Temperatura em Celsius: {celsius:.1f}°C")
print(f"Temperatura em Fahrenheit: {fahrenheit:.1f}°F")
print(f"Temperatura em Kelvin: {kelvin:.2f} K")