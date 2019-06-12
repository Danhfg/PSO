import keyboard
import time

aux = ""
def setAux(a):
    aux = a
def func(pos, aux):
    print(aux)
    aux = pos
    setAux(pos)

keyboard.add_hotkey('a', func, args=('A', aux))
keyboard.add_hotkey('s', func, args=('S', aux))
keyboard.add_hotkey('d', func, args=('D', aux))
keyboard.add_hotkey('w', func, args=('W', aux))
#keyboard.add_hotkey('a', print, args=('LEFT'))

while True:
    #keyboard.wait()
    print(aux)
    
    time.sleep(0.5)