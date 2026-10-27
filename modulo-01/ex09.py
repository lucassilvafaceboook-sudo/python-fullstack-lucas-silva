# Solicita o nome e guarda como texto (string)
nome = input("Qual é o seu nome? ")

# Solicita a iadade e converte imediatamente para inteiro (int)
idade = int(input("Qual  é a sua idade? "))

# Calcula o ano de nascimento aproximado (usando 2026 como ano atual)
ano_nascimento = 2026 - idade

# Exibe a mensagem formatada com f-string
print(f"Olá {nome}, você tem {idade} anos, e nasceu por volta de {ano_nascimento}.")