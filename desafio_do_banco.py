menu = '''
[ 1 ] DEPOSITO
[ 2 ] SAQUES
[ 3 ] EXTRATO
[ 0 ] SAIR
=>>> '''
balance = 0
limit = 500
extract = ''
number_withdrawals = 0
LIMET_WITHDRAWALS = 3

while True:
    option = input(menu)
    if option == '1':
        try:
            value = float(input('Informe o valor do deposito:'))
        except ValueError:
            print('Valor \033[1;31mINCORRETO.\033[m Tente novamente! ')
            continue
        if value > 0:
            balance += value
            extract += f'DEPOSITO:{value:.2f}\n'
            print(f'Valor depositado \033[1;32m{value:.2f}R$\033[m')
        else:
            print('Operação \033[1;31mFALHOU!\033[m O valor informado é invalido tente novamente.')

    elif option == '2':
        value = float(input('Informe o valor de saque: '))
        exceeded_balance = value > balance
        exceeded_limit = value > limit
        exceeded_withdraw = number_withdrawals >= LIMET_WITHDRAWALS
        if exceeded_balance:
            print('A operação \033[1;31mFALHOU!\033[m Você não tem saldo suficiênte.')
        elif exceeded_limit:
            print('A operação \033[1;31mFALHOU!\033[m O valor do saques excedeu o limite.')
        elif exceeded_withdraw:
            print('Operação \033[1;31mFALHOU!\033[m Numero maximo de saques excedido.')
        elif value > 0:
            balance -= value
            extract += f'SAQUE: R${value:.2f}\n'
            number_withdrawals += 1
            print(f'Saque de \033[1;32m{value:.2f}R$\033[m realizado com sucesso.')
        else:
            print('A operação \033[1;31mFALHOU!\033[m O valor informado é invalido.')

    elif option == '3':
        print('\n==========EXTRATO==========')
        print('\n\033[1;31mNÂO\033[m foram realizadas movimentações.'if not extract else extract)
        print(f'\nSALDO: \033[4;32mR${balance:.2f}\033[m')
        print('====================')
    elif option == '0':
        break
    else:
        print('Operação \033[1;31mINVALIDA\033[m, por favor selecione novamente a operação desejada:')