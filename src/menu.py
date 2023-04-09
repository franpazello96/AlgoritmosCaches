import inicial
import lru

while True: 
    inicial.cabecalho("MENU PRINCIPAL")
    resposta = inicial.menu()
    if resposta == -1:
        print("modo de simulação")
    elif resposta == 0:
        print("Programa encerrado!")
        break
    elif resposta in range(1,101):
       lru.lista(resposta)
    else:
        print("Número inválido.")
