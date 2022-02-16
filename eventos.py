from personagens import Personagem
import colorama
from time import sleep


def Cacar(jogador, inimigo):
    # Sempre chamar o menu na sequencia
    # Lutar enquanto estiver vivo ou sair (da pra mudar para while vivo = True futuramente)
    inimigo.lvl = input(f'Escolha o lvl do inimigo que deseja caçar: ')
    while jogador.vida > 0:
        # Cada um ataca por turno (botar chances de erro futuramente)
        inimigo.vida -= jogador.atk
        jogador.vida -= inimigo.atk
        print(f'{jogador.nome} atacou e tirou {jogador.atk} do inimigo {inimigo.nome}')
        sleep(0.5)
        print(f'A vida de {jogador.nome} é {jogador.vida}\n A vida do inimigo {inimigo.nome} é {inimigo.vida}')
        # Checa se o inimigo morreu
        if inimigo.vida <= 0:
            print(f'Você ganhou de {inimigo.nome}')
            sleep(0.5)
            Personagem.dar_exp(jogador, inimigo)
            resposta = int(input(f'Surgiu um novo inimigo {inimigo.nome}! Continuar lutando? [1] Sim [2] Não'))
            if resposta == 1:
                inimigo.vida = inimigo.maxvida
                pass
            else:
                break
    if jogador.vida <= 0:
        print('Você morreu! Tente ficar mais forte para tentar novamente')
        sleep(1)

    else:
        print('Você escolheu voltar para o menu')









