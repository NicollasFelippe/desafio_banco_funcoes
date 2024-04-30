saldo = 0.00
extratos = []
numero_de_depositos = 0
numero_de_saques = 0
opcao = ["D","E","S",'X',"U","C","L"]
usuario = []
nro_atual = 1
agencia = "0001"
conta_corrente = []

#deposito
def deposito(novo_saldo,extrato):
    valor_deposito = float(input("Informe o valor que você deseja depositar \n R$:"))
    if valor_deposito < 0:
        valor_deposito = float(input("Você não pode informar um valor negativo\n Informe o valor que deseja depositar:\n"))
    novo_saldo += valor_deposito
    extrato.append(f'deposito no valor de - R${valor_deposito}')
    return novo_saldo,extrato

#saques
def saque(numero_de_saques=0, saldo=0.00,extrato=extratos):
    valor_saque = float(input('Informe o valor que deseja sacar \n R$:'))
    if numero_de_saques >= 3:
      print("Você já excedeu o limite de saques diários \n ")
      return None,None,None
    elif valor_saque > saldo:
      print(f'Não será possível sacar este valor R${valor_saque}, pois seu saldo é insuficiente')
      return None,None,None
    elif valor_saque > 500:
      print(f'Você só pode sacar até R$ 500,00 \n Operação encerrada')
      return None, None, None
    elif valor_saque <= 0:
      print(f'Você não pode sacar um valor negativo\n Operação encerrada')
      return None, None, None
    else:
        saldo -= valor_saque
        numero_de_saques += 1
        extrato.append(f'saque realizado no valor de - R${valor_saque}')
        return saldo, numero_de_saques,extrato

#imprime extratos
def imprimir_extrato(saldo, *, extrato=extratos):
      print('========== EXTRATO ==========')
      for item in extrato:
        print(item)

      print('=============================')
      print(f"Saldo atual R$:{saldo}")

#cadastro de usuario
def cadastro_de_usuario():
  endereco = []
  print(f"Bem vindo usuário, á seguir efetuaremos seu cadastro")
  CPF = input("Por favor, informe seu CPF: \n")
  if any(dados_usuario['CPF'] == CPF for dados_usuario in usuario):
    print("Você já é cadastro, portanto não podá ter outro cadasto \n Operação encerrada!")
    return None
  else:
    nome = input("informe seu Nome completo: \n")
    data_nasc = input("informe sua data de nascimento DD/MM/YYYY: \n")
    logradouro = input("Informe seu endereço (logradouto - numero - bairro - cidade/Sigla Estado) \n")
    endereco.append(logradouro)
    usuario.extend([{"CPF":CPF,"nome":nome,'data_nasc':data_nasc,"endereco":logradouro}])
    print("Parabéns, conta criada com sucesso!")
    return usuario

#Cria conta
def criar_conta():
    global nro_atual
    global conta_corrente

    valida_CPF = input('Informe seu CPF para efetuarmos a criação da conta\n')

    # Verifica se o CPF já está cadastrado
    if not any(dados_usuario['CPF'] == valida_CPF for dados_usuario in usuario):
        print("Você ainda não é cadastrado, por favor efetue seu cadastro antes de criar uma conta.")
    else:
        # Encontra o usuário correspondente ao CPF
        usuario_encontrado = next(dados_usuario for dados_usuario in usuario if dados_usuario['CPF'] == valida_CPF)

        # Cria a nova conta corrente associada ao usuário encontrado
        nova_conta = {'conta': nro_atual, 'agencia': agencia, 'usuario': usuario_encontrado}

        # Incrementa o número atual de contas
        nro_atual += 1

        # Adiciona a nova conta corrente à lista de contas
        conta_corrente.append(nova_conta)

        print("Conta criada com sucesso!")

    return conta_corrente

#Lista contas criadas
def listar_contas():
   for cadastros in conta_corrente:
      print("====================================================================")
      for chave, valor in cadastros.items(): 
        print(f'{chave}: {valor}')

#Rodando o código
while True:
  menu = input("""
    Usuário informe a opção que você deseja utilizar:
          [D] - Deposito
          [S] - Saque
          [E] - Extrato
          [U] - Crir Usuário
          [C] - Criar Conta Corrente
          [L] - Listar Conta Corrente
          [X] - Sair \n
            """).upper()

  if menu not in opcao:
    print("Opcao invalida")
    menu

  if menu == 'D':
    saldo, extratos = deposito(saldo, extratos)


  if menu == "S":
    retorno_saque = saque(numero_de_saques, saldo, extratos)
    if retorno_saque[0] is not None:  # Verifica se o saldo foi atualizado
        saldo, numero_de_saques, extratos = retorno_saque


  if menu == "E":
    imprimir_extrato(saldo,extrato=extratos)

  if menu == "U":
    cadastro_de_usuario()

  if menu == "C":
    criar_conta()

  if menu == 'L':
    listar_contas()

  if menu == "X":
    break