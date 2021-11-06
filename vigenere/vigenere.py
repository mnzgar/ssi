# cambiar longitud de la palabra clave
def change_key(message, key):
  new_key = ''
  if len(message) == len(key):
    new_key = key

  elif len(message) > len(key):
    for i in range(int(len(message) / len(key))):
      new_key += key
    new_key += key[:len(message) % len(key)]

  else:
    new_key = key[:len(message)]

  return new_key


def write(string, key):
  j = 0
  for i in range(len(string)):
    print(string[i], end="")
    j += 1
    if j == len(key):
      print('\t', end="")
      j = 0
  print('\n', end="")


# encriptar
def encrypt(message, key, alphabet):
  encrypted = ''
  for i in range(len(message)):
    x = alphabet.find(message[i])
    y = alphabet.find(key[i])
    sum = x + y
    mod = sum % len(alphabet)
    encrypted += alphabet[mod]
  return encrypted


# desencriptar
def decrypt(message, key, alphabet):
  decrypted = ''
  for i in range(len(message)):
    x = alphabet.find(message[i])
    y = alphabet.find(key[i])
    dif = x - y
    mod = dif % len(alphabet)
    decrypted += alphabet[mod]
  return decrypted


# main del programas
def main():
  alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ=>?@'

  # ej (encriptar)
  print('CIFRADO\n')
  key = 'MISION'
  message = 'ESTE MENSAJE SE AUTODESTRUIRA'

  print('Palabra clave:\t' + key)
  print('Texto original:\t' + message + '\n')

  message = message.replace(' ', '')

  new_key = change_key(message, key)
  encrypt_message = encrypt(message, new_key, alphabet)

  write(message, key)
  write(new_key, key)
  write(encrypt_message, key)

  print('\nTexto cifrado: ' + encrypt_message)

  # ej (desencriptar)
  print('\n\nDESCIFRADO\n')
  print('Palabra clave:\t' + key)
  print('Texto cifrado:\t' + encrypt_message + '\n')

  decrypt_message = decrypt(encrypt_message, new_key, alphabet)

  write(encrypt_message, key)
  write(new_key, key)
  write(decrypt_message, key)

  print('\nTexto original:\t' + decrypt_message)

main()
