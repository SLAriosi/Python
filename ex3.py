# Como fazer aparecer na tela, e nós podermos inserir o nome que nós digitarmos

nome = input("Digite seu nome: ")
print (f"O nome digitado é: {nome}")

salario = input("Digite seu salário: ")
salario = float(salario)

# Essa parte do :.2f não consegue reconhecer string como um meio de colocar ,00 no valor;
print (f"O nome digitado é: {nome} e seu salário é R${salario:.2f}")
print (type(salario))