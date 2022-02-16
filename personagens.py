from time import sleep
import colorama
import random


class Personagem:
    def __init__(self, nome):
        self.nome = nome
        self.maxhp = 100
        self.lvl = 1
        self.vida = 100
        self.exp = 0
        self.maxexp = 300
        self.vivo = True
        self.atk = 15
        self.gold = 50
        self.resto_exp = 0

    # Trazer o evento de subir nivel pra cá

    def dar_exp(self, inimigo):
        print(f'Você obteve {inimigo.GExp} de experiência!')
        self.exp += inimigo.GExp
        Personagem.power_up(self)


    def power_up(self):
        while self.exp > self.maxexp:
            self.lvl += 1
            self.maxhp = round(self.lvl * (100 * (1.03 ** self.lvl)))
            self.maxexp = round(self.lvl * (300 * (1.03 ** self.lvl)))
            self.atk = round(self.lvl * (15 * (1.03 ** self.lvl)))
            if self.maxexp > self.exp:
                self.resto_exp = self.maxexp - self.exp
                self.exp += self.resto_exp
            print(f'Parabéns você subiu do nivel {self.lvl - 1} para o nivel {self.lvl}\n'
                  f'Level: {self.lvl}\n'
                  f'Vida Máxima: {self.maxhp}\n'
                  f'Ataque: {self.atk}\n'
                  f'{self.exp, self.maxexp}\n'
                  f'exp para o proximo nivel {self.exp - self.maxexp}')


    def healar(self):
        if self.vida < self.maxhp:
            print(f'Sua vida agora é {self.vida}')
            sleep(0.5)
            print(colorama.Fore.BLUE + 'Curando...' + colorama.Fore.RESET)
            sleep(1)
            print(colorama.Fore.BLUE + 'Curando...' + colorama.Fore.RESET)
            sleep(1)
            self.vida = self.maxhp
            print(f'Você se curou, sua vida agora é {self.vida}')
        else:
            print('Sua vida está cheia')


class DarkWarrior:
    def __init__(self):
        self.nome = 'DarkWarrior'
        self.lvl = 1
        self.vida = round((self.lvl * (125*(1.08 ** self.lvl)))-80)
        self.maxvida = 100
        self.GExp = round((self.lvl * (15*(1.01 ** self.lvl))+150))
        self.vivo = True
        self.atk = round(self.lvl * (10*(1.03 ** self.lvl)))



class Item:
    def __init__(self, name, tipo, descricao):
        self.name = name
        self.type = tipo
        self.description = descricao
        self.drop = 50






