import random
import time

from pyautogui import sleep
comp = random.randint(0,5)
print (' Ja tenho minha escolha agora sua vez escolha uma numero de 0 a 5 ')
jog= int(input("qual o seu numero:"))
print('vamos ver se esta igual')
sleep(3)
if jog==comp:
    print('voce acertou')
else:
    print('voce errou')