# ============================================================
# MÓDULO: arquivo.py
# Responsável por salvar e ler notas no formato JSON
# ============================================================

import json
import os

def salvar_nota(turma, aluno, nota1, nota2, nota3):
    # Passo 1: Calcular a média e arredondar a 2 casas
    media = round((nota1 + nota2 + nota3) / 3, 2)

    # Passo 2: Montar o dicionário do registo
    registro = {
        "aluno": aluno,
        "nota1": nota1,
        "nota2": nota2,
        "nota3": nota3,
        "media": media
    }

    # Passo 3: Montar o caminho do arquivo (substituindo espaços por underscores)
    nome_arquivo = turma.replace(" ", "_") + ".json"
    caminho = os.path.join("notas", nome_arquivo)

    # Garantir que a pasta "notas" existe antes de tentar guardar
    os.makedirs("notas", exist_ok=True)

    # Passo 4: Verificar se o arquivo já existe para ler os dados atuais
    if os.path.exists(caminho):
        with open(caminho, 'r', encoding='utf-8') as arquivo:
            dados = json.load(arquivo)
    else:
        dados = []

    # Passo 5: Adicionar o novo aluno à lista
    dados.append(registro)

    # Passo 6: Salvar a lista atualizada no arquivo JSON
    with open(caminho, 'w', encoding='utf-8') as arquivo:
        json.dump(dados, arquivo, indent=4, ensure_ascii=False)


def ler_notas(turma):
    # Passo 1: Montar o caminho
    nome_arquivo = turma.replace(" ", "_") + ".json"
    caminho = os.path.join("notas", nome_arquivo)

    # Passo 2: Verificar se existe
    if not os.path.exists(caminho):
        print(f"\nAinda não há registos para a {turma}.")
        return

    # Passo 3: Carregar dados
    with open(caminho, 'r', encoding='utf-8') as arquivo:
        dados = json.load(arquivo)

    # Passo 4: Exibir os dados formatados
    print(f"\n─── Registros da {turma} ───────────────────")
    for reg in dados:
        print(f"Aluno : {reg['aluno']}")
        print(f"Nota 1: {reg['nota1']}  |  Nota 2: {reg['nota2']}  |  Nota 3: {reg['nota3']}")
        print(f"Média : {reg['media']}")
        print("────────────────────────────────────────────")