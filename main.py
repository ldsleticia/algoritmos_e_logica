def imprimir_impares():
    fim = int(input('Digite o último número a imprimir: '))
    inicio = 0
    while inicio <= fim:
        if inicio % 2 != 0:
            print(inicio)
        inicio += 1


def imprimir_dez_primeiros_multiplos_de_tres():
    inicio = 0
    multiplos = 0

    while multiplos < 10:
        if inicio % 3 == 0:
            multiplos += 1
            print(inicio)
        inicio += 1


def menu():
    print('escolha o exercicio a ser exibido')
    print('1 para imprimir impares')
    print('2 para imprimir os dez primeiros multiplos de 3')

    escolha = int(input())

    match escolha:
        case 1:
            imprimir_impares()
        case 2:
            imprimir_dez_primeiros_multiplos_de_tres()


if __name__ == '__main__':
    menu()
