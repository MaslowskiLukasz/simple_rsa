from math import sqrt, gcd
from sympy import nextprime
from random import randint
from itertools import count, islice

def is_prime(n):
    return n > 1 and all(n % i for i in islice(count(2), int(sqrt(n) - 1)))

#generowanie klucza: 
#czynność przykład wybieramy dwie liczby pierwsze p i q -> p = 31, q = 19
#obliczamy n = p · q -> n = 589
#obliczamy φ(n) = (p – 1)(q – 1); -> φ(n)= 540
#generujemy e jako liczbę względnie pierwszą z φ(n) czyli taką, 
  #która jest liczbą pierwszą i dla której największy wspólny
  #dzielnik z φ(n) wynosi 1 -> e = 7 
#generujemy d w taki sposób, aby spełniona była zależność:
  #iloczyn e i d przystaje do 1 modulo φ(n),
  #co oznacza, że φ(n) dzieli wyrażenia e · d – 1. -> d = 463  
#Para e i n stanowią klucz publiczny, natomiast para d i n
  #jest kluczem prywatnym. 
def next_e(phi):
  random = randint(1, 100)
  prime = nextprime(random)
  while gcd(prime, phi) != 1:
    random = randint(1, 100)
    prime = nextprime(random)
  return prime
  
def generate_d(e, phi):
  d = 0
  d = randint(1, phi)
  while (e * d) % phi != 1:
    d = randint(1, phi)
  return d

def generate_key():
  p = nextprime(randint(1000, 9972))
  q = nextprime(randint(1000, 9972))
  n = p * q
  phi = (p - 1) * (q - 1)
  e = next_e(phi)
  d = generate_d(e, phi)
  print(f"p = {p}")
  print(f"q = {q}")
  print(f"n = {n}")
  print(f"phi = {phi}")
  print(f"e = {e}")
  print(f"d = {d}")
  return [e, n], [d, n]


#szyfrowanie wiadomości:  
#czynność przykład 
#c = m^e mod n; gdzie c oznacza wiadomość zaszyfrowaną, a m wiadomość jawną. 
#m = 8 
#c = 8^7 mod 589 = 312 
def encrypt(msg, public_key):
  return pow(msg, public_key[0], mod=public_key[1])


#deszyfrowanie wiadomości:  
#czynność przykład 
#m = c^d mod n; gdzie c oznacza wiadomość zaszyfrowaną, a m wiadomość jawną. 
#c = 312 
#m = 312^463 mod 589 = 8 
def decrypt(msg, private_key):
  return pow(msg, private_key[0], mod=private_key[1])