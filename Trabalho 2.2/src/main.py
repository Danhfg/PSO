import threading 
import time

from os import system
from re import split

def tratamentoArquivo( conteudoArquivo ):
  listaInformacoes = []
  for linha in conteudoArquivo:
    c = split('kB|:', linha)
    listaInformacoes.append(c[1].strip())
  return listaInformacoes
    
def atualizandoArquivo():
  while True:
    system("grep 'MemTotal\|MemFree\|Cached\|SwapCached\|SwapTotal\|SwapFree' /proc/meminfo > memInfo.dat")
    system("ps -eo pid,min_flt,maj_flt | head --lines=-2 > test.csv")
    time.sleep(0.5)

arqMemInfo = open("memInfo.dat", 'r')
conteudoArqMemInfo = arqMemInfo.readlines()

comando = "ps -eo pid,min_flt,maj_flt --no-header | head --lines=-2";

tratamentoArquivo( conteudoArqMemInfo)

t = threading.Thread(target=atualizandoArquivo)
t.start()