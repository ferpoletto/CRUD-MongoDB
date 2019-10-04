from pprint import pprint

from pymongo import MongoClient
#pip install pymongo

class MongoConnect():

    def __init__(self):
        self.cliente = MongoClient('localhost', 27017)
        self.banco = self.cliente.teste  # nome do banco
        self.aluno = self.banco.aluno  # nome da coleção

    def save(self, json):
        try:
            self.aluno.insert_one(json)
        except Exception as e:
            print("problema ao SALVAR registro")
            print(json)
            print(e)

    def read(self, json=None, escondido=None):
        try:
            for prod in self.aluno.find(json, escondido):
                pprint(prod)
        except Exception as e:
            print("problema ao MOSTRAR registro")
            print(json)
            print(e)



    def update(self, json, fields):
        try:
            self.aluno.update(json, fields)
        except Exception as e:
            print("problema ao UPDATE registro")
            print(json)
            print(e)


    def delete(self, json):
        try:
            self.aluno.remove(json)
        except Exception as e:
            print("problema ao DELETAR registro")
            print(json)
            print(e)
