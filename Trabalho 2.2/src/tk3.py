import psutil
import tkinter as tk
import pandas as pd
import pandastable

def update_model():
    df = pd.read_csv("test.csv", delim_whitespace=True)
    table.updateModel(pandastable.TableModel(df))


def update_title(set_smu=False):
    update_model()
    table.redraw()
    #root.title('total: {:.2f}MB - added per redraw: {:.2f}kB'
    #           .format(mem / 1000**2, (S/N)/1000))
    root.after(5000, update_title)

if __name__ == '__main__':
    me = psutil.Process()
    root = tk.Tk()
    frame = tk.Frame(root)
    table = pandastable.Table(frame)
    table.show()
    frame.pack(fill='both', expand=True)
    root.after(1000, update_title, True)
    update_model()
    root.update()
    #root.after(1000 + DURATION*1000, root.destroy)
    root.mainloop()
    #print('{:.2f} cycles/second'.format(N/DURATION))
    #print('{:.2f} kB/cycle'.format((S/N)/1000))
    #print('{:.2f} MB gained'.format((me.memory_full_info().uss-smu)/1000**2))