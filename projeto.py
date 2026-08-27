class Projeto:
    def __init__(self, id_projeto, nome, descricao):
        self.id_projeto = id_projeto
        self.nome = nome
        self.descricao = descricao
        self.tarefas = []

    def adicionar_tarefa(self, tarefa):
        self.tarefas.append(tarefa)

    def listar_tarefas(self):
        for tarefa in self.tarefas:
            print(tarefa.exibir_dados())
            print("-" * 40)

    def calcular_progresso(self):
        if len(self.tarefas) == 0:
            return 0

        concluidas = 0

        for tarefa in self.tarefas:
            if tarefa.status == "Concluída":
                concluidas += 1

        progresso = (concluidas / len(self.tarefas)) * 100

        return progresso
