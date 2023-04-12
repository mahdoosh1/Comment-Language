from colorama import *

init()
out = ''
inp = ''


def rem(inp):
    return ' '.join(inp.split(' ')[1:])


def col(inp):
    out = ''
    out2 = ''
    if inp.startswith('if ') or inp.startswith('else') or inp.startswith('for') or inp.startswith('while'):
        out2 = out + Fore.CYAN + inp.split()[0] + Style.RESET_ALL + " " + rem(inp)
    elif inp.startswith('var ') or inp.startswith('pntr'):
        out2 = out + Fore.RED + inp.split()[0] + Style.RESET_ALL + " " + rem(inp)
    elif inp.startswith('do ') or inp.startswith('end'):
        out2 = out + Fore.MAGENTA + inp.split()[0] + Style.RESET_ALL + " " + rem(inp)
    elif inp.startswith('#'):
        out2 = out + Fore.YELLOW + inp.split()[0] + rem(inp)
    elif inp.startswith('&tab '):
        out2 = out + '    ' + rem(inp)
    elif inp != ';':
        out2 = out + inp
    out = out2 + "\n" + Style.RESET_ALL
    return out


def rm(inp):
    inp = list(inp.split('    '))
    cnt = 0
    for i in inp:
        if i == '':
            cnt += 1
    out = col(''.join(inp))
    out = cnt * '    ' + out
    return out


while inp != ';':
    inp = input("End code with semicolon(';')")
    if inp != ';':
        if inp.startswith('    '):
            out = out + rm(inp)
        else:
            out = out + col(inp)
print(out)
input('Press Enter key to exit...')
