# Função para calcular a média de uma disciplina
# variáveis Disciplina, Nota1Bimestre, Nota2Bimestre
# Terá que calcular a média
# Se a média >= 7 foi aprovado
# Senão foi reprovado

def calcularMedia():
    import os;
    os.system("cls")
    
    print("--------------------------------------------------Calcular a média de uma disciplina--------------------------------------------------")
    disciplina = input("Digite qual a Disciplina: ")
    notaPrimeiroBimestre = float(input("Digite qual a Nota do 1° Bimestre: "))
    notaSegundoBimestre = float(input("Digite qual a Nota do 2° Bimestre: "))
    media = (notaPrimeiroBimestre + notaSegundoBimestre) / 2
    
    print(f"As notas tiradas na sua disciplina: {disciplina} foram {notaPrimeiroBimestre} e {notaSegundoBimestre}")
    print(f"A média da sua Disciplina: {disciplina} foi de {media}")
    if media >= 7:

        print(f"Parabéns meu(inha) fofo(a) você teve uma média de {media} e você Passou na matéria de {disciplina}")
    else:

        print(f"Que pena meu(inha) fofo(a) você teve uma média de {media} e você Reprovou na matéria de {disciplina}")   
        print(f"Se concentre na sua recuperação!")   
    resposta = input("Você deseja sair[S + Enter] ou Continuar[qualquer teclas ('-S') + Enter]")
    if resposta == "S" or "s":
        print("Tchauzinho meu(inha) lindão(ona)")
    else:
        calcularMedia();

calcularMedia()