'''
FIAP
Defesa Cibernética - 1TDCF - 2021
Development e Coding for Security
Prof. MS. Fábio H. Cabrini
Atividade: Checkpoint 01
Alunos
Nickolas Pereira dos Santos - RM 88103
Matheus Lambert Moreira - RM 87079
'''
RED   = "\033[1;31m"  
BLUE  = "\033[1;34m"
CYAN  = "\033[1;36m"
GREEN = "\033[0;32m"
RESET = "\033[0;0m"
BOLD    = "\033[;1m"
REVERSE = "\033[;7m"
YELLOW = "\033[1;33m"
MAGENTA = "\033[1;95m"
LRED = "\033[1;91m"
GREY = "\033[1;90m"

n = int(input(GREY .center(50) + 'Quantos números você deseja mostrar na sequência de Fibonnaci ? '))
if n < 2:
    print(GREEN .center(50) + "O número mínimo a ser escolhido é 2")
else:

    t1 = 0
    t2 = 1
    print(LRED .center(1) + '*'*156)
    print(YELLOW + '{}, {}'.format(t1, t2), end='')
    contagem = 3
    while contagem <= n:
        t3 = t1 + t2
        print(', {}'.format(t3), end='')
        t1 = t2
        t2 = t3
        contagem += 1
    print(BOLD .center(60) + ' Chegamos ao fim da sua solicitação, obrigado!')
    print(LRED + '*'*156)