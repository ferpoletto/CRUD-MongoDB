from CRUD_mongo.produto import *

def menu():
    op = int(input('MENU\n'
                   '=-=-=-=-=-=-=-=-=-=-=-=-\n'
                   '1 - CADASTRO\n'
                   '2 - MOSTRAR \n'
                   '3 - ATUALIZAR\n'
                   '4 - DELETAR \n'
                   '5 - SAIR\n'
                   '=-=-=-=-=-=-=-=-=-=-=-=-\n'
                   'DIGITE A OPÇÃO DESEJADA: '))
    return op

p = Produto()

while True:
    op = menu()

    if op == 1:
        print("Cadastro de produto")
        p.cadastrar()
        print("Sucesso!")

    if op == 2:
        print("Mostrar produto")
        p.mostrar()
        print("Sucesso!")

    if op == 3:
        print("Atualizar produto")
        p.atualizar()
        print("Sucesso!")

    if op == 4:
        print("Deletar Produto")
        p.excluir()
        print("Sucesso!")

    if op == 5:
        print("Finalizando...")
        break

    else:
        print(f'Opção inválida. Tente novamente!')

print("FIM!")
