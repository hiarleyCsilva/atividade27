# Exercício Python 27: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo,
# desconsiderando os espaços. DICA: VEJA SOBRE FUNÇÃO REPLACE(), LOWER() E UMA FORMA DE INVERTER OS CARACTERES. 
def eh_palindromo(frase):
 
    frase = frase.replace(" ", "").lower()

    frase_invertida = frase[::-1]

 
    if frase == frase_invertida:
        return True
    else:
        return False


frase = input("Digite uma frase: ")

if eh_palindromo(frase):
    print("A frase é um palíndromo!")
else:
    print("A frase não é um palíndromo.")
