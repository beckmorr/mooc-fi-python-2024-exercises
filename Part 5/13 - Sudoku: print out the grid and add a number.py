# Este exercício consiste em implementar um programa que manipula um tabuleiro de Sudoku. 
# O programa deve ser capaz de exibir o tabuleiro e permitir a adição de números em células específicas.
#
# Objetivos:
# 1. Implemente uma função `print_sudoku(sudoku)` que recebe uma matriz 9x9 representando um tabuleiro de Sudoku 
#    e o imprime no formato adequado:
#    - Células vazias (com valor 0) devem ser representadas por "_".
#    - O tabuleiro deve ser formatado de forma que haja espaçamento extra entre os subquadrantes 3x3.
#
# 2. Implemente uma função `add_number(sudoku, row_no, column_no, number)` que permita adicionar um número específico 
#    em uma célula no tabuleiro.
#    - O parâmetro `sudoku` será a matriz 9x9 que representa o tabuleiro.
#    - Os parâmetros `row_no` e `column_no` indicam a linha e coluna onde o número será inserido.
#    - O parâmetro `number` é o número a ser adicionado.
#
# 3. No programa principal, crie um tabuleiro de Sudoku vazio (todas as células contendo o valor 0). 
#    - Exiba o tabuleiro usando a função `print_sudoku`.
#    - Adicione três números em diferentes posições usando a função `add_number`.
#    - Exiba o tabuleiro atualizado.
#
# Solução:
def print_sudoku(sudoku: list):
    for i in range(len(sudoku)):
        if i % 3 == 0 and i != 0:
            print()
        for j in range(len(sudoku)):
            if sudoku[i][j] == 0:
                print('_ ', end='')
            else:
                print(str(sudoku[i][j]) + " ", end='')
            if j == 2 or j == 5 and j != 0:
                 print(" ", end='')
        print()

def add_number (sudoku: list, row_no: int, column_no: int, number: int):
    sudoku[row_no][column_no] = number

if __name__ == "__main__":
    sudoku = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
    print_sudoku(sudoku)
    add_number(sudoku, 0, 0, 2)
    add_number(sudoku, 1, 2, 7)
    add_number(sudoku, 5, 7, 3)
    print("\nThree numbers added:")
    print_sudoku(sudoku)