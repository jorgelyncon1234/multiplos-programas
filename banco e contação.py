import uuid
nome = ''
bv = 0
ID = int
numero = int
marcela = ('marcela')
savot =''
novo = ''
salvo = ''
saldo = 0.0
depv =0.0
saque =0.0
programa = ''
while True:   

 print('------PROGRAMAS------\n 1 para CONTADOR \n 2 para banco   \n 5 para informações adicionais de cada programa.\n 6 ENCERRAR PROGRAMA.')
 try:
  programa = int(float(input()))    
 except:
     print('ERRO! tente novamente de acordo com as informações.')           
 if programa == 1: 

  while True:
    print('====-+CONTADOR+-/====')
    escolha = int(input('ALTERNATIVAS DE CALCULOS:\n 1:LUCRO \n 2:SOMA \n 3:DIVISÃO \n 4:SAIR \n FAÇA SUA ESCOLHA; '))

    if escolha == 1:
        print('=LUCRO=')
        ganho = int(input('quanto vc ganha: '))
        gasto = int(input('quanto vc gasta: '))
        lucro = ganho - gasto
        print('então seu lucro é:', lucro)

    elif escolha == 2:
        print('===SOMA===')
        n1 = int(input('primeiro número desejado a ser somado: '))
        n2 = int(input('segundo número a ser acrescentado: '))
        soma1 = n1 + n2
        print('o resultado de sua soma é:', soma1)

    elif escolha == 3:
        print('==DIVISÃO==')
        d1 = int(input('dividendo: '))
        d2 = int(input('divisor: '))
        divisao = d1 / d2
        print('resultado:', divisao)

    elif escolha == 4:
        print('obrigado por usar.')
        break
    

    else:
        print('INCORRETO')
 elif programa == 2:
    
    while True:
     print('/=/=/=/=/BANCO/=/=/=/=/')
     if bv == 0  :
      nome = str(input('me diga seu nome:'))
      numero = int(input('insira seu numero:'))
      
      print ('seu id é',uuid)
      bv =+ 1 
     else:
      print (' bem vindo')
        
     escobanco = int(input("escolha: \n 1 DEPOSITAR \n 2 SACAR \n 3 transferir \n 4 ver meu perfil/informações \n 6 SAIR "))
     print(saldo)
     

     if escobanco ==1 :
        depv = float(input('digite o valor que desejas depositar: '))
        depv = round(depv, 2)
        print ('valor depositado:',depv)
        saldo += depv 
        print ('SALDO ATUAL: ',saldo )
     elif escobanco ==6:
          print('volte sempre!')
          break
     elif escobanco ==2:
          print('SALDO ATUAL',saldo)
          saque = float(input('Deseja sacar quanto?;'))
          saldo -= saque 
          print('você sacou:',saque)
          print('SALDO RESTANTE:',saldo)
     elif escobanco ==3:
         print ('saldo atual:',saldo,'\n DESEJA TRANSFERIR PARA USUÁRIO SALVO OU REGISTRAR UM NOVO?\n1para salvo \n2 para novo')
         escotrans = int(input())
         if escotrans ==1:
             print('selecione entre os usuários salvos:','\nmarcela')
             savot = (input('digite o nome do usuário á receber:'))
             transfer = int(input('valor a ser transferido'))
             if savot == 'marcela' :
                 if saldo <transfer:
                     print('erro,saldo insuficiente;')
                     break
                 print('valor de ',transfer,'será transferido á ',savot,':')
                 saldo -= transfer 
                 
     elif escobanco ==4:
         print(nome,numero,uuid)         
          
          
          
 if programa ==6:
    print('obrigado por usar o programa!')
    break
 