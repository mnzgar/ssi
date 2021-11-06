def write(key, LFSR, n):
  xt = ''
  i = len(key)
  for j in range(len(key)):
    pos = False
    for k in LFSR:
      if i == k:
        pos = True

    if pos:
      print('\033[0;34m' + key[j] + '\033[0m\t', end="")
      xt += key[j]
    elif i == n:
      print('\033[0;31m' + key[j] + '\033[0m\t', end="")
      x = int(key[j])
    else:
      print(key[j] + '\t', end="")
    
    i -= 1
  
  return xt, x


def add(x):
  sum = 0
  for i in x:
    sum ^= int(i)
  return sum


def mayoria(a, b, c):
  f = (a * b) ^ (a * c) ^ (b * c)
  return f


def change(key, x):
  key = key[1:]
  key += x
  return key


def encrypt(text, sec_cifr):
  encrypted = ''
  for i in range(len(text)):
    encrypted += str(int(text[i]) ^ int(sec_cifr[i]))
  return encrypted



def main():
  LFSR1 = [19, 15, 14, 10]
  LFSR2 = [14, 3]                            # Modificacion
  LFSR3 = [23, 22, 21, 8]

  original_text = '111111'
  seed = '1001000100011010001010110011110001001101010111100110111100001111'
  key1 = ''
  key2 = ''
  key3 = ''
  sec_cifr = ''

  for i in range(LFSR1[0]):
    key1 += seed[i]
  
  for i in range(LFSR1[0], LFSR1[0] + 22):    # Modificacion
    key2 += seed[i]
  
  for i in range(LFSR1[0] + 22, LFSR1[0] + 22 + LFSR3[0]):
    key3 += seed[i]

  print('Semilla:\t' + key1 + '\n\t\t' + key2 + '\n\t\t' + key3 + '\n')
  
  end = False

  while end != True:
    # Numero iterador
    # for i in range(LFSR3[0], 0, -1):
    #   print(str(i) + '\t'),

    # Fila 1 (a)
    print('\n\t\t\t\t'),
    a, a9 = write(key1, LFSR1, 9)

    # Fila 2 (b)
    print('\n\t'),
    b, b11 = write(key2, LFSR2, 11)
      
    # Fila 3 (c)
    print
    c, c11 = write(key3, LFSR3, 11)

    sum = ''
    sum += str(add(a))
    sum += str(add(b))
    sum += str(add(c))
    F = mayoria(a9, b11, c11)
    z = ''
    z += key1[0]
    z += key2[0]
    z += key3[0]
    sumz = add(z)
    sec_cifr += str(sumz)
    
    print('\nF(' + str(a9) + ', ' + str(b11) + ', ' + str(c11) + ') = ' + str(F))
    print('z(t) = ' + z[0] + ' + ' + z[1] + ' + ' + z[2] + ' = ' + str(sumz))
    print('Secuencia cifrante: ' + sec_cifr)
    print('\n-------------------------------------------------------------------\n')

    if a9 == b11 == c11 == F:
      end = True
    else:
      if a9 == F:
        key1 = change(key1, sum[0])
      if b11 == F:
        key2 = change(key2, sum[1])
      if c11 == F:
        key3 = change(key3, sum[2])
  
  encrypt_text = encrypt(original_text, sec_cifr)
  print('Mensaje original: ' + original_text)
  print('Clave: ' + sec_cifr)
  print('Mensaje cifrado: ' + encrypt_text)
  decrypt_text = encrypt(encrypt_text, sec_cifr)
  print('Mensaje descifrado: ' + decrypt_text)


main()
