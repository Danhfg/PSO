import threading 
import time

from os import system
    
def atualizandoArquivo():
  while True:
    system("grep 'MemTotal\|MemFree\|Cached\|SwapCached\|SwapTotal\|SwapFree' /proc/meminfo > memInfo.dat")
    system("ps -eo pid,min_flt,maj_flt | head --lines=-2 > test.csv")
    time.sleep(0.5)

t = threading.Thread(target=atualizandoArquivo)
t.start()