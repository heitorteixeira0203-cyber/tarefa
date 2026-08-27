class Tarefa:
    def __init__(self, id_tarefa, titulo, descricao, prioridade, responsavel):
        self.id_tarefa = id_tarefa
        self.titulo = titulo
        self.descricao = descricao
        self.prioridade = prioridade
        self.responsavel = responsavel
        self.status = "Pendente"

    def concluir(self):
        self.status = "Concluída"

    def alterar_status(self, novo_status):
        self.status = novo_status

    def exibir_dados(self):
        return (
            f"Tarefa: {self.titulo}\n"
            f"Descrição: {self.descricao}\n"
            f"Prioridade: {self.prioridade.value}\n"
            f"Responsável: {self.responsavel.nome}\n"
            f"Status: {self.status}"
        )
