import numpy as np
import matplotlib.pyplot as plt

def make_autopct(values):
    def my_autopct(pct):
        total = sum(values)
        val = int(round(pct*total/100.0))
        return '{p:.2f}%  ({v:d})'.format(p=pct,v=val)
    return my_autopct

plt.axis([0, 10, 0, 1])
x = [1,2,3,4]
i = 0
while True:
    plt.title("Monitorando MEMORIA")
    plt.pie(x, labels=["T1", "T2", "T3", "T4"],autopct=make_autopct(x),shadow=True, startangle=90)
    plt.draw()
    plt.pause(0.5)
    plt.clf()
    x[i%4]+=10
    i+=1

plt.show()
