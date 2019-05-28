import numpy as np
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

def make_autopct(values):
    def my_autopct(pct):
        total = sum(values)
        val = int(round(pct*total/100.0))
        return '{p:.2f}%  ({v:d})'.format(p=pct,v=val)
    return my_autopct

labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
fracs = [15, 30, 45, 10]
fracs2 = [10,10,10,10]

the_grid = GridSpec(1, 2)
i = 0
winOpen = True
while winOpen:

    plt.subplot(the_grid[0, 0], aspect=1, title="MONITORANDO RAM")

    plt.pie(fracs, labels=labels, autopct=make_autopct(fracs), shadow=True)

    plt.subplot(the_grid[0, 1], aspect=1, title="MONITORANDO CACHE")

    plt.pie(fracs2, labels=labels, autopct=make_autopct(fracs2),shadow=True)

    plt.draw()

    plt.pause(0.5)
    fracs[i%4]+=10
    fracs2[i%4]+=10
    i+=1
    if plt.get_fignums():
        plt.clf()
        continue
    else:
        winOpen = False



plt.show()
