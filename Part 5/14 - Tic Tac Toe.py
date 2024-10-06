# Implementar uma função chamada 'play_turn' que simula a 
# jogada de um jogador em um tabuleiro de jogo.
# O tabuleiro é representado por uma lista de listas (matriz), 
# onde cada posição pode conter uma peça "X", "O" ou estar vazia 
# (representada por uma string vazia "").
# A função 'play_turn' recebe os seguintes parâmetros:
# - 'game_board': uma matriz representando o tabuleiro atual.
# - 'x': a coordenada x (coluna) da jogada, representando a posição da peça na horizontal.
# - 'y': a coordenada y (linha) da jogada, representando a posição da peça na vertical.
# - 'piece': uma string ("X" ou "O") que representa a peça a ser colocada na posição.
# A função deve verificar se a posição no tabuleiro está vazia e, 
# se estiver, colocar a peça naquela posição.
# Se a jogada for válida (posição vazia), a função retorna True. 
# Caso contrário (posição ocupada ou fora dos limites), retorna False.
# Em seguida, a função deve ser testada com um exemplo de tabuleiro e uma jogada.
#
# Solução
def  play_turn(game_board: list, x: int, y: int, piece: str):
    for i in range(len(game_board)):
        if i == y:
            for j in range(len(game_board[i])):
                if j == x:
                    if game_board[i][j] == "":
                        game_board[i][j] = piece
                        return True
    return False


if __name__ == "__main__":
    game_board = [['O', 'O', 'X'], ['O', '', ''], ['X', 'O', 'X']]
    print(play_turn(game_board, 3, 0, "X"))
    print(game_board)