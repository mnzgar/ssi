def exp_rapida(y, exp, mod):
  x = 1

  # print('\n   y\t\t\tb\tx')
  # print(' ----------------------------------')
  # print('   ' + str(y) + '\t\t\t' + str(exp) + '\t' + str(x))

  while exp != 0:
    if exp % 2 != 0:
      exp -= 1
      tmp = (y * x) % mod
      # print('   \t\t\t' + str(exp) + '\t' + str(y) + ' * ' + str(x) + ' (mod ' + str(mod) + ') = ' + str(tmp))
      x = tmp
    
    else:
      exp /= 2
      tmp = (y ** 2) % mod
      # print('   ' + str(y) + ' ^ 2 (mod ' + str(mod) + ') = ' + str(tmp) + '\t' + str(exp))
      y = tmp

  return x



def main():
  print(u'N\xfamero primo p:\t', end="")
  p = int(input())
  print(u'N\xfamero \u03b1 < p:\t', end="")
  alpha = int(input())
  print(u'N\xfamero de usuarios:\t', end="")
  n = int(input())
  
  # Recogemos xi
  x = []
  for i in range(n):
    x.append(int(input('Clave secreta x' + str(i) + ':\t')))

  # Hallamos yi
  y = []
  for i in range(n):
    print('\n\033[1mSujeto ' + str(i) + '\033[0m')
    print('calcula y' + str(i) + ' = ' + str(alpha) + ' ^ ' + str(x[i]) + ' (mod ' + str(p) + ')')
    y.append(exp_rapida(alpha, x[i], p))
    print(u'Clave p\xfablica:\ty' + str(i) + ' = ' + str(y[i]))
  
  # Calculamos claves
  for i, j in zip(x, range(n)):
    j1 = 0
    j2 = 0
    if j == 0:
      j1 = n - 1
      j2 = j + 1
    elif j == n - 1:
      j1 = j - 1
      j2 = 0
    else:
      j1 = j - 1
      j2 = j + 1
    
    print('\n\033[1mSujeto ' + str(j) + '\033[0m')
    print('genera kA = ' + str(y[j1]) + ' ^ ' + str(i) + ' (mod ' + str(p) + ')')
    kA = exp_rapida(y[j1], i, p)
    print(u'Clave de sesi\xf3n:\tkA = ' + str(kA))
    print('\ngenera kB = ' + str(y[j2]) + ' ^ ' + str(i) + ' (mod ' + str(p) + ')')
    kB = exp_rapida(y[j2], i, p)
    print(u'Clave de sesi\xf3n:\tkB = ' + str(kB))
    

main()