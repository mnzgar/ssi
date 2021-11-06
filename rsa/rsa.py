import random
import math


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


def Euclides(d, fi):
  x = [d, fi]
  z = [1, 0]
  i = 1

  while x[i] != 0:
    x.append(x[i - 1] % x[i])
    z.append(-(x[i - 1] // x[i]) * z[i] + z[i - 1])
    i += 1
  
  return x[i - 1], z[i - 1]


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


# def codificacion_practica(alph, mod, n, text):
  # j = 1
  # while mod ** j < n:
  #   j += 1
  
  # print('se divide el texto en bloques de ' + str(int(j - 1)) + ' caracteres,'),
  
  # block_text = []
  # block = ''
  # while j < len(text):
  #   for i in range(j):
  #     block += text[j]
  #   block_text.append(block)
  #   j += i - 1
  
  # decimal_text= []

  # for i in block_text:
    
    # dec = 0
    # pos = j - 1
    # k = 0
    # while k < len(i):
    #   dec += alph.find(i[k]) * (mod ** pos)
    #   k += 1
    #   pos -= 1
    # decimal_text.append(dec)


  # print('al pasar el bloque a decimal se obtiene')
  # print(str(decimal_text))




def main():
  # Informacion privada
  p = int(input('p = '))
  while not(LehmanPeralta(p)):
    print('Recuerde que p debe ser primo.')
    p = int(input('p = '))

  q = int(input('q = '))
  while not(LehmanPeralta(q)):
    print('Recuerde que q debe ser primo.')
    q = int(input('q = '))

  fi = (p - 1) * (q - 1)
  d = int(input('d = '))
  x0, e = Euclides(d, fi)
  if e < 0:
    e += fi
  while x0 != 1:
    print('Recuerde que d debe ser primo con fi.')
    d = int(input('d = '))
    x0, e = Euclides(d, fi)
    if e < 0:
      e += fi
  
  # Informacion publica
  n = p * q

  text = int(input('Texto: '))

  print('\nTexto a cifrar: ' + str(text) + ', y los parametros p = ' + str(p) + ', q = ' + str(q) + ' y d = ' + str(d))
  print('\t\tp y q son primos, d es primo con fi(n) = ' + str(fi) + ', y el parametro e = ' + str(e))
  print('\t\tcomo n = ' + str(n) + ','),

  # Cifrar
  alph = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
  mod = len(alph)

  cod = (text ** e) % n
  print('\n\nTexto cifrado: ' + str(cod))
  
  decod = (cod ** d) % n
  print('Texto descifrado: ' + str(decod))
  
  a = (math.log(13, 3)) % 17
  print(a)



main()