# Exercício Python 26: Desenvolva um programa que leia o primeiro termo e a razão de uma Pogreçao Aritimetica.
# No final, mostre os 10 primeiros termos dessa progressão.

print("progresão aritmetica")

termo = int(input("digite o termo da progressão:"))
razao = int(input("digite a razão dessa progressão:"))

for i in range(0, 10):
    progressao = termo + i * razao
    print(f"progressão e {i+1}: {progressao}")