# Questão: Verificação de Tabuleiro de Sudoku
#
# Escreva um programa que verifica se um tabuleiro de Sudoku 9x9 está correto.
# O programa deve verificar se:
# 1. Todas as linhas do tabuleiro contêm apenas números únicos de 1 a 9 (zeros são considerados células vazias).
# 2. Todas as colunas do tabuleiro contêm apenas números únicos de 1 a 9.
# 3. Todas as subgrades 3x3 dentro do tabuleiro (as regiões menores do Sudoku) contêm apenas números únicos de 1 a 9.
#
# Funções a serem implementadas:
# - check_row(sudoku: list, row_no: int) -> bool:
#     Verifica se a linha 'row_no' do tabuleiro contém apenas números únicos de 1 a 9.
#
# - check_column(sudoku: list, column_no: int) -> bool:
#     Verifica se a coluna 'column_no' do tabuleiro contém apenas números únicos de 1 a 9.
#
# - check_grid(sudoku: list, row_no: int, column_no: int) -> bool:
#     Verifica se a subgrade 3x3 começando na célula (row_no, column_no) contém apenas números únicos de 1 a 9.
#
# - sudoku_grid_correct(sudoku: list) -> bool:
#     Verifica se todas as linhas, colunas e subgrades 3x3 estão corretas, retornando True se o tabuleiro for válido e False caso contrário.
#
# Entrada:
# - Uma lista 2D de inteiros representando um tabuleiro de Sudoku 9x9. O tabuleiro pode conter zeros, que indicam células vazias.
#
# Saída:
# - Um valor booleano (True ou False) indicando se o tabuleiro é válido de acordo com as regras descritas.
#
# Exemplo de tabuleiro de entrada:
# sudoku1 = [
# [9, 0, 0, 0, 8, 0, 3, 0, 0],
# [2, 0, 0, 2, 5, 0, 7, 0, 0],
# [0, 2, 0, 3, 0, 0, 0, 0, 4],
# [2, 9, 4, 0, 0, 0, 0, 0, 0],
# [0, 0, 0, 7, 3, 0, 5, 6, 0],
# [7, 0, 5, 0, 6, 0, 4, 0, 0],
# [0, 0, 7, 8, 0, 3, 9, 0, 0],
# [0, 0, 1, 0, 0, 0, 0, 0, 3],
# [3, 0, 0, 0, 0, 0, 0, 0, 2]
# ]
#
# Saída esperada:
# False (pois há duplicatas na linha 1 e na coluna 1).
#
# Solução:
def check_row (sudoku: list, row_no: int):
    row = sudoku[row_no]
    checked_row = [row.count(i) for i in range(len(row))]
    for element in range(1, 9):
        if checked_row[element] > 1:
            return False
    return True

def check_column (sudoku: list, column_no: int):
    column_list = []
    for i in range (len(sudoku)):
        column_list.append(sudoku[i][column_no])
    checked_column = [column_list.count(i) for i in range (len(column_list))]
    for j in range(1, 9):
        if checked_column[j] > 1:
            return False
    return True

def check_grid (sudoku: list, row_no: int, column_no: int):
    subgrid_list = []
    for i in range (row_no, row_no+3):
        for j in range (column_no, column_no+3):
            subgrid_list.append(sudoku[i][j])
    checked_subgrid = [subgrid_list.count(i) for i in range (9)]
    for k in range(1,9):
        if checked_subgrid[k] > 1:
            return False
    return True

def sudoku_grid_correct (sudoku: list):
    for i in range(9):
        if not check_row(sudoku, i):
            return False
    for j in range(9):
        if not check_column(sudoku, j):
            return False
    for k in range(0, 9, 3):
        for l in range(0, 9, 3):
            if not check_grid(sudoku, k, l):
                return False
    return True

if __name__ == "__main__":
    sudoku1 = [
    [9, 0, 0, 0, 8, 0, 3, 0, 0],
    [2, 0, 0, 2, 5, 0, 7, 0, 0],
    [0, 2, 0, 3, 0, 0, 0, 0, 4],
    [2, 9, 4, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 7, 3, 0, 5, 6, 0],
    [7, 0, 5, 0, 6, 0, 4, 0, 0],
    [0, 0, 7, 8, 0, 3, 9, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 3],
    [3, 0, 0, 0, 0, 0, 0, 0, 2]
    ]

    print(sudoku_grid_correct(sudoku1))

    sudoku2 = [
    [2, 6, 7, 8, 3, 9, 5, 0, 4],
    [9, 0, 3, 5, 1, 0, 6, 0, 0],
    [0, 5, 1, 6, 0, 0, 8, 3, 9],
    [5, 1, 9, 0, 4, 6, 3, 2, 8],
    [8, 0, 2, 1, 0, 5, 7, 0, 6],
    [6, 7, 4, 3, 2, 0, 0, 0, 5],
    [0, 0, 0, 4, 5, 7, 2, 6, 3],
    [3, 2, 0, 0, 8, 0, 0, 5, 7],
    [7, 4, 5, 0, 0, 3, 9, 0, 1]
    ]

    print(sudoku_grid_correct(sudoku2))