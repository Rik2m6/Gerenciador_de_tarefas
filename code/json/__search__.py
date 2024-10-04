import json

class Search():

    def __init__(self):
        
        self.caminho = './/code//json//dados.json'

    def search(self):

        with open(self.caminho, 'r') as file:

            load_json = json.load(file)

        return load_json