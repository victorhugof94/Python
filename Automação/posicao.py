import pyautogui
import time
pyautogui.alert("Escolha a posição")
time.sleep(4)
print(pyautogui.position())
pyautogui.alert("Posição Registrada")