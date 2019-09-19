class Usuario:
    def __init__(self, nome, cpf, senha, modo):
        self.nome = nome
        self.cpf = cpf
        self.senha = senha

    def getUsuarioNome(self):
        return self.nome

    def getUsuarioCpf(self):
        return self.cpf 
    
    def getUsuarioSenha(self):
        return self.senha

    def setUsuarioNome(self, nome):
        self.nome = nome
    
    def setUsuarioCpf(self, cpf):
        self.cpf = cpf

    def setUsuarioSenha(self, senha):
        self.senha = senha

    def cadastrarUsuario(self, nome, cpf, senha, modo):
        self.__init__(nome, cpf, senha, modo)
    