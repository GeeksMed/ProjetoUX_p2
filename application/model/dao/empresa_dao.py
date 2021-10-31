from application.model.entity.empresa import Empresa

class EmpresaDAO:
    __empresa_list: list

    def __init__(self, empresa_list: list):
        self.__empresa_list = empresa_list

    def retornar_emnpresas(self):
        return self.__empresa_list
