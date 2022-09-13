# Guido van Rossum <guido@python.org>

def step1():
    print(
        'Утка-маляр 🦆 решила зайти в бар и выпить. '
        'Взять ей зонтик? ☂️'
    )
    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()

    if options[option]:
        return step2_umbrella()
    return step2_no_umbrella()


def step2_umbrella():
    print(
        'Утка взяла зонт. '
        'Теперь ей точно не страшен дождь!'
    )


def step2_no_umbrella():
    print(
        'Утка не взяла зонт. '
        'Пошел ли дождь?'
    )
    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()

    if options[option]:
        print('Утка промокла и не добралась до бара. :(')
    else:
        print('Утке повезло, и теперь она сидит в баре счастливая! :)')


if __name__ == '__main__':
    step1()
