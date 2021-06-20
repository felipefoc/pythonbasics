import time
from controllers.helper import cls
from models.classes import Jogo


def main():
    jogo.novo_jogo()
    while True:
        cls()
        jogo.saber_rodada()
        jogo.aviso_balde()
        continuar = input('Deseja inserir mais agua? \nResponda sim ou não... : ')
        if continuar.lower() in ['sim', 's']:
            jogo.adicionar_agua()
            jogo.nova_rodada()
            time.sleep(1)
            if jogo.checar_resultado():
                cls()
                jogo.fim_de_jogo()
                break
        else:
            time.sleep(1)
            cls()
            jogo.fim_de_jogo()
            break

if __name__ == '__main__':
    jogo = Jogo()
    main()