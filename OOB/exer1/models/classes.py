from random import randint


class Balde:

    '''Criando Balde'''

    def __init__(self):
        self.capacidade = randint(10, 50)
        self.agua = 0


class Jogo:
    
    '''Classe jogo'''    

    def __init__(self):
        self.balde = Balde()
        self.rodada = 1

    def nova_rodada(self):
        self.rodada += 1
    
    def aviso_balde(self):
        capacidade = self.balde.capacidade
        agua = self.balde.agua
        if agua >= (capacidade / 2):
            print('O balde já está na metade ou passou da metade!!!')

    def saber_rodada(self):
        print(f'Rodada {self.rodada}!')

    def adicionar_agua(self):
        quantidade = randint(1,7)
        print('Foi adicionada mais agua!')
        self.balde.agua += quantidade
        
    def fim_de_jogo(self):
        if self.balde.agua > self.balde.capacidade:
            print(f'''
                    Você ultrapassou a capacidade do balde...
                    Capacidade = {self.balde.capacidade}
                    Agua = {self.balde.agua}
                   ''')
        print(f'''
                Jogo encerrado
                Você terminou com o balde de capacidade {self.balde.capacidade}.
                Com a quantidade de agua {self.balde.agua}.
               ''')

    def checar_resultado(self):
        if self.balde.agua > self.balde.capacidade:
            return True
 