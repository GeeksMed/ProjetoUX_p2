from application.model.entity.pessoa import Pessoa


class Empresa(Pessoa):
    __contratados_efetuados: list

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
        super().__init__(cpf_cnpj,
                       nome,
                       imagem,
                       descr_breve,
                       endereco,
                       cep,
                       uf,
                       descr_completa,
                       valor_diario,
                       disp_semana)
        self.__avaliacao=0.0
        self.__contratados_efetuados = []

    @property
    def contratados_efetuados(self):
        return self.__contratados_efetuados

    @contratados_efetuados.setter
    def contcontratados_efetuadosatos(self, contratados_efetuados):
        self.__contratados_efetuados.append(contratados_efetuados)
