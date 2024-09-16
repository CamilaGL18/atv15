# Crie um programa que receba dois números e uma operação (soma, subtração, multiplicação ou divisão) e execute a operação desejada.

num1 = float(input("digite o primeiro numero"))
num2 = float(input("digite o segundo numero"))

operaçao = str(input("digite a operaçao que deseja utilizar soma, multiplicaçao, subtração, divisão"))

if operaçao =="soma":
    print(num1 + num2)
elif operaçao == "multiplicação":
    print(num1 * num2)
elif operaçao == "subtração":
    print(num1 - num2)
elif operaçao == "divisão":
    print(num1 / num2)

