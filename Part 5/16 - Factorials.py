# Questão:
# Implemente duas funções que retornem um dicionário com os fatoriais de todos os números de 1 até n. 
# Uma função (factorials) deve utilizar uma abordagem recursiva para calcular os fatoriais, 
# enquanto a outra (factorials2) deve usar uma abordagem iterativa.
#
# O código deve conter:
# 1. A função `factorials(n: int) -> dict`: que retorna um dicionário 
# onde as chaves são os números de 1 a n, 
# e os valores são os respectivos fatoriais calculados recursivamente.
#
# 2. A função `factorials2(n: int) -> dict`: que retorna um dicionário semelhante, mas com os fatoriais 
# calculados de forma iterativa.
#
# 3. A função auxiliar `iterative_calculate_factorial(num: int)`: que retorna o 
# fatorial de `num` usando um laço.
#
# 4. A função auxiliar `recursive_calculate_factorial(num: int)`: que retorna o 
# fatorial de `num` usando recursão.
#
# No final, o programa deve calcular e armazenar os fatoriais de 1 a 5 usando a 
# função recursiva e de 1 a 6 usando a função iterativa.
# Imprima os valores do fatorial de 1, 3 e 5 da função recursiva e o valor do 
# fatorial de 6 da função iterativa.
#
# Solução:
def factorials (n: int) -> dict:
    factorials_dict = {}
    for i in range(1, n+1):
        factorials_dict[i] = recursive_calculate_factorial(i)
    return factorials_dict

def factorials2 (n: int) -> dict:
    factorials_dict = {}
    for i in range(1, n+1):
        factorials_dict[i] = iterative_calculate_factorial(i)
    return factorials_dict

def iterative_calculate_factorial (num: int):
    fat = 1
    for i in range(1, num+1):
        fat *= i
    return fat

def recursive_calculate_factorial (num: int):
    if num == 0 or num == 1:
        return 1
    return num * recursive_calculate_factorial(num-1)

if __name__ == "__main__":
    k = factorials(5)
    j = factorials2(6)
    print(k[1])
    print(k[3])
    print(k[5])
    print(j[6])