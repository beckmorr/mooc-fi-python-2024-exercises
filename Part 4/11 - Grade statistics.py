# Neste exercício, você escreverá um programa para imprimir estatísticas de notas para um curso universitário.
# O programa solicita ao usuário os resultados de diferentes alunos no curso.
# Esses resultados incluem pontos de exame e número de exercícios completados.
# O programa então imprime estatísticas baseadas nos resultados.
# Os pontos de exame são inteiros entre 0 e 20.
# O número de exercícios completados é um inteiro entre 0 e 100.
# O programa continua solicitando entradas até que o usuário digite uma linha em branco.
# Você pode assumir que todas as linhas contêm entradas válidas,
# o que significa que há dois inteiros em cada linha ou a linha está vazia.
# Exemplo de como os dados são digitados:
# Exemplo de saída:
# Pontos do exame e exercícios completados: 15 87
# Pontos do exame e exercícios completados: 10 55
# Pontos do exame e exercícios completados: 11 40
# Pontos do exame e exercícios completados: 4 17
# Pontos do exame e exercícios completados: 
# Estatísticas:
# Quando o usuário digita uma linha em branco, o programa imprime estatísticas.
# Essas estatísticas são formuladas da seguinte forma:
# Os exercícios completados são convertidos em pontos de exercício,
# de modo que completar pelo menos 10% dos exercícios concede um ponto,
# 20% concede dois pontos e assim por diante.
# Completar todos os 100 exercícios concede 10 pontos de exercício.
# O número de pontos de exercício concedidos é um valor inteiro, arredondado para baixo.
# A nota para o curso é determinada com base na seguinte tabela:
# Pontos de exame + pontos de exercício    Nota
# 0–14                                    0 (ou seja, reprovado)
# 15–17                                   1
# 18–20                                   2
# 21–23                                   3
# 24–27                                   4
# 28–30                                   5
# Há também um limite de pontos para exame.
# Se um aluno recebeu menos de 10 pontos no exame,
# ele automaticamente reprova o curso, independentemente do total de pontos.
# Com a entrada de exemplo acima, o programa imprimiria as seguintes estatísticas:
# Exemplo de saída:
# Estatísticas:
# Média de pontos: 14.5
# Porcentagem de aprovação: 75.0
# Distribuição de notas:
#   5:
#   4:
#   3: *
#   2:
#   1: **
#   0: *
# Números de ponto flutuante devem ser impressos com uma precisão de uma casa decimal.
# Nota: Este exercício não pede para você escrever funções específicas,
# então você não deve colocar nenhum código dentro de um bloco if __name__ == "__main__".
# Se alguma funcionalidade em seu programa, por exemplo, estiver na função principal,
# você deve incluir o código chamando essa função normalmente e não contê-la em um bloco if
# como nos exercícios que especificam certas funções.
# Dica:
# A entrada do usuário neste programa consiste em linhas com dois valores inteiros.
# Exemplo de saída:
# Pontos do exame e exercícios completados: 15 87

# Solução
exam_points_list = []
exercises_completed_list = []

while True:
    user_input = input("Exam points and exercises completed: ")
    
    if user_input.strip() == "":
        break

    exam_points, exercises_completed = map(int, user_input.split())
    
    exam_points_list.append(exam_points)
    exercises_completed_list.append(exercises_completed)

total_students = len(exam_points_list)
if total_students == 0:
    print("No data to display.")
else:
    total_points = 0
    pass_count = 0
    grade_distribution = [0] * 6

    for exam_points, exercises_completed in zip(exam_points_list, exercises_completed_list):
        exercise_points = min(exercises_completed // 10, 10)
        total_score = exam_points + exercise_points

        if exam_points < 10:
            grade = 0 
        else:
            if total_score < 15:
                grade = 0
            elif total_score < 18:
                grade = 1
            elif total_score < 21:
                grade = 2
            elif total_score < 24:
                grade = 3
            elif total_score < 28:
                grade = 4
            else:
                grade = 5

        total_points += total_score
        grade_distribution[grade] += 1
        
        if grade > 0:
            pass_count += 1

    points_average = total_points / total_students
    pass_percentage = (pass_count / total_students) * 100

    print("\nStatistics:")
    print(f"Points average: {points_average:.1f}")
    print(f"Pass percentage: {pass_percentage:.1f}")

    print("Grade distribution:")
    for grade in range(5, -1, -1):
        print(f"  {grade}: {'*' * grade_distribution[grade]}")
