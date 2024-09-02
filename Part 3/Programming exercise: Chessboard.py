# Por favor, escreva uma função chamada tabuleiro_de_xadrez, 
# que imprime um tabuleiro de xadrez feito de uns e zeros. 
# A função recebe um argumento inteiro, que especifica o comprimento do lado do tabuleiro.
#  Veja os exemplos abaixo para mais detalhes:
# Exemplo de uso:
#tabuleiro_de_xadrez(3)
#print()
#tabuleiro_de_xadrez(6)
# Saída esperada:
# 101
# 010
# 101
# 
# 101010
# 010101
# 101010
# 010101
# 101010
# 010101
#
# Dicas:
# Você pode usar o operador de módulo (%) para alternar entre 0 e 1.

# Solução
# A função chessboard() imprime um tabuleiro de xadrez feito de uns e zeros.
def chessboard(num):
    for i in range(num):
        for j in range(num):
            if (i + j) % 2 == 0:
                print("1", end="")
            else:
                print("0", end="")
        print()

# Testing the function
if __name__ == "__main__":
    chessboard(3)
