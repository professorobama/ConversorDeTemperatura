#Conversor de Temperatura:
#Desenvolva um programa que converta temperaturas de Celsius para Fahrenheit e vice-versa. Use um laço de repetição for para iterar sobre as conversões.

# Define a função para converter Celsius para Fahrenheit
def celsius_para_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Define a função para converter Fahrenheit para Celsius
def fahrenheit_para_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

# Define as opções de conversão
opcoes = ["Celsius para Fahrenheit", "Fahrenheit para Celsius"]

# Imprime as opções de conversão
print("Escolha uma opção:")
for i, opcao in enumerate(opcoes, start=1):
    print(f"{i}. {opcao}")

# Solicita ao usuário a escolha da conversão
escolha = int(input("Digite o número correspondente à opção desejada: "))

# Verifica a escolha do usuário e executa a conversão correspondente
if escolha == 1:
    # Conversão de Celsius para Fahrenheit
    for celsius in range(-100, 101, 10):
        fahrenheit = celsius_para_fahrenheit(celsius)
        print(f"{celsius}°C = {fahrenheit:.1f}°F")
elif escolha == 2:
    # Conversão de Fahrenheit para Celsius
    for fahrenheit in range(-148, 213, 18):
        celsius = fahrenheit_para_celsius(fahrenheit)
        print(f"{fahrenheit}°F = {celsius:.1f}°C")
else:
    print("Opção inválida. Por favor, escolha uma opção válida.")

#Este código permite que o usuário escolha entre converter de Celsius para Fahrenheit ou de Fahrenheit para Celsius. Em seguida, ele utiliza um laço de repetição for para iterar sobre um intervalo de temperaturas e realiza as conversões, imprimindo os resultados na saída padrão.