from personagens import Personagem, DarkWarrior
import eventos
from time import sleep
import colorama
import os

p1 = Personagem('Stickdaleh')
m1 = DarkWarrior()


def mapa():
    pass


def menu_jogo():
    print('Escolha uma das opçoes:')
    print('[1] Caçar\n'
          '[2] Healar\n'
          '[3] Mapa\n'
          '[4] Status\n')


def Iniciar(personagem, inimigo):
    while True:
        menu_jogo()
        resposta = int(input('Resposta: '))
        if resposta == 1:
            eventos.Cacar(p1, m1)
        elif resposta == 2:
            personagem.healar()



Iniciar(p1,m1)

