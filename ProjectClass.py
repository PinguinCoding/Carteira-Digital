class carteira:

    def adicionar_fundos(self, valor, saldo):
        nsaldo = saldo + valor
        print('Operação realizada com sucesso!')
        return nsaldo

    def remover_fundos(self, valor, saldo):
        if saldo < valor:
            print('Operação não autorizada, saldo insuficiente!')
            return saldo
        else:
            nsaldo = saldo - valor
            print('Operação realizada com sucesso!')
            return nsaldo


saldo = 0
c = 1

while c == 1:
    print('O que deseja fazer?')
    print('(1) Depositar')
    print('(2) Sacar')
    print('(3) Encerrar')
    op = int(input('Digite sua opção: '))
    minha_carteira = carteira()

    if op == 1:
        valor = float(input('Insira o valor que deseja depositar: R$'))
        saldo = minha_carteira.adicionar_fundos(valor, saldo)
        print(f'Seu saldo atual é R${saldo}')
        m = 0
        while m == 0:
            c = int(input('Deseja fazer outra operação? (1) Sim (2) Não: '))

            if c == 1:
                print('='*50)
                break

            elif c == 2:
                print('FIM')
                break

            else:
                print('Opção inválida! Tente novamente')

    elif op == 2:
        valor = float(input('Insira o valor que deseja sacar: R$'))
        saldo = minha_carteira.adicionar_fundos(valor, saldo)
        print(f'Seu saldo atual é R${saldo}')
        m = 0
        while m == 0:
            c = int(input('Deseja fazer outra operação? (1) Sim (2) Não: '))

            if c == 1:
                print('='*50)
                break

            elif c == 2:
                print('FIM')
                break

            else:
                print('Opção inválida! Tente novamente')

    elif op == 3:
        print('FIM')
        break

    else:
        print('Opção inválida! Tente novamente')