# ============================================================
# ARQUIVO PRINCIPAL: main.py
# Sistema de Lançamento de Notas — Nível Fácil
# ============================================================

from funcoes.validacoes import validar_turma, validar_aluno, validar_nota
from funcoes.arquivo import salvar_nota, ler_notas

def obter_turma():
    while True:
        entrada = input("\nNome da turma: ")
        
        if entrada.strip().lower() == "sair":
            return None
            
        if validar_turma(entrada):
            return entrada.strip()
            
        print("❌ Turma inválida. O nome não pode estar vazio.")

def obter_aluno():
    while True:
        entrada = input("\nNome do aluno (ou 'sair'): ")
        
        if entrada.strip().lower() == "sair":
            return None
            
        if validar_aluno(entrada):
            return entrada.strip()
            
        print("❌ Nome inválido. Digite o nome e apelido do aluno.")

def obter_nota(numero_da_nota):
    while True:
        entrada = input(f"Nota {numero_da_nota}: ")
        
        if entrada.strip().lower() == "sair":
            return None
            
        nota = validar_nota(entrada)
        if nota is not None:
            return nota
            
        print("❌ Nota inválida. Digite um número entre 0 e 10.")


def main():
    print("=" * 45)
    print("  Sistema de Lançamento de Notas")
    print("  Digite 'sair' a qualquer momento para encerrar")
    print("=" * 45)

    # Passo 1: Obter a Turma
    turma = obter_turma()
    if turma is None:
        print("\nEncerrando o sistema. Até logo!")
        return

    # Passo 2: Loop Principal de Alunos
    while True:
        aluno = obter_aluno()
        if aluno is None:
            break

        # Coletar as notas (quebrando o loop caso digite 'sair' a meio)
        nota1 = obter_nota(1)
        if nota1 is None: break
        
        nota2 = obter_nota(2)
        if nota2 is None: break
        
        nota3 = obter_nota(3)
        if nota3 is None: break

        # Salvar e ler dados
        salvar_nota(turma, aluno, nota1, nota2, nota3)
        print("\n✔ Nota salva com sucesso!")
        
        ler_notas(turma)

    # Passo 3: Encerramento
    print("\nEncerrando o sistema. Até logo!")


if __name__ == "__main__":
    main()