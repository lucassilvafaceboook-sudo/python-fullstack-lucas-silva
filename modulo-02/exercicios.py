"""
=============================================================
MÓDULO 2 – Estruturas de Controle
Curso de Capacitação Full Stack – ITEAM

Aluno(a): <Lucas da Silva>
Data    : <21/10/2026>
=============================================================

INSTRUÇÕES:
  1. Substitua <SEU NOME COMPLETO AQUI> e <DATA DE ENTREGA> acima.
  2. Implemente cada função no espaço indicado com # SUA SOLUÇÃO AQUI.
  3. Não apague os comentários de orientação.
  4. Execute o arquivo para testar suas soluções antes de enviar.
  5. Salve este arquivo como modulo-02/exercicios.py, na sua cópia
     do repositório do curso.

COMO EXECUTAR:
  python exercicios.py
=============================================================
"""


# ==============================================================
# EXERCÍCIO 01 – Classificador de Temperatura
# Conceitos: if / elif / else, float(), input()
# ==============================================================
def ex01_classificador_temperatura():
    """
    Lê uma temperatura em Celsius e exibe sua classificação.

    Faixas:
        < 0        → ❄️ Congelante
        0  a 14   → 🥶 Frio
        15 a 24   → 😊 Agradável
        25 a 34   → ☀️ Quente
        >= 35     → 🔥 Muito quente
    """

    # Lógica para o Exercício 01:
    # Lembre-se de converter o input() para float()
    temperatura = float(input("Digite a temperatura em Celsius: "))

    # Estrutura condicional para classificar a temperatura
    if temperatura < 0:
        classificacao = "❄️ Congelante"
    elif temperatura <= 14:
        classificacao = "🥶 Frio"
    elif temperatura <= 24:
        classificacao = "😊 Agradável"
    elif temperatura <= 34:
        classificacao = "☀️ Quente"
    else:
        classificacao = "🔥 Muito quente"
        
    # Saída formatada
    print(f"Temperatura: {temperatura:.0f}°C")
    print(f"Classificação: {classificacao}")


# ==============================================================
# EXERCÍCIO 02 – Validador de Acesso
# Conceitos: if aninhado, comparação de strings
# ==============================================================
def ex02_validador_acesso():
    """
    Solicita usuário e senha e valida o acesso.

    Credenciais corretas:
        usuário → "admin"
        senha   → "iteam2025"
    """
# Solicita as credenciais ao utilizador
    usuario = input("Digite o usuário: ")
    senha = input("Digite a senha: ")

    # Verifica primeiro se o utilizador está correto
    if usuario == "admin":
        # Se o utilizador estiver correto, verifica a senha
        if senha == "iteam2025":
            print("✅ Acesso liberado. Bem-vindo!")
        else:
            print("❌ Senha incorreta.")
    else:
        # Se o utilizador estiver errado, não chega sequer a testar a senha
        print("❌ Usuário não encontrado.")

# ==============================================================
# EXERCÍCIO 03 – Tabuada Interativa
# Conceitos: for, range(), f-string com alinhamento
# ==============================================================
def ex03_tabuada():
    """
    Solicita um número inteiro e exibe sua tabuada de 1 a 10.
    """
    numero = int(input("Digite um número inteiro: "))

    print(f"\n=== Tabuada do {numero} ===")

    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i:>2} = {resultado:>3}")
# ==============================================================
# EXERCÍCIO 04 – Contador Regressivo
# Conceitos: while, print com end=
# ==============================================================
def ex04_contador_regressivo():
    """
    Solicita um número inteiro positivo e faz a contagem
    regressiva até 0, finalizando com '🚀 Lançamento!'.
    """
    # 1. Solicita o número inteiro
    numero = int(input("Digite um número inteiro positivo para a contagem: "))
    
    # 2. O laço repete ENQUANTO o número for maior ou igual a zero
    while numero >= 0:
        # end=" " faz com que o texto fique na mesma linha
        print(f"{numero}...", end=" ")
        
        # Subtrai 1 ao valor atual para a contagem descer
        numero -= 1
        
    # 3. Fora do laço (quando chega ao fim), quebra a linha (\n) e lança o foguetão!
    print("\n🚀 Lançamento!")


