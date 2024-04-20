import os;

os.system("cls")
print("------------Programa Chinês-------------")

# função para saber o valor das parcelas
def calcularParcela(produto, valor, parcelas):
    valor = float(valor)
    parcelas = int(parcelas)
    valorParcela = valor / parcelas;
    print(f"O valor das parcelas do produto {produto} é R${valorParcela:.2f}");


produto = input("Digite o nome do produto: ")
valor = input("Digite o valor do produto: ")
parcelas = input("Digite as parcelas: ")

# chamar a função calcular parcelas
calcularParcela(produto,valor,parcelas)