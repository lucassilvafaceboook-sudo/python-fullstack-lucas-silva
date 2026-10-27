# ============================================================
# MÓDULO: validacoes.py
# Responsável por todas as funções de validação do sistema
# ============================================================

def validar_turma(nome_turma):
    texto = nome_turma.strip()
    # Verifica se está vazio ou é igual a "sair"
    if texto == "" or texto.lower() == "sair":
        return False
    return True

def validar_aluno(nome_aluno):
    texto = nome_aluno.strip()
    # Verifica se está vazio ou é igual a "sair"
    if texto == "" or texto.lower() == "sair":
        return False
    
    # Verifica se tem pelo menos duas palavras (nome e sobrenome)
    palavras = texto.split()
    if len(palavras) < 2:
        return False
        
    return True

def validar_nota(valor_digitado):
    # Substitui a vírgula por ponto para facilitar a conversão
    texto = str(valor_digitado).replace(",", ".")
    
    try:
        nota = float(texto)
        # Verifica se está dentro do intervalo permitido [0.0, 10.0]
        if 0.0 <= nota <= 10.0:
            return nota
        else:
            return None
    except ValueError:
        # Se não for um número válido, a conversão falha
        return None