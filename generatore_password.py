import random
caratteri="+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

numero=int(input("inserisci un numero"))

password=""

for i in range(numero):
    password+= random.choice(caratteri)
print(password)