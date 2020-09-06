class Vetor():

    def __init__(self, tamanho: int):
        self.__tamanho = tamanho
        self.__elementos = [None] * tamanho
        self.__posicao = 0

    def inserir_elemento_posicao(self, elemento, posicao):
        if self.__elementos[posicao] is not None:
            vetor_inicio = self.__elementos[:posicao] + [None]
            vetor_inicio[len(vetor_inicio) - 1] = elemento
            vetor_final = self.__elementos[posicao:]
            self.__elementos = vetor_inicio + vetor_final
            self.__posicao += 1
        self.__elementos[posicao] = elemento

    def inserir_elemento_final(self, elemento):
        if self.__posicao >= len(self.__elementos):
            self.__elementos = self.__elementos + [None, None]

        self.__elementos[self.__posicao] = elemento
        self.__posicao += 1

    def listar_elemento(self, posicao):
        return self.__elementos[posicao]
