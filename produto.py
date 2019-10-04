from CRUD_mongo.conexao import MongoConnect

class Produto():

    def __init__(self):
        self.conexao = MongoConnect()

    def cadastrar(self):
        nome = input("Digite o nome do produto: ")
        preco = float(input(f'Digite o preco do {nome} R$ '))
        quantidade = int(input(f'Digite a quantidade do {nome}: '))

        produto = {"Nome": nome, "Preco": preco, "Quantidade": quantidade}

        self.conexao.save(produto)

    def excluir(self):
        find = input("Digite o produto para excluir: ")
        self.conexao.delete({"Nome": find})

    def atualizar(self):
        atualiza = input("Digite o produto que quer atualizar: ")

        nome = input("Digite o nome do produto: ")
        preco = float(input(f'Digite o preco do {nome} R$ '))
        quantidade = int(input(f'Digite a quantidade do {nome}: '))

        produto = {"Nome": nome, "Preco": preco, "Quantidade": quantidade}

        #self.conexao.update({"Nome": atualiza}, {produto})
        self.conexao.update({"Nome" : atualiza}, {"$set": produto})


    def mostrar(self):
        #Passa os campos que não quer motrar...
        self.conexao.read({"Nome": "Bike"}, {"Preco": 0, "_id": 0})

        #motrar tudo
        self.conexao.read()

