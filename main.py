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
    deposito_inicial = float(input('Digite o valor do depósito inicial: '))
    deposito_mensal = float(input('Digite o valor do depósito mensal: '))
    taxa_de_juros = float(input('Digite a taxa de juros: '))
    taxa_de_juros /= 100
    tempo = 24
    saldo = deposito_inicial
    meses = 1

    while meses <= tempo:
        juros = saldo * taxa_de_juros
        saldo += juros + deposito_mensal
        print(
            f"No mês {meses}, você ganhou R$ {juros:.2f} de juros. Seu saldo atual é R$ {saldo:.2f}")
        meses += 1

    print(f"\nApós {tempo} meses, seu saldo final será de R$ {saldo:.2f}")


def pagamento_de_juros():
    divida_total = float(input('Digite o valor da dívida: '))
    deposito_mensal = float(input('Digite o valor do pagamento mensal: '))
    taxa_de_juros = float(input('Digite a taxa de juros (em porcentagem): '))
    taxa_de_juros /= 100
    divida_parcial = divida_total
    tempo = 0
    total_pago = 0
    total_juros = 0

    while divida_parcial > 0:
        juros = divida_parcial * taxa_de_juros
        divida_parcial += juros - deposito_mensal
        tempo += 1
        total_pago += deposito_mensal
        total_juros += juros

    print(f"O número de meses para pagar a dívida é: {tempo}")
    print(f"O total pago foi de: R$ {total_pago:.2f}")
    print(f"O total de juros pago foi de: R$ {total_juros:.2f}")


def enquanto_for_true():
    numero_inicial = 0

    while True:
        digite = int(input('digite um numero: '))
        if digite == 0:
            break
        else:
            numero_inicial += digite
    print(numero_inicial)


def caixa_registradora():
    valor_do_item = 0
    total = 0

    while True:
        codigo_do_item = int(
            input('digite o código do item ou 0 para exibir o total: '))

        if codigo_do_item == 0:
            print(f"O total da compra é de R$ {total:.2f}")
            break

        qtde_do_item = int(input('digite a quantidade de itens: '))

        match codigo_do_item:
            case 1:
                valor_do_item = 0.50
            case 2:
                valor_do_item = 1.00
            case 3:
                valor_do_item = 4.00
            case 5:
                valor_do_item = 7.00
            case 9:
                valor_do_item = 8.00
            case _:
                print('Código invalido')

        total += valor_do_item * qtde_do_item

def conta_cedulas():
    valor = int(input('Digite o valor a pagar: '))
    cedulas = 0
    atual = 50
    apagar = valor
    while True:
        if atual <= apagar:
            apagar -= atual
            cedulas +=1
        else:
            print(f'{cedulas} cedulas de R${atual}')
            if apagar == 0:
                break
            if atual == 50:
                atual = 20
            elif atual == 20:
                atual = 10
            elif atual == 10:
                atual = 5
            elif atual == 5:
                atual = 1
            cedulas = 0


def ex_bonus():
    while True:
        print('0 para sair')
        print('1 para calcular o diametro do circulo')
        print('2 para calcular a area do circulo')
        print('3 para calcular a circunferencia do circulo')
        print('4 para exibir todos os calculos')
        escolha = int(input())

        if escolha == 0:
            break

        raio = int(input('digite o raio do circulo: '))

        diametro = raio * 2
        area = 3.14 * (raio ** 2)
        circunferencia = 2 * 3.14 * raio

        match escolha:
            case 1:
                print(f'o diametro do circulo é {diametro}')
            case 2:
                print(f'a area do circulo é {area}')
            case 3:
                print(f'a circunferência do circulo é {circunferencia}')
            case 4:
                print(
                    f"O diametro é {diametro}, a area é {area}, a circunferencia é {circunferencia}")


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
    print('9 para pagamento de juros')
    print('10 para enquanto for true')
    print('11 para caixa registradora')
    print('99 para ex bonus')

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
        case 9:
            pagamento_de_juros()
        case 10:
            enquanto_for_true()
        case 11:
            caixa_registradora()
        case 99:
            ex_bonus()


if __name__ == '__main__':
    menu()
