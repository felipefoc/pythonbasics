import time
from controllers.helper import cls, novo_jogo
from models.classes import Jogo


def start_game():
    novo_jogo()
    jogo = Jogo()
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


def main():
<<<<<<< ours
    start_game()
=======
    game = start_game()
    game2 = start_game()
>>>>>>> theirs


if __name__ == '__main__':
    main()
