import valida


def linha(tam=55):
      return '-' * tam

def cabecalho(txt):
      print(linha())
      print(txt.center(45))
      print(linha())
      
def menu():
      opcao = valida.leiaNumeroInteiro("Digite o número que identifica o texto desejado: ")
      return opcao
