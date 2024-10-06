# Questão: Implemente uma função chamada 'transpose' que recebe uma matriz (lista de listas) como entrada e 
# retorna a matriz transposta. A transposição de uma matriz envolve inverter suas linhas e colunas. 
# Por exemplo, dada a matriz de entrada:
# [[1, 2, 3],
#  [4, 5, 6],
#  [7, 8, 9]]
# a matriz transposta deve ser:
# [[1, 4, 7],
#  [2, 5, 8],
#  [3, 6, 9]]
# A função deve modificar a matriz original em vez de criar uma nova. 
# Ao final da execução, a matriz transposta deve ser impressa.
#
# Solução:
def transpose(matrix: list):
    transposed_matrix = [[0] * len(matrix) for row in range(len(matrix))]
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            transposed_matrix[i][j] = matrix[j][i]

    for i in range(len(matrix)):
        for j in range(len(matrix)):
            matrix[i][j] = transposed_matrix[i][j]

    print(matrix)

if __name__ == "__main__":
    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9],
    ]
    transpose(matrix)