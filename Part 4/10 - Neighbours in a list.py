# Enunciado:
# Dado um vetor de inteiros, desenvolva uma função que determine o comprimento
# da maior sequência consecutiva de números vizinhos (ou seja, números cuja
# diferença entre valores adjacentes é igual a 1). A sequência pode crescer
# tanto em valores ascendentes quanto descendentes, desde que cada número
# consecutivo seja vizinho do anterior. A função deve retornar o tamanho da maior
# sequência identificada.

# Exemplo:
# Para a lista de entrada [1, 2, 3, 0, 1, 2, 3, 4, 5, 3, 4, 5, 1, 2, 3], a maior
# sequência de vizinhos consecutivos é [1, 2, 3, 4, 5], e o programa deve retornar 5.

def longest_series_of_neighbours(int_list: list):
    # Lista que armazenará a maior sequência de números vizinhos
    longest_series_list = []
    
    # Lista temporária para armazenar a sequência atual de números vizinhos
    current_series = []
    
    # Percorre todos os elementos da lista
    for i in range(len(int_list)):
        # Se for o primeiro elemento ou a diferença entre o elemento atual e o anterior for 1
        if i == 0 or abs(int_list[i] - int_list[i - 1]) == 1:
            # Adiciona o elemento atual à sequência atual
            current_series.append(int_list[i])
        else:
            # Se a sequência atual for a maior até o momento, armazena como a maior sequência
            if len(current_series) > len(longest_series_list):
                longest_series_list = current_series
            # Reinicia a sequência atual começando do elemento atual
            current_series = [int_list[i]]

    # Verifica uma última vez após o loop se a sequência atual é a maior
    if len(current_series) > len(longest_series_list):
        longest_series_list = current_series

    # Retorna o comprimento da maior sequência de números vizinhos
    return len(longest_series_list)

# Exemplo de uso:
if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]
    print(longest_series_of_neighbours(my_list))  # Saída: 5
