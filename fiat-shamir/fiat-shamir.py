import random


def FiatShamir(x, s, N, v, e):
  a = (x ** 2) % N
  print('\t\t\ta = ' + str(a) + ','),
  if e == 0:
    y = x % N
  else:
    y = (x * s) % N

  check(y, a, N, v, e)


def check(y, a, N, v, e):
  p1 = (y ** 2) % N
  p2 = (a * v ** e) % N
  print('y = ' + str(y) + ', comprobamos que ' + str(y) + ' ^ 2 (mod ' + str(N) + ') = ' + str(p1) + ','),
  if p1 == p2:
    print('ES'),
  else:
    print('NO ES'),
  print('igual a ' + str(a)),
  if e != 0:
    print('* ' + str(v)),
  print('(mod ' + str(N) + ') = ' + str(p2))



def main():
  # Inicializacion
  p = int(input('p =\t'))
  q = int(input('q =\t'))
  N = p * q

  # Identificacion secreta de A
  s = int(input('s =\t'))

  # Identificacion publica de A
  v = (s ** 2) % N

  # Numero de iteraciones 
  i = int(input('i =\t'))

  # Numero secretos y e
  x = []
  e = []
  for j in range(i):
    x.append(int(input('x' + str(int(j + 1)) + ' =\t')))
    e.append(random.randint(0, 1))

  print('\nEntrada:')
  print('    Inicializacion:\t\t\tp = ' + str(p) + ', q = ' + str(q))
  print('    Identificacion secreta de A:\ts = ' + str(s))
  print('    Numero de iteraciones:\t\ti = ' + str(i))
  for j in range(i):
    print('    Iteracion ' + str(int(j + 1)) + ':\t\t\tx = ' + str(x[j]) + ', e = ' + str(e[j]))

  print('\nSalida:')
  print('    Modulo:\t\t\t\tN = ' + str(N))
  print('    Identificacion publica de A:\tv = ' + str(v))
  for j in range(i):
    print('    Iteracion ' + str(int(j + 1)) + ':'),
    FiatShamir(x[j], s, N, v, e[j])


main()