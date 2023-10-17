from random import randint

print('#### Iníciando Jogo ####')
# O Algoritmo seleciona um número aleatório entre 0 e 100
random = randint(0, 100)
# Chute é uma variável que se inicia em 0 e é a entrada do usuário
chute = 0
# Chance é o incremento do valor maximo de chances para os chutes 
chances = 10
# Enquanto o usuário não acertar corretamente o número escolhido pelo algoritmo o bloco de repetição sera executado até o acerto ou a falha do usuário.
while chute != random:
    chute = input('Chute um número entre 0 a 100: ')
    if chute.isnumeric():
        chute = int(chute)
        chances = chances - 1
        if chute == random:
            print('')
            print('Parabéns, você venceu! O número era {} e você ainda tinha {} chances.'.format(random, chances))
            print('')
            break
        else:
            print('')
            if chute > random:
                print('Você errou!!! Dica: É um número menor.')
            else:
                print('Você errou!!! Dica: É um número maior.')
            print('Você ainda possui {} chances.'.format(chances))
            print('')
        if chances == 0:
            print('')
            print('Suas chances acabaram, você perdeu!')
            print('')
            break

print('#### Fim do Jogo ####')