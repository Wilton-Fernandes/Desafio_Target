print("_______________________________________________________________________________________________________")
print(" Questão 2 - Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos")
print("  2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem ")
print(" que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem ")
print(" avisando se o número informado pertence ou não a sequência.")
print("")
valor = int(input('Digite um valor: '))
fibonacci = []
fibonacci.append(0)
fibonacci.append(1)

i = 1 

while fibonacci[len(fibonacci)-1] < valor:
    fibonacci.append(fibonacci[i] + fibonacci[i-1])
    i+= 1

print(f'Sequencia de Fibonacci: {fibonacci}')
if valor in fibonacci:
    print(f'{valor} Pertence a sequência de Fibinacci')
else:
    print(f'{valor} Não pertence a sequência de Fibonacci')

print("_______________________________________________________________________________________________________")

print(" Questão 3 - Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, ")
print(" na linguagem que desejar, que calcule e retorne:")

print("• O menor valor de faturamento ocorrido em um dia do mês;")
print("• O maior valor de faturamento ocorrido em um dia do mês;")
print("• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.")

import json

with open("dados.json", encoding='utf-8') as dados_json:
    dados = json.load(dados_json)

valores = []

for i in dados:
    valores.append(i["valor"])
while 0 in valores:
    valores.remove(0)
print("")
print(f'Menor valor diário: {min(valores)}') 
print(f'Maior valor diário: {max(valores)}')
n = 0
media =sum(valores)/len(valores)
for i in valores:
    if i > media:
        n+=1
print(f'Houve {n} dias que o faturamento foi superior a média mensal no valor de {media}')


print("_______________________________________________________________________________________________________")
print("Questão 4 - Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:")
print("")
print("SP – R$67.836,43")
print("RJ – R$36.678,66")
print("MG – R$29.229,88")
print("ES – R$27.165,48")
print("Outros – R$19.849,53")

print("Escreva um programa na linguagem que desejar onde calcule o percentual de representação que") 
print("cada estado teve dentro do valor total mensal da distribuidora.")

sp = 67836.43
rj = 36678.66
mg = 29229.88
es = 27165.48
outros = 19849.53

somatoria = sp + rj + mg + es + outros
print("")
print(f'SP – R$67.836,43 - equivalente a {sp / somatoria * 100} %')
print(f'RJ – R$36.678,66 - equivalente a {rj / somatoria * 100} %')
print(f'MG – R$29.229,88 - equivalente a {mg / somatoria * 100} %')
print(f'ES – R$27.165,48 - equivalente a {es / somatoria * 100} %')
print(f'Outros – R$19.849,53 - equivalente a {outros / somatoria * 100} %')

print("_______________________________________________________________________________________________________")
print("Questão 5 - Escreva um programa que inverta os caracteres de um string.")

palavra = input("Digite uma palavra: ")
print("")
p =len(palavra)
print("A palavra invertida é: ", end="")
while p > 0 :
    print(palavra[p-1], end="")
    p -= 1
print("")
print("_______________________________________________________________________________________________________")
