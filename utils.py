from models import Pessoas

def inserir_pessoas(nome, idade):
    pessoa = Pessoas(nome=nome, idade=idade)
    pessoa.save()

def consultar_nomes(nome):
    pessoa = Pessoas.query.filter_by(nome=nome).first()
    print("Nome encontrado: " + pessoa.nome + "\nIdade: "+ str(pessoa.idade))

def alterar_idade(nome, idade):
    pessoa = Pessoas.query.filter_by(nome=nome).first()
    pessoa.idade = idade
    pessoa.save()

def alterar_nome(nome_atual, nome_novo):
    pessoa = Pessoas.query.filter_by(nome=nome_atual).first()
    pessoa.nome = nome_novo
    pessoa.save()

def consultar_todos():
    pessoa = Pessoas.query.all()
    for i in pessoa:
        print("\nNome encontrado: " + i.nome + "\nIdade: " + str(i.idade))

def excluir_pessoa(nome):
    try:
        pessoa = Pessoas.query.filter_by(nome=nome).first()
        pessoa.delete()
    except:
        print("\nNão foi possível excluir")

inserir_pessoas("Francisquinha", 19)
#excluir_pessoa("Francisquinha")
consultar_todos()
#alterar_nome("Eduardo", "Luiz Eduardo")
#consultar_nomes("Luiz Eduardo")