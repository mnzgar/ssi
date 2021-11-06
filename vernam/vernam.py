import random

# de ascii a binario
def binary(message):
  return ''.join([bin(ord(x))[2:].zfill(8) for x in message])

# de binario a ascii
def ascii(binary_message):
  message = ""
  while binary_message != "":
    i = chr(int(binary_message[:8], 2))
    message += i
    binary_message = binary_message[8:]
  return message

# puerta xor
def xor(b, k):
  return ''.join(str(ord(x) ^ ord(y)) for x, y in zip(b, k))

# encriptar
def encrypt(binary_message, key):
  encrypted = ''
  for i in range(len(key)):
    encrypted += xor(binary_message[i], key[i])
  return(encrypted)

# desencriptar
def decrypt(encrypt_binary_message, key):
  decrypted = ''
  for i in range(len(key)):
    decrypted += xor(encrypt_binary_message[i], key[i])
  return(decrypted)

# main del programa
def main():
  # ej 1 (encriptar)
  print('CIFRADO\n')

  message1 = 'SOL'
  binary_message1 = binary(message1)
  # key1 = '001111000001100001110011'
  key1 = ''
  for i in range(len(binary_message1)):
      key1 += str(random.randint(0, 1))

  print('Mensaje original:\t\t' + message1)
  print('Mensaje original en binario:\t' + binary_message1)
  print('Longitud del mensaje binario:\t' + str(len(binary_message1)))
  print('\nClave aleatoria:\t\t' + key1)

  encrypt_binary_message1 = encrypt(binary_message1, key1)
  encrypt_message1 = ascii(encrypt_binary_message1)

  print('\nMesaje cifrado en binario:\t' + encrypt_binary_message1)
  print('Mesaje cifrado:\t\t\t' + str(encrypt_message1))

  # ej 2 (desencriptar)
  print('\n\nDESCIFRADO\n')
  encrypt_message2 = '[t'
  encrypt_binary_message2 = binary(encrypt_message2)
  key2 = '0000111100100001'

  print('Mensaje cifrado:\t\t' + encrypt_message2)
  print('Mensaje cifrado en binario:\t' + encrypt_binary_message2)
  print('Longitud del mensaje binario:\t' + str(len(encrypt_binary_message2)))
  print('\nClave aleatoria:\t\t' + key2)

  binary_message2 = decrypt(encrypt_binary_message2, key2)
  message2 = ascii(binary_message2)

  print('\nMensaje original en binario:\t' + binary_message2)
  print('Mensaje original:\t\t' + message2)

main()
