#Classe Pai de Pessoa Fisica e Juridica

class Pessoa():
    __cpf_cnpj: str
    __nome: str
    __imagem: str
    __descr_breve: str
    __endereco: str
    __cep: str
    __uf: str
    __descr_completa: str
    __valor_diario: float
    __disp_semana: int
    __avaliacao: float

    def __init__(self,
                 cpf_cnpj:str,
                 nome:str,
                 imagem:str,
                 descr_breve:str,
                 endereco:str,
                 cep:str,
                 uf:str,
                 descr_completa:str,
                 valor_diario:float,
                 disp_semana:int):
        self.__cpf_cnpj = cpf_cnpj
        self.__nome = nome
        self.__imagem = imagem
        self.__descr_breve = descr_breve
        self.__endereco = endereco
        self.__cep = cep
        self.__uf = uf
        self.__descr_completa = descr_completa
        self.__valor_diario = valor_diario
        self.__disp_semana = disp_semana
        self.__avaliacao = 0

    @property
    def cpf_cnpj(self):
        return self.__cpf_cnpj

    @cpf_cnpj.setter
    def cpf_cnpj(self, cpf_cnpj):
        self.__cpf_cnpj = cpf_cnpj

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def imagem(self):
        return self.__imagem

    @imagem.setter
    def imagem(self, imagem):
        self.__imagem = imagem

    @property
    def descr_breve(self):
        return self.__descr_breve

    @descr_breve.setter
    def descr_breve(self, descr_breve):
        self.__descr_breve = descr_breve

    @property
    def endereco(self):
        return self.__descr_breve

    @endereco.setter
    def endereco(self, endereco):
        self.__endereco = endereco

    @property
    def cep(self):
        return self.__cep

    @cep.setter
    def cep(self, cep):
        self.__cep = cep

    @property
    def uf(self):
        return self.__uf

    @uf.setter
    def uf(self, uf):
        self.__uf = uf

    @property
    def descr_completa(self):
        return self.__descr_completa

    @descr_completa.setter
    def descr_completa(self, descr_completa):
        self.__descr_completa = descr_completa

    @property
    def valor_diario(self):
        return self.__valor_diario

    @valor_diario.setter
    def valor_diario(self, valor_diario):
        self.__valor_diario = valor_diario

    @property
    def disp_semana(self):
        return self.__disp_semana

    @disp_semana.setter
    def disp_semana(self, disp_semana):
        self.__disp_semana = disp_semana

    @property
    def avaliacao(self):
        return self.__avaliacao

    @avaliacao.setter
    def avaliacao(self, avaliacao):
        media = self.avaliacao()
        if media == 0:
            self.__avaliacao = avaliacao
        else:
            media += avaliacao
            media /= 2
            self.__avaliacao = media
