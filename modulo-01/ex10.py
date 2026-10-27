# Dados fornecidos pelo exercício
capacidade_caminhao = 850
peso_caixa = 32

# 1. Calcula quantas caixas completas cabem usando divisão inteira (//)
caixas_completas = capacidade_caminhao // peso_caixa

# 2. Calcula o peso que sobra (o resto da divisão) usando o módulo (%)
peso_restante = capacidade_caminhao % peso_caixa

# 3. Exibe os resultados com mensagens claras
print(f"O camião comporta {caixas_completas} caixas completas.")
print(f"O peso restante que não completa uma caixa é de {peso_restante} kg.")git remote -v