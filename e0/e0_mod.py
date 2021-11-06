# Elementos importantes
def important(LFSR, seed_reg):
  x = ''
  for i in LFSR:
    x += seed_reg[i - 1]
  return x


# Suma binaria
def add(x):
  sum = 0
  for i in x:
    sum ^= int(i)
  return sum


# Algoritmo (operaciones)
def generator(seed, a, b, c, d, e):
  print('LFSR1 = ' + str(a))
  print('LFSR2 = ' + str(b))
  print('LFSR3 = ' + str(c))
  print('LFSR4 = ' + str(d))
  print('LFSR5 = ' + str(e))

  r1 = seed[::-1]
  t1 = r1
  r2 = r1[::-1]
  t2 = r2[1] + str(int(r2[0]) ^ int(r2[1]))
  next_seed = a + b + c + d

  print('R1 = ' + r1)

  r1 = int(r1, 2)

  print('R1 (decimal) = ' + str(r1))
  print('T1 = ' + t1)
  print('R2 = ' + r2)
  print('T2 = ' + t2)
  print('\nSuma (LFSR decimal) = ' + str(next_seed))

  next_seed += r1
  print('Suma (LFSR + R1 decimal) = ' + str(next_seed))

  next_seed /= 2
  print(u'Divisi\xf3n (LFSR + R1 / 2 decimal) = ' + str(next_seed))

  next_seed = bin(int(next_seed)).replace('0b', '').zfill(2)
  print(u'Divisi\xf3n (LFSR + R1 / 2 binario) = ' + str(next_seed))

  tmp = str(int(next_seed[0]) ^ int(t2[0])) + str(int(next_seed[1]) ^ int(t2[1]))
  print('Suma (LFSR + R1 / 2 + T2 binario) = ' + str(tmp))

  next_seed = str(int(tmp[0]) ^ int(t1[0])) + str(int(tmp[1]) ^ int(t1[1]))
  print('Suma (LFSR + R1 / 2 + T2 + T1 binario) = ' + str(next_seed))

  z = a ^ b ^ c ^ d ^ int(t1[1]) ^ e
  print('z(t) = ' + str(z))

  return next_seed, z


# Cambiar la semilla
def change(seed_reg, x):
  seed_reg = seed_reg[:len(seed_reg) - 1]
  seed_reg = str(x) + seed_reg
  return seed_reg


# Cifrado
def encrypt(text, sec_cifr):
  encrypted = ''
  for i in range(len(text)):
    encrypted += str(int(text[i]) ^ int(sec_cifr[i]))
  return encrypted



def main():
  LFSR1 = [8, 12, 20, 25]
  LFSR2 = [12, 16, 24, 31]
  LFSR3 = [4, 24, 28, 33]
  LFSR4 = [4, 28, 36, 39]
  LFSR5 = [5, 10, 15, 25]
  seed_reg1 = '0111111111111111111111111'
  seed_reg2 = '0111111111111111111111111111111'
  seed_reg3 = '011111111111111111111111111111111'
  seed_reg4 = '010101010101010101010101010101010101010'
  seed_reg5 = '111111111111111111111111111111111111111'
  seed_r1 = '01'
  n_bits = 4
  sec_cifr = ''
  text = '1111'

  print('Entradas:')
  print('   - Semilla del Primer Registro:\t' + seed_reg1 + '(25 bits)')
  print('   - Semilla del Segundo Registro:\t' + seed_reg2 + '(31 bits)')
  print('   - Semilla del Tercer Registro:\t' + seed_reg3 + '(33 bits)')
  print('   - Semilla del Cuarto Registro:\t' + seed_reg4 + '(39 bits)')
  print('   - Semilla del Quinto Registro:\t' + seed_reg5 + '(39 bits)')
  print('   - Semilla de R1:\t\t\t' + seed_r1)
  print(u'   - N\xfamero de bits de salida:\t\t' + str(n_bits) + '\n')

  end = 0
  while end < n_bits:
    imp_a = important(LFSR1, seed_reg1)
    imp_b = important(LFSR2, seed_reg2)
    imp_c = important(LFSR3, seed_reg3)
    imp_d = important(LFSR4, seed_reg4)
    imp_e = important(LFSR5, seed_reg5)
    
    x1 = add(imp_a)
    x2 = add(imp_b)
    x3 = add(imp_c)
    x4 = add(imp_d)
    x5 = add(imp_e)

    a = int(seed_reg1[len(seed_reg1) - 1])
    b = int(seed_reg2[len(seed_reg2) - 1])
    c = int(seed_reg3[len(seed_reg3) - 1])
    d = int(seed_reg4[len(seed_reg4) - 1])
    e = int(seed_reg5[len(seed_reg5) - 1])

    seed_r1, z = generator(seed_r1, a, b, c, d, e)
    sec_cifr += str(z)

    print('\n-------------------------------------------------------------------\n')

    seed_reg1 = change(seed_reg1, x1)
    seed_reg2 = change(seed_reg2, x2)
    seed_reg3 = change(seed_reg3, x3)
    seed_reg4 = change(seed_reg4, x4)
    seed_reg5 = change(seed_reg5, x5)

    end += 1
  
  print('Salida: ' + sec_cifr)

  encrypt_text = encrypt(text, sec_cifr)

  print('\nTexto original: ' + text)
  print('Clave: ' + sec_cifr)
  print('Texto cifrado: ' + encrypt_text)

  decrypt_text = encrypt(encrypt_text, sec_cifr)

  print('Texto descrifrado: ' + decrypt_text)
  

main()
