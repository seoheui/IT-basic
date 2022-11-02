import random

BLACK   = '\033[30m'
RED     = '\033[91m'
GREEN   = '\033[92m'
YELLOW  = '\033[93m'
BLUE    = '\033[94m'
MAGENTA = '\033[95m'
CYAN    = '\033[96m'
WHITE   = '\033[97m'

REDBG = '\033[101m'
GREENBG = '\033[102m'

END = '\033[0m'

def cprint(str):
    col = random.randint(0, 256)

    print(f'\033[38;5;{col}m' + '*'*5 + ' ' + str + ' ' + '*'*5 + '\033[0m')

# cprint('test')