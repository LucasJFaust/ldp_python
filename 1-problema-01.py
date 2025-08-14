"""
Escreva um programa que retorne o valor por hora de um funcionário.
O programa deve receber o salário mensal do funcionário e a quantidade de horas trabalhadas no mês.
"""
salario_mensal = float(input("Digite o salário mensal do funcionário: "))
horas_trabalhadas_dia = 8
horas_trabalhadas_mês = horas_trabalhadas_dia * 22  # Considerando 22 dias úteis no mês
print(f"Quantidade de horas trabalhadas no mês: {horas_trabalhadas_mês} horas")
valor_por_hora = salario_mensal / horas_trabalhadas_mês
print(f"O valor por hora do funcionário é: R$ {valor_por_hora:.2f}")