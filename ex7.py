import os;

os.system("cls")
print("----------------Programa Chinês-----------------------")
def calcularParcelas():
    produto = input("Produto: ")
    valor = float(input("Valor: "))
    numeroParcelas = int(input("Numero de Parcelas: "))
    juros = float(input("Juros Mensal: "))
    
    # calcular as parcelas
    valorParcelas = valor / numeroParcelas;
    total = 0;
    for i in range(1, numeroParcelas + 1):
        if i > 1:
            valorParcelas = valorParcelas + (valorParcelas * juros / 100);
        print(f"Parcela {i}: R${valorParcelas:.2f}")
        total = total + valorParcelas;
    print(f"O valor total pago no {produto} foi de {total:.2f}")
    print("--------------------------------------------");
    resposta = input("Você deseja sair[S + Enter] ou Continuar[qualquer teclas ('-S') + Enter]")
    if resposta == "S":
        print("Tchauzinho meu(inha) lindão(ona)")
    else:
        calcularParcelas();

calcularParcelas()