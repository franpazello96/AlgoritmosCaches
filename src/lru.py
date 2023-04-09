import json

def LRU(resposta, cache):
    with open("database.json", encoding="utf-8") as database:
        data = json.load(database)
    
    # Busca a resposta no banco de dados
    for i in data:
        if i['id'] == resposta:
            print(f"Título: {i['titulo']}")
            print(f"Autor: {i['autor']}")
            print(f"Conteúdo: {i['conteudo']}")
            
            # Insere a resposta na lista cache
            cache.append(i)
            
            # Remove o primeiro item da lista cache, caso já tenha 10 itens
            if len(cache) > 10:
                cache.pop(0)
            break
            
    else:
        print("Resposta não encontrada no banco de dados.")
        
    return cache
