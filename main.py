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


def tabuada():
    fim = int(input('Digite o numero que deseja saber a tabuada: '))
    inicio = int(input('Digite de onde devemos começar: '))
    while inicio <= 10:
        print(f"{inicio} x {fim} = {fim * inicio}")
        inicio += 1


def multiplica_com_soma():
    primeiro_numero = int(input('digite o número que quer multiplicar: '))
    segundo_numero = int(
        input('digite a quantidade de vezes que quer multiplicar: '))
    resultado = 0

    while segundo_numero > 0:
        resultado += primeiro_numero
        segundo_numero -= 1
    print(resultado)


def divisao_com_subtracao():
    dividendo = 2
    divisor = 2
    quociente = 0
    resto = dividendo

    while resto >= divisor:
        resto -= divisor
        quociente += 1
    print('sou o quociente ', quociente)
    print('sou o resto ', resto)


def questoes_certas():
    pontos = 0
    questao = 1

    while questao <= 3:
        resposta = input(f'Resposta da questao {questao} ')
        if questao == 1 and resposta.lower() == "b":
            pontos += 1
        if questao == 2 and resposta.lower() == "a":
            pontos += 1
        if questao == 3 and resposta.lower() == "d":
            pontos += 1
        questao += 1
    print(f'voce acertou {pontos} questoes')


def media():
    x = 1
    soma = 0

    while x <= 5:
        n = int(input('digite um numero: '))
        soma = soma + n
        x += 1
    print(f'a média dos valores é {soma / 5}')


def soma_juros():
    deposito_inicial = int(input('digite o valor do deposito inicial: '))
    deposito_mensal = int(input('digite o valor do deposito mensal: '))
    taxa_de_juros = int(input('digite a taxa de juros: '))
    tempo = 24
    soma = 0

    while tempo > 0:
        soma = soma + (deposito_inicial * (taxa_de_juros / 100) + deposito_mensal)
        print(f'Voce ganhou R$ {soma} de juros o mes passado')
        somei_com_juros = soma + deposito_inicial
        tempo -= 1
    print(f'Voce tem R$ {somei_com_juros} no final dos {tempo} meses')


def menu():
    print('escolha o exercicio a ser exibido')
    print('1 para imprimir impares')
    print('2 para imprimir os dez primeiros multiplos de 3')
    print('3 para imprimir a tabuada de um numero')
    print('4 para multiplicar utilizando a soma')
    print('5 para dividir utilizando a subtração')
    print('6 para questoes certas')
    print('7 para media')
    print('8 para juros')

    escolha = int(input())

    match escolha:
        case 1:
            imprimir_impares()
        case 2:
            imprimir_dez_primeiros_multiplos_de_tres()
        case 3:
            tabuada()
        case 4:
            multiplica_com_soma()
        case 5:
            divisao_com_subtracao()
        case 6:
            questoes_certas()
        case 7:
            media()
        case 8:
            soma_juros()


if __name__ == '__main__':
    menu()
