from application.model.entity.pessoa import Pessoa


class Entregador(Pessoa):
    __contrato_em_vigencia: bool
    __contratos: list

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
        self.__contrato_em_vigencia = False
        self.__contratos = []

    @property
    def contrato_em_vigencia(self):
        return self.__contrato_em_vigencia

    @contrato_em_vigencia.setter
    def contrato_em_vigencia(self, contrato):
        self.__contrato_em_vigencia = contrato

    @property
    def contratos(self):
        return self.__contratos

    @contratos.setter
    def contratos(self, contrato):
        self.__contratos.append(contrato)
