import random

def cprint(str):
    col = random.randint(0, 256)

    print(f'\033[38;5;{col}m' + '*'*5 + ' ' + str + ' ' + '*'*5 + '\033[0m')

# cprint('test')