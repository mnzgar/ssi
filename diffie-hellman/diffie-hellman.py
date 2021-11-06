def exp_rapida(y, exp, mod):
  x = 1

  print('\n   y\t\t\tb\tx')
  print(' ----------------------------------')
  print('   ' + str(y) + '\t\t\t' + str(exp) + '\t' + str(x))

  while exp != 0:
    if exp % 2 != 0:
      exp -= 1
      tmp = (y * x) % mod
      print('   \t\t\t' + str(exp) + '\t' + str(y) + ' * ' + str(x) + ' (mod ' + str(mod) + ') = ' + str(tmp))
      x = tmp
    
    else:
      exp /= 2
      tmp = (y ** 2) % mod
      print('   ' + str(y) + ' ^ 2 (mod ' + str(mod) + ') = ' + str(tmp) + '\t' + str(exp))
      y = tmp

  return x



def main():
  print(u'N\xfamero primo p:\t', end="")
  p = int(input())
  print(u'N\xfamero \u03b1 < p:\t', end="")
  alpha = int(input())
  xA = int(input('Secreto xA:\t'))
  xB = int(input('Secreto xB:\t'))

  print('\n\033[1mSujeto A\033[0m')
  print('calcula yA = ' + str(alpha) + ' ^ ' + str(xA) + ' (mod ' + str(p) + ')')
  yA = exp_rapida(alpha, xA, p)
  print('\nyA = ' + str(yA))
  
  print('\n\033[1mSujeto B\033[0m')
  print('calcula yB = ' + str(alpha) + ' ^ ' + str(xB) + ' (mod ' + str(p) + ')')
  yB = exp_rapida(alpha, xB, p)
  print('\nyB = ' + str(yB))
  
  print('\n\033[1mSujeto A\033[0m')
  print('genera kA = ' + str(yB) + ' ^ ' + str(xA) + ' (mod ' + str(p) + ')')
  kA = exp_rapida(yB, xA, p)
  print('\nkA = ' + str(kA))
  
  print('\n\033[1mSujeto B\033[0m')
  print('genera kB = ' + str(yA) + ' ^ ' + str(xB) + ' (mod ' + str(p) + ')')
  kB = exp_rapida(yA, xB, p)
  print('\nkB = ' + str(kB))

  if kA == kB:
    print('\nLas claves coinciden.')
  else:
    print('\nLas claves NO coinciden.')


main()