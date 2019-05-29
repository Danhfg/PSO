import numpy as np
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
import threading 
import time

from os import system
from re import split

def make_autopct(values):
    def my_autopct(pct):
        total = sum(values)
        val = int(round(pct*total/100.0))
        return '{p:.2f}%  ({v:d})'.format(p=pct,v=val)
    return my_autopct

def tratamentoArquivo( conteudoArquivo ):
    listaInformacoes = []
    for linha in conteudoArquivo:
        c = split('kB|:', linha)
        listaInformacoes.append(int(c[1].strip()))
    return listaInformacoes

the_grid = GridSpec(2, 3)

winOpen = True

while winOpen:
    try:
        arqMemInfo = open("memInfo.dat", 'r')

        conteudoArqMemInfo = arqMemInfo.readlines()

        lista =  tratamentoArquivo(conteudoArqMemInfo)

        labels1 = 'Memória Usada', 'Memória Livre'

        labels2 = 'Cached', 'SwapCached'

        labels3 = 'Swap Total', 'Swap Livre'

        fracs1 = [lista[0]-lista[1], lista[1]]

        fracs2 = lista[2:4]

        fracs3 = [lista[4]-lista[5], lista[5]]

        plt.subplot(the_grid[0, 0], aspect=1, title="MONITORANDO RAM")

        plt.pie(fracs1, labels=labels1, autopct=make_autopct(fracs1), shadow=True)

        plt.subplot(the_grid[0, 2], aspect=1, title="MONITORANDO CACHE")

        plt.pie(fracs2, labels=labels2, autopct=make_autopct(fracs2),shadow=True)

        plt.subplot(the_grid[1, 1], aspect=1, title="MONITORANDO SWAP")

        plt.pie(fracs2, labels=labels3, autopct=make_autopct(fracs2),shadow=True)

        plt.draw()

        plt.pause(0.5)

        if plt.get_fignums():
            plt.clf()
            continue
        else:
            winOpen = False
    except:
        pass

plt.show()
