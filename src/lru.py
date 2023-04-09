import json
from cachetools import LRUCache

cache = LRUCache(maxsize=10)

def lista(resposta):
    if resposta in cache:
        item = cache[resposta]
        item['contador'] += 1
        print(f"Título: {item['titulo']}")
        print(f"Autor: {item['autor']}")
        print(f"Conteúdo: {item['conteudo']}")
    else:
        with open("database.json", encoding="utf-8") as database:
            data = json.load(database)
            for i in data:
                if i["id"] == resposta:
                    item = {'id': i['id'], 'titulo': i['titulo'], 'autor': i['autor'], 'conteudo': i['conteudo'], 'contador': 1}
                    cache[resposta] = item
                    print(f"Título: {item['titulo']}")
                    print(f"Autor: {item['autor']}")
                    print(f"Conteúdo: {item['conteudo']}")
                    break
            else:
                print("Item não encontrado")
                return None
    print("Cache atual:")
    for key, value in cache.items():
        print(f"{key}: {value}")
    return cache