# ==============================================================
# EXERCÍCIO 05 – Buscador com break
# Conceitos: for, break, enumerate()
# ==============================================================
def ex05_buscador_break():
    """
    Percorre o estoque e localiza 'Monitor', exibindo
    sua posição. Usa break ao encontrar o item.
    """
    estoque = ["Teclado", "Mouse", "Webcam", "Monitor", "Headset", "Notebook"]

    # 1. Cria uma variável para memorizar se o produto foi achado
    encontrado = False

    # 2. O enumerate() serve para obtermos tanto a posição (índice) quanto o nome do produto
    for posicao, produto in enumerate(estoque):
        if produto == "Monitor":
            print(f"✅ Produto 'Monitor' encontrado na posição {posicao} do estoque.")
            encontrado = True
            # 3. O 'break' força o laço a parar imediatamente, pois já achámos o que queríamos
            break
            
    # 4. Fora do laço, verifica se a variável continuou False
    if not encontrado:
        print("❌ Produto não encontrado no estoque.")


# ==============================================================
# EXERCÍCIO 06 – Filtro de Dados com continue
# Conceitos: for, continue, None, acumuladores
# ==============================================================
def ex06_filtro_continue():
    """
    Percorre a lista de leituras, ignora os valores None
    com continue e calcula soma, média e total ignorado.
    """
    leituras = [12.5, None, 8.3, None, 15.0, 9.7, None, 11.2, 6.8, None]

    # 1. Cria as variáveis para guardar as contagens e a soma (os acumuladores)
    soma = 0
    quantidade_validos = 0
    total_ignorados = 0

    # 2. Percorre cada item da lista de leituras
    for leitura in leituras:
        # Se o valor for None, conta como ignorado e salta a vez
        if leitura is None:
            total_ignorados += 1
            # O 'continue' faz o laço ignorar o código abaixo e saltar logo para o próximo item!
            continue 
        
        # Se o código chegou até aqui, é porque o valor NÃO é None
        soma += leitura
        quantidade_validos += 1

    # 3. Calcula a média (apenas se houver números válidos para não dividir por zero)
    if quantidade_validos > 0:
        media = soma / quantidade_validos
    else:
        media = 0

    # 4. Exibe o relatório final
    print(f"📊 Relatório de Leituras:")
    print(f"Registos ignorados (None): {total_ignorados}")
    print(f"Soma dos valores válidos: {soma:.2f}")
    print(f"Média dos valores válidos: {media:.2f}")


# ==============================================================
# EXERCÍCIO 07 – Validação de Entrada com while
# Conceitos: while True, break, if/elif/else, float()
# ==============================================================
def ex07_validacao_nota():
    """
    Solicita a nota do aluno repetidamente até receber
    um valor válido (0.0 a 10.0), então exibe o conceito.
    """
    # 1. Laço infinito que só para quando receber uma nota válida
    while True:
        nota = float(input("Digite a nota do aluno (0.0 a 10.0): "))
        
        if 0.0 <= nota <= 10.0:
            # Se a nota for válida, quebra o laço e avança
            break
        else:
            # Se for inválida, avisa e o laço repete automaticamente
            print("❌ Nota inválida! Por favor, digite um valor entre 0 e 10.")

    # 2. Quando o laço é quebrado, o programa chega aqui para classificar a nota
    if nota >= 9.0:
        conceito = "A – Excelente"
    elif nota >= 7.0:
        conceito = "B – Bom"
    elif nota >= 5.0:
        conceito = "C – Regular"
    else:
        conceito = "D – Insuficiente"
        
    # 3. Exibe o resultado final
    print(f"\n✅ Nota validada: {nota:.1f}")
    print(f"🎓 Conceito Final: {conceito}")


