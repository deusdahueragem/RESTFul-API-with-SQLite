from models import Pessoas, Usuarios

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

def insere_usuario(login, senha):
    usuario = Usuarios(login=login, senha=senha)
    usuario.save()

def consulta_todosusuarios():
    usuario = Usuarios.query.all()
    for i in usuario:
        print("\nUsuario encontrado: " + i.login)

#inserir_pessoas("Francisquinha", 19)
#inserir_pessoas("Eduardo", 24)
#inserir_pessoas("Marcio", 51)
#excluir_pessoa("Francisquinha")
#consultar_todos()
#alterar_nome("Eduardo", "Luiz Eduardo")
#consultar_nomes("Luiz Eduardo")

#insere_usuario("eduardo", "34014154")
#insere_usuario("francisquinha", "123456")
consulta_todosusuarios()