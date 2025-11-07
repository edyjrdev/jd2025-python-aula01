"""
Instruções:
O programa deve começar solicitando ao usuário que insira seu nome.
Em seguida, o programa deve pedir ao usuário para inserir o valor do seu salário. Considere que este valor pode ser um número decimal.
Depois, o programa deve solicitar a porcentagem do bônus recebido pelo usuário, que também pode ser um número decimal.
O cálculo do KPI do bônus de 2024 é de 1000 + salario * bônus
Finalmente, o programa deve imprimir uma mensagem no seguinte formato: "Olá [nome], o seu valor bônus foi de 5000".
Exemplo de Saída:
Se o usuário digitar "Luciano" como nome, "5000" como salário e "1.5" como bônus, o programa deve imprimir:
"""

# CONSTANTE
BONUS_GERAL = 1000

# Entradas
nome = input('Digite seu nome: ')
salario_str = input('Informe o valor do seu salário: ')
bonus_str = input('Informe o valor percentual do seu bônus:')

# processamento 
salario = float(salario_str)
bonus = float(bonus_str)
kpi = BONUS_GERAL + (salario * bonus)

# saida
print(f'Olá {nome}, o seu valor bônus foi de {kpi}')