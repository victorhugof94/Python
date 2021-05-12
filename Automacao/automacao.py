import pyautogui as pg
import time 
import pyperclip as pc

pg.PAUSE = 1
pg.alert('Vamos Registrar o Horario')
# para abrir o navegador do chrome
pg.press('win')
pg.write('chrome')
pg.press('enter')
# copiando link para o navegador
link = 'url'
pc.copy(link)
pg.hotkey('ctrl','v')
pg.press('enter')
time.sleep(5)

pg.click(1753,200)
pg.click(1690,246)

tempo = '8h'
pc.copy(tempo)
pg.hotkey('ctrl','v')

pg.click(1008,389)
pg.hotkey('pagedown','pagedown', 'pagedown','pagedown','pagedown','pagedown','pagedown','pagedown', 'pagedown' )
pg.click(1026,659)
pg.click(1026,659)

pg.alert('Horario Registrado')