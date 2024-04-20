# Fazer a tela ser limpa automaticamente
# Importar Pacote do SO
import os;

# Aqui vamos limpar a tela
os.system("cls");
salario = input("Digite seu salário: ")
aumento = input("Digite a % do seu aumento (apenas o número sem %): ")

salario = float(salario);
aumento = float(aumento);

novoSalario = salario + ( salario * aumento / 100)

print(f"Seu novo salário é de: R${novoSalario:.2f}")