# Divide el segundo byte en los 1
def divide(b):
  b = b[::-1]
  index = ''

  for i in range(len(b)):
    if b[i] == '1':
      index += str(i)

  bytes = []
  for i in index:
    tmp = ''
    for j in range(len(b)):
      if int(i) == j:
        tmp += '1'
      else:
        tmp += '0'
    bytes.append(tmp)

  return bytes, index


# Calcula la tabla
def table(b1, alg, index):
  bytes = []
  for i in range(int(index[len(index) - 1])):
    if i == 0:
      print('\033[1m   ' + str(i) + ' -> \033[0;33m' + b1 + '\033[0;0m')
      for j in index:
        if i == int(j):
          bytes.append(b1)

    if b1[0] == '0':
      b1 = b1[1:]
      b1 += '0'
      print('\033[1m   ' + str(int(i + 1)) + ' -> \033[0;0m' + b1)
      for j in index:
        if i + 1 == int(j):
          bytes.append(b1)
    
    else:
      b1 = b1[1:]
      b1 += '0'
      tmp = ''
      for j in range(len(alg)):
        tmp += str(int(b1[j]) ^ int(alg[j]))
      print('\033[1m   ' + str(int(i + 1)) + ' -> \033[0;0m' + b1 + ' + ' + '\033[0;31m' + alg + '\033[0;0m' + ' = ' + tmp)
      b1 = tmp
      for j in index:
        if i + 1 == int(j):
          bytes.append(b1)
  
  return bytes


# Suma binaria
def add(bytes):
  mul = ''
  for i in range(len(bytes[0])):
    tmp = 0
    for j in bytes:
      tmp ^= int(j[i])
    mul += str(tmp)
  return mul


# Cifrado
def encrypt(text, sec_cifr):
  encrypted = ''
  for i, j in zip(text, sec_cifr):
    encrypted += str(int(i) ^ int(j))
  return encrypted



def main():
  algorithm = ['SMOW 3G', 'AES']
  algorithm_byte = ['10101001', '00011011']
  byte1 = 'AA'
  byte2 = '34'
  opc = int(input('0: SNOW 3G\n1: AES\n> Que algoritmo quiere hacer? '))

  # Imprimir entradas
  print('\nEntradas:')
  print('   - Primer byte:\t' + byte1)
  print('   - Segundo byte:\t' + byte2)
  print('   - Algoritmo:\t\t' + algorithm[opc])

  byte1 = bin(int(byte1, 16)).replace('0b', '').zfill(8)
  byte2 = bin(int(byte2, 16)).replace('0b', '').zfill(8)

  # Dividir byte
  bytes, index = divide(byte2)
  print(u'\nDonde la operaci\xf3n ' + '\033[0;33m' + byte1 + '\033[0m' + ' x ' + bytes[len(bytes) - 1] + ' resulta de los pasos:')
  
  # Calcular tabla y sumar el resultado
  bytes_table = table(byte1, algorithm_byte[opc], index)
  multiplication = add(bytes_table)

  # Imprimir la operacion
  print(u'\nResultante de la operaci\xf3n:\n  '),
  print('\033[0;33m' + byte1 + '\033[0m' + ' x ' + byte2 + ' ='),
  
  for i in range(len(bytes) - 1, -1, -1):
    print('\033[0;33m' + byte1 + '\033[0m' + ' x ' + bytes[i]),
    if i == 0:
      print('=\n  '),
    else:
      print(' + '),
  
  for i in range(len(bytes_table)):
    print('\033[0;32m' + bytes_table[i] + '\033[0m'),
    if i == len(bytes) - 1:
      print('='),
    else:
      print('+'),
  
  print(multiplication)

  # Imprimir salida
  print('\nSalida:')
  print('   - Primer byte:\t' + '\033[0;33m' + byte1 + '\033[0m')
  print('   - Segundo byte:\t' + byte2)
  print('   - Byte Algoritmo:\t' + '\033[0;31m' + algorithm_byte[opc] + '\033[0m')
  print(u'   - Multiplicaci\xf3n:\t' + multiplication)


  # Cifrar texto ascii
  text = 'S'
  print('\nTexto original:\t\t' + text)

  text = bin(ord(text)).replace('0b', '').zfill(8)
  print('Texto binario:\t\t' + text)
  print('Secuencia cifrante:\t' + multiplication)

  encrypt_text = encrypt(text, multiplication)
  print('Texto cifrado:\t\t' + encrypt_text)
  
  decrypt_text = encrypt(encrypt_text, multiplication)
  print('Texto descrifrado:\t' + decrypt_text)


main()