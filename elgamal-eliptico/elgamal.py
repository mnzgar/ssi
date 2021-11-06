import random


def LehmanPeralta(x):
  a = []
  primo = True
  i = 0

  for i in range(100):
    a.append(random.randint(2, x - 1))

  while (i < len(a)) and primo:
    exp = exp_rapida(a[i], (x - 1) / 2, x)
    if exp != 1 and exp != x - 1:
      primo = False
    i += 1

  return primo


def exp_rapida(y, exp, mod):
  x = 1

  while exp != 0:
    if exp % 2 != 0:
      exp -= 1
      x = (y * x) % mod

    else:
      exp /= 2
      y = (y ** 2) % mod

  return x


def potencia(x):
  if x == 1:
    return True
  
  else:
    r = 1
    for i in range(1, x):
      r *= 2
      if r == x:
        return True

    return False


def puntos(p, a, b):
  x = []
  y = []
  ptos = []

  for i in range(p):
    x.append([i, ((i ** 3) + (a * i) + b) % p])
    y.append([i, (i ** 2) % p])

  for i in x:
    for j in y:
      if i[1] == j[1]:
        ptos.append([i[0], j[0]])

  return ptos


def bucle_suma(x, P, a, p):
  Q = P

  for i in range(x - 1):
    Q = suma_puntos(P, Q, a, p)
  
  return Q


def suma_puntos(P, Q, a, p):
  if P != Q:
    e = Euclides(P[0] - Q[0], p)
    while e < 0:
      e += p
    l = ((P[1] - Q[1]) * e) % p

  else:
    e = Euclides(2 * Q[1], p)
    while e < 0:
      e += p
    l = ((3 * (Q[0] ** 2) + a) * e) % p
  
  x3 = (l ** 2 - Q[0] - P[0]) % p
  PQ = [x3, (l * (Q[0] - x3) - Q[1]) % p]

  return PQ


def Euclides(d, fi):
  x = [d, fi]
  z = [1, 0]
  i = 1

  while x[i] != 0:
    x.append(x[i - 1] % x[i])
    z.append(-(x[i - 1] // x[i]) * z[i] + z[i - 1])
    i += 1

  return z[i - 1]


# Opcional
def codificar_msg(m, h, curva, p):
  j = 0

  while j < h:
    for i in curva:
      if m * h + j == i[0]:
        return i
    j += 1


def cifrar(Qmo, aA, dBP, aAP, M, a, p):
  p1 = suma_puntos(Qmo, bucle_suma(aA, dBP, a, p), a, p)
  msg = [bucle_suma(M, p1, a, p), bucle_suma(M, aAP, a, p)]
  
  return msg



def main():
  p = 13
  if not LehmanPeralta(p):
    print('Recuerde que p debe ser primo.')
    exit(0)

  a = 5
  b = 3
  P = [9, 6]

  aA = 4
  if not potencia(aA):
    print('Recuerde que aA debe ser potencia de 2.')
    exit(0)

  dB = 2
  if not potencia(dB):
    print('Recuerde que dB debe ser potencia de 2.')
    exit(0)

  Qm = [7, 2]
  M = 4

  # Opcional
  msg = 10
  m = int(str(msg), 2)

  print('A partir de las entradas:')
  print('    p = ' + str(p))
  print('    a = ' + str(a))
  print('    b = ' + str(b))
  print('    P = ' + str(P))
  print('    aA = ' + str(aA))
  print('    dB = ' + str(dB))
  print('    Mensaje original = ' + str(Qm))
  print('    (Opcional): Mensaje original = m = ' + str(msg) + ' = ' + str(m))
  print('    M = ' + str(M))

  curva = puntos(p, a, b)

  aAP = bucle_suma(aA, P, b, p)
  dBP = bucle_suma(dB, P, a, p)

  h = 0
  while h < (p / M):
    h += 1
  
  Qmo = codificar_msg(m, h, curva, p)
  msg_cifrado = cifrar(Qmo, aA, dBP, aAP, M, a, p)

  print('\nSe producen las salidas:')
  print('    Puntos de la curva: ' + str(curva))
  print('    Clave publica de A: punto aAP = ' + str(aAP))
  print('    Clave publica de B: punto dBP = ' + str(dBP))
  print('    h = ' + str(h) + ' < ' + str(p) + ' / ' + str(M))
  print('    (Opcional): Mensaje original codificado como punto Qm = (' + str(m) + ' * ' + str(h) + ' + 1, 2, ... ) = ' + str(Qmo))
  print('    Primer punto del Mensaje cifrado: Qm + aA (dBP) = ' + str(msg_cifrado[0]))
  print('    Segundo punto del Mensaje cifrado: aAP = ' + str(msg_cifrado[1]))
  

main()