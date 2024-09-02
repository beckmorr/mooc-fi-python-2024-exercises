#Por favor, escreva um programa que peça ao usuário para digitar uma string. 
#O programa então imprime todas as substrings que terminam com o último caractere, do tamanho mais curto para o mais longo.
#Veja o exemplo abaixo.
#Saída de exemplo:
#Por favor, digite uma string: teste
#e
#te
#ste
#este
#teste

# Solução
input_string = str(input("Por favor, digite uma string: "))
word = ""
index = 0

while index < len(input_string):
    word = input_string[len(input_string) - len(input_string) - index - 1] + word
    print(word)
    index += 1
