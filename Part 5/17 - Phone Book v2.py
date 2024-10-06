# Enunciado:
# 
# Escreva um programa que simula uma agenda de contatos com as seguintes funcionalidades:
# 
# 1. Buscar contato: 
#    - Quando o comando 1 é inserido, o programa solicita o nome de um contato. 
#    - Se o contato existir, todos os números de telefone associados a ele são exibidos. 
#    - Se o contato não existir, exibe a mensagem "no number".
# 
# 2. Adicionar contato: 
#    - Quando o comando 2 é inserido, o programa solicita o nome de 
#      um contato e um número de telefone. 
#    - Se o contato já existir, o número é adicionado à lista de números. 
#    - Se o contato não existir, o programa cria o contato e associa o número informado a ele.
# 
# 3. Sair do programa: 
#    - Quando o comando 3 é inserido, o programa encerra a execução 
#      exibindo a mensagem "quitting...".
# 
# Regras:
# - O programa deve armazenar múltiplos números de telefone para um único contato.
# - O programa continuará em execução até que o comando 3 seja inserido.
# 
# Exemplo de Interação:
# command(1 search, 2 add, 3 quit): 2
# name: Alice
# number: 12345
# ok!
#
# command(1 search, 2 add, 3 quit): 2
# name: Alice
# number: 67890
# ok!
#
# command(1 search, 2 add, 3 quit): 1
# name: Alice
# 12345
# 67890
#
# command(1 search, 2 add, 3 quit): 1
# name: Bob
# no number
#
# command(1 search, 2 add, 3 quit): 3
# quitting...
#
# Solução
contacts = {}

while True:
    n = int(input("command(1 search, 2 add, 3 quit): "))

    if n == 1:
        name = str(input("name: "))
        if name in contacts:
            for number in contacts[name]:
                print(number)
        else:
            print("no number")

    if n == 2:
        name = str(input("name: "))
        num = str(input("number: "))
        if name not in contacts:
            contacts[name] = []
        contacts[name].append(num)
        print("ok!")
        
    if n == 3:
        print("quitting...")
        break
