#!/usr/bin/env python3


# https://matplotlib.org/gallery/user_interfaces/embedding_in_tk_sgskip.html
# https://matplotlib.org/gallery/animation/simple_anim.html


import tkinter

from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.figure import Figure
import matplotlib.animation as animation

import numpy as np


def _quit():
    root.quit()     # stops mainloop
    root.destroy()  # this is necessary on Windows to prevent
                    # Fatal Python Error: PyEval_RestoreThread: NULL tstate


def init():  # only required for blitting to give a clean slate.
    line.set_ydata(np.sin(x))
    return line,


def animate(i):
    line.set_ydata(np.sin(x + i))  # update the data.
    return line,


root = tkinter.Tk()
root.wm_title("Embedding in Tk anim")

fig = Figure()
# FuncAnimationより前に呼ぶ必要がある
canvas = FigureCanvasTkAgg(fig, master=root)  # A tk.DrawingArea.

x = np.arange(0, 3, 0.01)  # x軸(固定の値)
l = np.arange(0, 8, 0.01)  # 表示期間(FuncAnimationで指定する関数の引数になる)
plt = fig.add_subplot(111)
plt.set_ylim([-1.1, 1.1])
line, = plt.plot(x, np.sin(x))

ani = animation.FuncAnimation(fig, animate, l,
    init_func=init, interval=10, blit=True,
    )

toolbar = NavigationToolbar2Tk(canvas, root)
canvas.get_tk_widget().pack()

button = tkinter.Button(master=root, text="Quit", command=_quit)
button.pack()

tkinter.mainloop()