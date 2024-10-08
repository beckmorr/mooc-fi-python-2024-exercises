#Problema: Encontre todas as Substrings de 3 Caracteres
#Descrição:
#Escreva um programa que receba uma palavra e um caractere como entrada. O programa deve imprimir todas as 
#substrings da palavra que têm exatamente 3 caracteres e que começam com o caractere especificado pelo usuário.
#Você pode assumir que a palavra de entrada tem pelo menos três caracteres.
#
#Exemplo de Entrada e Saída:
#
#Entrada:
#    Palavra: mammoth
#   Caractere: m
#
#Saída:
#    mam
#    mmo
#    mot
#
#Entrada:
#    Palavra: banana
#    Caractere: n
#
#Saída:
#    nan
#
# Solução
input_string = str(input("Palavra: "))
character = str(input("Caractere: "))

if not input_string or not character:
    print("Por favor insira uma palavra e uma caractere válidos.")
else:
    found = False
    for i in range(len(input_string) - 2):
        if input_string[i] == character:
            print(input_string[i:i+3])
            found = True
        
    if not found:
        print("A palavra não tem o caractere que você inseriu!")
        
