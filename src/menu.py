import inicial
import lru

# Inicializa o cache vazio
cache = []

while True: 
    inicial.cabecalho("MENU PRINCIPAL")
    resposta = inicial.menu()
    if resposta == -1:
        print("modo de simulação")
    if resposta == 0:
        print("Programa encerrado!")
        break
    if resposta in range(1,100):
        cache = lru.LRU(resposta, cache)
    else:
        print("Número inválido.")
