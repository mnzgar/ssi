def encrypt(text, key):
  encrypted = ''
  for i in range(len(text)):
    encrypted += str(int(text[i]) ^ int(key[i]))
  return encrypted


def main():
  original_text = '1, 34'
  # key_seed = '1, 35, 69, 103, 137, 171, 205, 139'
  # key_seed = '2, 5'
  key_seed = '97, 45, 117, 98, 34'
  mod = 256

  print('Entrada:')
  print('Semilla de clave = ' + key_seed)
  print('Texto original: ' + original_text)

  original_text = original_text.replace(' ', '').split(',')
  key_seed = key_seed.replace(' ', '').split(',')

  # Inicializacion
  print(u'\nInicializaci\xf3n:')

  S = []
  K = []

  for i in range(mod):
    S.append(i)

  for i in range(int(len(S) / len(key_seed))):
    for j in range(len(key_seed)):
      K.append(int(key_seed[j]))

  if len(S) != len(K):
    sz = len(S) % len(key_seed)
    for i in range(sz):
      K.append(int(key_seed[i]))

  print('S = ' + str(S))
  print('K = ' + str(K))

  j = 0
  for i in range(mod):
    print('S[' + str(i) + '] = ' + str(S[i])),
    print('K[' + str(i) + '] = ' + str(K[i])),
    j = (j + S[i] + K[i]) % mod
    print('produce f = ' + str(j)),
    tmp = S[i]
    S[i] = S[j]
    S[j] = tmp
    print('S[' + str(i) + '] = ' + str(S[i]) + ' S[' + str(j) + '] = ' + str(S[j]))

  print('S = ' + str(S))

  # Generacion de secuencia cifrante
  print(u'\nGeneraci\xf3n de secuencia cifrante y texto cifrado:')

  i = 0
  j = 0
  for k in range(len(original_text)):
    i = (i + 1) % mod
    j = (j + S[i]) % mod
    tmp = S[i]
    S[i] = S[j]
    S[j] = tmp
    t = (S[i] + S[j]) % mod

    St = bin(S[t]).replace('0b', '').zfill(8)
    print('Byte ' + str(k + 1) + ' de secuencia cifrante: Salida = S[' + str(t) + '] = ' + str(S[t]) + ':\t\t' + St)
    M = bin(int(original_text[k])).replace('0b', '').zfill(8)
    print('Byte ' + str(k + 1) + ' de texto original: Entrada: M[' + str(k + 1) + '] = ' + str(original_text[k]) + ':\t\t\t' + M)
    Cb = encrypt(St, M)
    C = int(Cb, 2)
    print('Byte ' + str(k + 1) + ' de texto cifrado, Salida = C[' + str(k + 1) + '] = ' + str(C) + ':\t\t\t' + Cb)

  # Modificacion
  print(u'\nModificaci\xf3n:')

  i = 0
  j = 0
  k = 0
  w = 3
  z = 0
  for l in range(len(original_text)):
    i = (i + w) % mod
    j = (k + S[j + S[i]]) % mod
    k = (i + k + S[j]) % mod
    tmp = S[i]
    S[i] = S[j]
    S[j] = tmp
    z = ((S[j + S[i + S[z + k]]]) % mod) - 1

    Sz = bin(S[z]).replace('0b', '').zfill(8)
    print('Byte ' + str(l + 1) + ' de secuencia cifrante: Salida = S[' + str(z) + '] = ' + str(S[z]) + ':\t\t' + Sz)
    M = bin(int(original_text[l])).replace('0b', '').zfill(8)
    print('Byte ' + str(l + 1) + ' de texto original: Entrada: M[' + str(l + 1) + '] = ' + str(original_text[l]) + ':\t\t\t' + M)
    Cb = encrypt(Sz, M)
    C = int(Cb, 2)
    print('Byte ' + str(l + 1) + ' de texto cifrado, Salida = C[' + str(l + 1) + '] = ' + str(C) + ':\t\t\t' + Cb)

main()
