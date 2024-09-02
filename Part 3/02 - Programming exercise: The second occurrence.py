#Descrição:
#Por favor, escreva um programa que encontre a segunda ocorrência de uma substring.
#Se não houver uma segunda (ou primeira) ocorrência, o programa deve imprimir uma mensagem apropriada.
#Neste exercício, as ocorrências não podem se sobrepor. Por exemplo, na string "aaaa", a segunda ocorrência da substring "aa" está no índice 2.
#Alguns exemplos de comportamento esperado:
#
#Exemplo de Saída
#Por favor, digite uma string: abcabc
#Por favor, digite uma substring: ab
#A segunda ocorrência da substring está no índice 3.
#
#Exemplo de Saída
#Por favor, digite uma string: methodology
#Por favor, digite uma substring: o
#A segunda ocorrência da substring está no índice 6.
#
#Exemplo de Saída
#Por favor, digite uma string: aybabtu
#Por favor, digite uma substring: ba
#A substring não ocorre duas vezes na string.
#
# Solução
string = input("Por favor, digite uma string: ")
substring = input("Por favor, digite uma substring: ")

first_occurrence = string.find(substring)

if first_occurrence == -1:
    print("A substring não ocorre na string.")
else:
    second_occurrence = string.find(substring, first_occurrence + len(substring))

    #O segundo parâmetro do método find() em Python especifica o índice a partir do qual a 
    #busca pela substring deve começar dentro da string principal.
    #Supondo a palavra : bebbela
    #E a substring: be
    #first_occurence = 0
    #second_occurrence = string.find(substring, 0 + 2) a partir do *índice 2*: A string a partir do índice 2 é "bbela".
    #second_occurrence = 3
    
    if second_occurrence == -1:
        print("A substring não ocorre duas vezes na string.")
    else:
        print(f"A segunda ocorrência da substring está no índice {second_occurrence}.")

