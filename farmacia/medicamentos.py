from laboratorio import Laboratorio
class Medicamento:

    def __init__(self, nome: str, comp_principal: str, laboratorio: Laboratorio, descricao: str) -> None:
        self.nome: nome
        self.comp_principal = comp_principal
        self.laboratorio = Laboratorio
        self.descricao = descricao



