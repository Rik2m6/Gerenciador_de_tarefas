import json

class Search():

    def __init__(self):
        
        self.caminho = 'code//paste_json//dados.json'

    def search(self):

        with open(self.caminho, 'r') as file:

            load_json = json.load(file)

        return load_json

if __name__ == "__main__":

    load = Search()
    arquivo = load.search()

    for tarefa in arquivo['teste']:
        print(f"Nome: {tarefa['nome']}, Prioridade: {tarefa['prioridade']}")