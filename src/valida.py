def leiaNumeroInteiro(msg):
    while True:
        try:
            numero = int(input(msg))
        except (ValueError, TypeError):
            print('ERRO! Por favor, digite um número válido.')
            continue
        except KeyboardInterrupt:
            print('Usuário preferiu não digitar esse número.')
            return 0
        else:
            return numero
        