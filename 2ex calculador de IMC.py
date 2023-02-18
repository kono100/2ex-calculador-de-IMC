


#2. Faça uma função que receba o peso e altura de uma pessoa. Calcule e retorne o seu IMC
#(Índice de Massa Corporal) através da fórmula:

Peso = float(input("Digite o Seu Peso : "))

Altura = float(input("Digite a sua Altura : "))

IMC = Peso/(Altura*Altura)
print(f"O seu IMC é: {IMC:,.4f}")
