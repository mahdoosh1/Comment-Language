out = u''
inp = ''
while inp != ';':
  inp = input("End code with semicolon(';')")
  if inp.startswith('if') or inp.startswith('else') or inp.startswith('for') or inp.startswith('while'):
    out = out + u"\033[1;36m" + u"\u001b[0m" + inp
  elif inp.startswith('var') or inp.startswith('pntr'):
    out = out + u"\033[1;33m" + u"\u001b[0m" + inp
  elif inp.startswith('do') or inp.startswith('end'):
    out = out + u"\033[1;31m" + u"\u001b[0m" + inp
  elif inp.startswith('#'):
    out = out + u"\033[1;32m" + inp
  out = out + u"\n\u001b[0m"
print(out)
input('Press Enter key to exit...')
