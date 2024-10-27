import json
import os

class Search():
    def __init__(self):
        self.caminho = 'code//paste_json//dados.json'

    def search(self):
        # Verifica se o arquivo existe e não está vazio
        if os.path.exists(self.caminho) and os.path.getsize(self.caminho) > 0:
            with open(self.caminho, 'r') as file:
                try:
                    load_json = json.load(file)
                    return load_json
                except json.JSONDecodeError:
                    print("Erro: O arquivo JSON está vazio ou inválido.")
                    return {}  # Retorna um dicionário vazio
        else:
            print("Arquivo JSON não encontrado ou vazio.")
            return {}  # Retorna um dicionário vazio

if __name__ == "__main__":
    load = Search()
    arquivo = load.search()
    print(arquivo)