# ==============================================================
# EXERCÍCIO 08 – Calculadora com try/except
# Conceitos: try/except/else/finally, ValueError, ZeroDivisionError
# ==============================================================
def ex08_calculadora_segura():
    """
    Solicita dois números e uma operação (+, -, *, /).
    Trata: ValueError, ZeroDivisionError, operação inválida.
    Usa else para exibir o resultado e finally para encerrar.
    """
    try:
        # 1. Solicitação de dados dentro do bloco que "tenta" (try) executar o código
        num1 = float(input("Digite o primeiro número: "))
        operacao = input("Digite a operação (+, -, *, /): ")
        num2 = float(input("Digite o segundo número: "))

        # 2. Verificação matemática
        if operacao == "+":
            resultado = num1 + num2
        elif operacao == "-":
            resultado = num1 - num2
        elif operacao == "*":
            resultado = num1 * num2
        elif operacao == "/":
            resultado = num1 / num2
        else:
            # Se a operação não for nenhuma das aceites, forçamos um erro de valor
            raise ValueError("Operação inválida! Símbolo não reconhecido.")

    # 3. Tratamento de Erros (except)
    except ValueError as erro:
        # Apanha o erro caso o utilizador digite letras em vez de números, ou o erro da operação inválida acima
        print(f"❌ Erro de valor: Certifique-se de que digitou números corretos e uma operação válida.")
    except ZeroDivisionError:
        # Apanha a tentativa impossível de dividir por zero
        print("❌ Erro matemático: Não é possível dividir por zero!")
    
    # 4. O bloco 'else' só é executado se NENHUM erro ocorrer no 'try'
    else:
        print(f"✅ Resultado: {num1} {operacao} {num2} = {resultado}")
        
    # 5. O bloco 'finally' é executado SEMPRE, independentemente de ter dado erro ou não
    finally:
        print("Calculadora encerrada.")


