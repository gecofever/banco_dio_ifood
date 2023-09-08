menu = """
[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair
=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
limite_saques = 3

while True:
  opcao = input(menu)

  if opcao == '1':
    valor = float(input('Informe valor do deposito: '))

    if valor > 0:
      saldo += valor
      extrato = extrato + f'Deposito R$: {valor:.2f}\n'

    else:
      print('Operação falhou. Valor Inválido!')

  elif opcao == '2':
    valor = float(input('Informe valor do saque: '))

    excedeu_saldo = valor > saldo
    execedeu_limite = valor > limite
    exedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
      print('Operação falhou, Saldo insuficiente.')
    elif execedeu_limite:
      print('Operação falhou, valor do saque excede o limite')
    elif exedeu_saques:
      print('OPeração falhou, numero de saques excedido')

    elif valor > 0:
      saldo -= valor
      extrato += f'Saque R$: {valor:.2f}\n'
      numero_saques += 1

    else:
      print('Operação falhou, valor informado inválido')

  elif opcao =='3':
    print('************ Extrato ************')
    print('Não foram realizadas movimentações.' if not extrato else extrato)
    print(f'\nSaldo: R$ {saldo:.2f}')

  elif opcao == '4':
    break

  else:
    print('Operação Invalida, escolha a opção correta.')