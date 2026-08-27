class Usuario:
    def __init__(self, id_usuario, nome, email):
        self.id_usuario = id_usuario
        self.nome = nome
        self.email = email

    def exibir_dados(self):
        return f"{self.id_usuario} - {self.nome} - {self.email}"
