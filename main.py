from usuario import Usuario
from prioridade import Prioridade
from tarefa import Tarefa
from projeto import Projeto


usuarios = []
projetos = []
tarefas = []


def menu():
    print("\n" + "=" * 50)
    print("GERENCIADOR INTELIGENTE DE TAREFAS")
    print("=" * 50)
    print("1 - Cadastrar usuário")
    print("2 - Criar projeto")
    print("3 - Criar tarefa")
    print("4 - Listar tarefas")
    print("5 - Concluir tarefa")
    print("6 - Mostrar progresso do projeto")
    print("7 - Sair")


def cadastrar_usuario():
    print("\n--- CADASTRO DE USUÁRIO ---")

    id_usuario = len(usuarios) + 1
    nome = input("Nome: ")
    email = input("E-mail: ")

    usuario = Usuario(id_usuario, nome, email)
    usuarios.append(usuario)

    print("Usuário cadastrado com sucesso!")


def criar_projeto():
    print("\n--- CRIAR PROJETO ---")

    id_projeto = len(projetos) + 1
    nome = input("Nome do projeto: ")
    descricao = input("Descrição: ")

    projeto = Projeto(id_projeto, nome, descricao)
    projetos.append(projeto)

    print("Projeto criado com sucesso!")


def criar_tarefa():
    print("\n--- CRIAR TAREFA ---")

    if not usuarios:
        print("Cadastre um usuário primeiro.")
        return

    if not projetos:
        print("Crie um projeto primeiro.")
        return

    titulo = input("Título da tarefa: ")
    descricao = input("Descrição: ")

    print("\nPrioridade:")
    print("1 - Baixa")
    print("2 - Média")
    print("3 - Alta")
    print("4 - Urgente")

    opcao_prioridade = input("Escolha: ")

    prioridades = {
        "1": Prioridade.BAIXA,
        "2": Prioridade.MEDIA,
        "3": Prioridade.ALTA,
        "4": Prioridade.URGENTE
    }

    prioridade = prioridades.get(opcao_prioridade)

    if prioridade is None:
        print("Prioridade inválida.")
        return

    print("\nUsuários:")

    for usuario in usuarios:
        print(f"{usuario.id_usuario} - {usuario.nome}")

    id_responsavel = int(input("Escolha o responsável: "))

    responsavel = None

    for usuario in usuarios:
        if usuario.id_usuario == id_responsavel:
            responsavel = usuario
            break

    if responsavel is None:
        print("Usuário não encontrado.")
        return

    print("\nProjetos:")

    for projeto in projetos:
        print(f"{projeto.id_projeto} - {projeto.nome}")

    id_projeto = int(input("Escolha o projeto: "))

    projeto_escolhido = None

    for projeto in projetos:
        if projeto.id_projeto == id_projeto:
            projeto_escolhido = projeto
            break

    if projeto_escolhido is None:
        print("Projeto não encontrado.")
        return

    id_tarefa = len(tarefas) + 1

    tarefa = Tarefa(
        id_tarefa,
        titulo,
        descricao,
        prioridade,
        responsavel
    )

    tarefas.append(tarefa)
    projeto_escolhido.adicionar_tarefa(tarefa)

    print("Tarefa criada com sucesso!")


def listar_tarefas():
    print("\n--- LISTA DE TAREFAS ---")

    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
        return

    for tarefa in tarefas:
        print("-" * 40)
        print(f"ID: {tarefa.id_tarefa}")
        print(tarefa.exibir_dados())


def concluir_tarefa():
    listar_tarefas()

    if not tarefas:
        return

    id_tarefa = int(input("\nDigite o ID da tarefa que deseja concluir: "))

    for tarefa in tarefas:
        if tarefa.id_tarefa == id_tarefa:
            tarefa.concluir()
            print("Tarefa concluída com sucesso!")
            return

    print("Tarefa não encontrada.")


def mostrar_progresso():
    if not projetos:
        print("Nenhum projeto cadastrado.")
        return

    print("\n--- PROJETOS ---")

    for projeto in projetos:
        print(f"{projeto.id_projeto} - {projeto.nome}")

    id_projeto = int(input("Escolha o projeto: "))

    for projeto in projetos:
        if projeto.id_projeto == id_projeto:
            progresso = projeto.calcular_progresso()

            print(f"\nProjeto: {projeto.nome}")
            print(f"Progresso: {progresso:.1f}%")
            return

    print("Projeto não encontrado.")


while True:
    menu()

    opcao = input("\nEscolha uma opção: ")

    if opcao == "1":
        cadastrar_usuario()

    elif opcao == "2":
        criar_projeto()

    elif opcao == "3":
        criar_tarefa()

    elif opcao == "4":
        listar_tarefas()

    elif opcao == "5":
        concluir_tarefa()

    elif opcao == "6":
        mostrar_progresso()

    elif opcao == "7":
        print("\nSistema encerrado.")
        break

    else:
        print("\nOpção inválida.")