# ==============================================================
# EXERCÍCIO 09 – Padrão Numérico com for aninhado
# Conceitos: for aninhado, range(), print com end=
# ==============================================================
def ex09_padrao_numerico():
    """
    Gera o triângulo crescente:
        1
        1 2
        1 2 3
        ...
        1 2 3 4 5

    Desafio extra: gera também o triângulo decrescente logo abaixo.
    """
    print("Triângulo Crescente:")
    for i in range(1, 6):
        # Laço interno para imprimir de 1 até a linha atual (i)
        for j in range(1, i + 1):
            print(j, end=" ")
        print()  # Quebra de linha após cada nível do triângulo
        
    print("\nTriângulo Decrescente (Desafio):")
    for i in range(4, 0, -1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()


# ==============================================================
# EXERCÍCIO 10 – Jogo de Adivinhação
# Conceitos: while, contador, random, if/elif/else
# ==============================================================
def ex10_jogo_adivinhacao():
    """
    O computador sorteia um número entre 1 e 100.
    O usuário tem 7 tentativas para adivinhar.
    A cada erro, indica se o número é maior ou menor.
    """

    import random
    numero_secreto = random.randint(1, 100)
    tentativas = 7

    print("🎯 Bem-vindo ao Jogo de Adivinhação!")
    print("O computador pensou num número entre 1 e 100.")
    
    while tentativas > 0:
        try:
            palpite = int(input(f"Tens {tentativas} tentativa(s). Qual é o teu palpite? "))
            
            if palpite == numero_secreto:
                print("🎉 Parabéns! Acertaste no número secreto!")
                break
            elif palpite < numero_secreto:
                print("🔼 O número secreto é MAIOR.")
            else:
                print("🔽 O número secreto é MENOR.")
                
            tentativas -= 1
        except ValueError:
            print("❌ Erro: Por favor, digita apenas números inteiros.")
            
    if tentativas == 0:
        print(f"💀 Fim de jogo! O número secreto era {numero_secreto}.")


# ==============================================================
# EXERCÍCIO 11 – Verificador de Número Primo
# Conceitos: for, break, try/except, otimização com √n
# ==============================================================
def ex11_numero_primo():
    """
    Solicita um número inteiro positivo e verifica se é primo.
    Usa break ao encontrar o primeiro divisor.
    Trata ValueError e números negativos/zero.
    Otimização: verifica divisores somente até √n.
    """
    try:
            n = int(input("Digite um número inteiro positivo: "))
            
            if n <= 1:
                print(f"❌ {n} não é um número primo (deve ser maior que 1).")
            else:
                is_primo = True
                # Otimização: testa apenas até à raiz quadrada do número (n**0.5)
                for i in range(2, int(n**0.5) + 1):
                    if n % i == 0:
                        is_primo = False
                        break
                        
                if is_primo:
                    print(f"✅ {n} é um número PRIMO!")
                else:
                    print(f"❌ {n} não é um número primo (é divisível por outros números).")
                    
    except ValueError:
            print("❌ Erro: Entrada inválida. Digita um número inteiro positivo.")


# ==============================================================
# EXERCÍCIO 12 – Analisador de Senha Forte
# Conceitos: for, if, booleanos, métodos de string
# ==============================================================
def ex12_analisador_senha():
    """
    Analisa se uma senha atende aos critérios de segurança:
        - Mínimo 8 caracteres
        - Pelo menos 1 maiúscula
        - Pelo menos 1 minúscula
        - Pelo menos 1 dígito
        - Pelo menos 1 caractere especial: !@#$%^&*

    Exibe relatório com ✅ ou ❌ para cada critério.
    """
    senha = input("Digite a senha para análise: ")
    
    tem_tamanho = len(senha) >= 8
    tem_maiuscula = any(c.isupper() for c in senha)
    tem_minuscula = any(c.islower() for c in senha)
    tem_digito = any(c.isdigit() for c in senha)
    
    especiais = "!@#$%^&*"
    tem_especial = any(c in especiais for c in senha)

    print("\n📊 Relatório de Segurança da Senha:")
    print(f"{'✅' if tem_tamanho else '❌'} Mínimo de 8 caracteres")
    print(f"{'✅' if tem_maiuscula else '❌'} Pelo menos 1 letra maiúscula")
    print(f"{'✅' if tem_minuscula else '❌'} Pelo menos 1 letra minúscula")
    print(f"{'✅' if tem_digito else '❌'} Pelo menos 1 dígito numérico")
    print(f"{'✅' if tem_especial else '❌'} Pelo menos 1 caractere especial (!@#$%^&*)")
    
    if tem_tamanho and tem_maiuscula and tem_minuscula and tem_digito and tem_especial:
        print("\n🏆 STATUS: SENHA FORTE!")
    else:
        print("\n⚠️ STATUS: SENHA FRACA. Por favor, corrige os itens com ❌.")


# ==============================================================
# EXERCÍCIO 13 – Simulador de Caixa Eletrônico
# Conceitos: while, //, if/else, try/except
# ==============================================================
def ex13_caixa_eletronico():
    """
    Solicita um valor de saque (múltiplo de R$10, máx R$3.000).
    Calcula o menor número de cédulas: R$200, R$100, R$50, R$20, R$10.
    Trata entradas inválidas.
    """

    cedulas = [200, 100, 50, 20, 10]
    try:
            saque = int(input("Digite o valor do saque (Múltiplo de R$10, máx R$ 3.000): "))
            
            if saque <= 0 or saque > 3000:
                print("❌ Erro: O valor do saque deve estar entre R$ 10 e R$ 3.000.")
            elif saque % 10 != 0:
                print("❌ Erro: O valor não é múltiplo de R$ 10. Não temos moedas ou notas pequenas.")
            else:
                print(f"\n💵 Processando saque de R$ {saque:.2f}...")
                print("Cédulas a entregar:")
                
                for cedula in cedulas:
                    quantidade = saque // cedula  # Divisão inteira para saber quantas notas deste valor
                    if quantidade > 0:
                        print(f"  → {quantidade}x cédula(s) de R$ {cedula}")
                        saque = saque % cedula    # Resto da divisão é o que ainda falta pagar
                        
    except ValueError:
            print("❌ Erro: Digita um valor numérico inteiro.")


# ==============================================================
# EXERCÍCIO 14 – Leitura de Múltiplos Dados com Tratamento
# Conceitos: while, break, continue, try/except, pass
# ==============================================================
def ex14_leitura_notas_turma():
    """
    Lê notas de uma turma até o usuário digitar 'fim'.
    Ignora notas inválidas com continue + mensagem de aviso.
    Ao encerrar, exibe: total, média, maior e menor nota.
    """

    notas = []
    print("✏️ Lançamento de notas. Digita 'fim' para encerrar e calcular a turma.")
    
    while True:
        entrada = input("Digite a nota do aluno (0.0 a 10.0) ou 'fim': ").strip().lower()
        
        if entrada == 'fim':
            break
            
        try:
            nota = float(entrada)
            if nota < 0.0 or nota > 10.0:
                print("⚠️ Nota inválida! O valor deve estar entre 0.0 e 10.0.")
                continue # Pula para a próxima iteração do ciclo
                
            notas.append(nota)
            
        except ValueError:
            print("⚠️ Entrada inválida! Digita um número válido ou 'fim'.")
            continue # Pula para a próxima iteração do ciclo

    # Relatório final, mas apenas se a lista não estiver vazia
    if notas:
        total_soma = sum(notas)
        media = total_soma / len(notas)
        
        print("\n📊 --- RESUMO DA TURMA ---")
        print(f"Total de notas lidas: {len(notas)}")
        print(f"Média da turma: {media:.2f}")
        print(f"Maior nota registrada: {max(notas):.2f}")
        print(f"Menor nota registrada: {min(notas):.2f}")
        print("--------------------------")
    else:
        print("\nℹ️ Nenhuma nota válida foi registrada no sistema.")


# ==============================================================
# EXERCÍCIO 15 – Desafio Final: Menu de Sistema
# Conceitos: while True, if/elif/else, break, continue, try/except
# ==============================================================
def ex15_menu_sistema():
    """
    Menu interativo que permanece ativo até o usuário sair.

    Opções:
        [1] Conversor de temperatura (Celsius → Fahrenheit)
        [2] Verificador de número primo (versão simplificada)
        [3] Analisador de senha (apenas comprimento e dígito)
        [4] Calculadora segura (só +, -, *, /)
        [0] Sair

    Usa try/except em toda entrada do usuário.
    """
    while True:
        print("\n" + "=" * 29)
        print("   SISTEMA ITEAM - MENU    ")
        print("=" * 29)
        print("[1] Conversor de temperatura")
        print("[2] Verificador de número primo")
        print("[3] Analisador de senha")
        print("[4] Calculadora segura")
        print("[0] Sair")
        print("=" * 29)

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "0":
            print("👋 Encerrando o sistema. Até logo!")
            break
            
        elif opcao == "1":
            try:
                celsius = float(input("Digite a temperatura em Celsius: "))
                fahrenheit = (celsius * 9/5) + 32
                print(f"✅ {celsius:.1f}°C equivalem a {fahrenheit:.1f}°F")
            except ValueError:
                print("❌ Entrada inválida.")
                
        elif opcao == "2":
            try:
                n = int(input("Digite um número: "))
                if n > 1 and all(n % i != 0 for i in range(2, int(n**0.5) + 1)):
                    print(f"✅ {n} é um número primo!")
                else:
                    print(f"❌ {n} não é primo.")
            except ValueError:
                print("❌ Entrada inválida.")
                
        elif opcao == "3":
            senha = input("Digite a senha: ")
            # Versão simplificada: verifica tamanho >= 8 e se tem pelo menos um dígito numérico
            if len(senha) >= 8 and any(c.isdigit() for c in senha):
                print("✅ Senha válida (atende aos critérios básicos de comprimento e numerais).")
            else:
                print("❌ Senha fraca. (Deve ter 8+ caracteres e pelo menos um número).")
                
        elif opcao == "4":
            try:
                n1 = float(input("Primeiro número: "))
                op = input("Operação (+, -, *, /): ")
                n2 = float(input("Segundo número: "))
                
                if op == "+": print(f"Resultado: {n1 + n2}")
                elif op == "-": print(f"Resultado: {n1 - n2}")
                elif op == "*": print(f"Resultado: {n1 * n2}")
                elif op == "/": print(f"Resultado: {n1 / n2}")
                else: print("❌ Operação inválida.")
            except ZeroDivisionError:
                print("❌ Erro: Não é possível dividir por zero.")
            except ValueError:
                print("❌ Erro: Entrada numérica inválida.")
                
        else:
            print("❌ Opção não reconhecida! Escolha um número válido no menu.")


# ==============================================================
# EXECUÇÃO PRINCIPAL
# Descomente as chamadas dos exercícios que você já resolveu.
# ==============================================================
if __name__ == "__main__":
    print("\n" + "=" * 50)
    print("MÓDULO 2 – Estruturas de Controle")
    print(f"Aluno(a): <LUCAS DA SILVA>")
    print("=" * 50)

    # Descomente linha por linha conforme for resolvendo:
    # ex01_classificador_temperatura()
    # ex02_validador_acesso()
    # ex03_tabuada()
    # ex04_contador_regressivo()
    # ex05_buscador_break()
    # ex06_filtro_continue()
    # ex07_validacao_nota()
    # ex08_calculadora_segura()
    # ex09_padrao_numerico()
    # ex10_jogo_adivinhacao()
    # ex11_numero_primo()
    # ex12_analisador_senha()
    # ex13_caixa_eletronico()
    # ex14_leitura_notas_turma()
    ex15_menu_sistema()
