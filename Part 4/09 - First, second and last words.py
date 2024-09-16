# Escreva um código que defina três funções:
# 1. A primeira função deve retornar a primeira palavra de uma string, onde as palavras são separadas por espaços.
# 2. A segunda função deve retornar a segunda palavra da string, que aparece logo após a primeira palavra.
# 3. A terceira função deve retornar a última palavra da string, identificando-a a partir do final da frase.
#
# Depois, no bloco principal (__main__), utilize essas três funções para imprimir a primeira, a segunda e a última
# palavra de uma frase de exemplo fornecida.
#
# Dica: Para a última palavra, uma abordagem eficiente seria iterar pela string começando do fim, parando ao encontrar
# o primeiro espaço.

# Solução
# Function that returns the first word in the string, stopping at the first space (" ")
def first_word(string):
    first = ""
    for i in range(len(string)):
        if string[i] == " ":
            break
        first += string[i]
    return first

# Function that returns the second word by starting after the first word (after the first space)
def second_word(string):
    first_word_index = len(first_word(string)) + 1
    second = ""
    for i in range(first_word_index, len(string)):
        if string[i] == " ":
            break
        second += string[i]
    return second

# Function that returns the last word by iterating from the end of the string and stopping at the first space encountered
def last_word(string):
    last = ""
    for i in range(len(string)-1, 0, -1):
        if string[i] == " ":
            break
        last = string[i] + last
    return last
    
# You can test your function by calling it within the following block
if __name__ == "__main__":
    sentence = "once upon a time there was a programmer"
    print(first_word(sentence))
    print(second_word(sentence))
    print(last_word(sentence))