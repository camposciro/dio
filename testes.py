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
            value = float(input('Informe o valor do deposito: '))
        except ValueError:
            print('Tente novamente')
            continue
        if value > 0:
            balance += value
            extract += f'DEPOSITO:{value:.2f}\n'
            print(f'Valor depositado {value:.2f}R$.')
        else:
            print('Operação FALHOU! O valor informado é invalido.Tente novamente.')
