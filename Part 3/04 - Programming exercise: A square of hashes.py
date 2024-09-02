#Por favor, escreva uma função chamada quadrado_de_hashes(tamanho), que receba um argumento inteiro. 
# A função deve imprimir um quadrado de caracteres "#" com o tamanho especificado no argumento.
#
# Exemplo de uso:
# quadrado_de_hashes(1)
# print()
# quadrado_de_hashes(3)
#
# Saida esperada:
# #
# 
# ###
# ###
# ###
#
# Solução
def quadrado_de_hashes(tamanho):
    for i in range(tamanho):
            print("#" * tamanho)
            
if __name__ == "__main__":
    quadrado_de_hashes(5)

