from application.model.entity.entregador import Entregador

class EntregadorDAO:
    __entregador_list: list

    def __init__(self, entregador_list: list):
        self.__entregador_list = entregador_list

    def retornar_entregadores(self):
        return self.__entregador_list
