import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
import io
from PIL import Image, ImageTk 

import multiprocessing
import system1

class Color_Pallet(system1.Charactor):
    pass

# 円グラフを描画
# allmodule = ['chara', 'memo', 'calendar', 'fileseach', 'game', 'sample1', 'sample2']
allmodule = ['chara', 'memo', 'calendar', 'fileseach', 'game', 'sample1', 'sample2', 'sample3', 'sample4', 'sample5', 'sample6']
per1 = []
label1 = []
partmodule = allmodule
partmodule.remove('chara')
color0 = ["#C7243A", "#EDAD0B", "#FFE600", "#A4C520", "#23AC0E", "#007FB1", "#3261AB", "#744199"]
color1 = []
if len (partmodule) <= 8:
    for i in range(len(partmodule)):
        per1.insert(i, 1)
        label1.insert(i,partmodule[i])
        color1.insert(i,color0[i])
else:
    for i in range(8):
        per1.insert(i, 1)
        label1.insert(i,partmodule[i])
    color1 = color0

x = np.array(per1)

#plt.pie(x, counterclock=False, startangle=90, colors=color1, wedgeprops={'linewidth': 2, 'edgecolor':"Black"})
#plt.axis('equal')

# 中心(0,0)に70%の大きさで円を描画
#centre_circle = plt.Circle((0, 0), 0.45, color='black', fc='white', linewidth=1.25)
#fig = plt.gcf()
#fig.gca().add_artist(centre_circle)

#plt.show()

fig1 = plt.Figure(figsize=(8,8),dpi=(64))
fig1.patch.set_facecolor('None')

ring0 = fig1.add_subplot(111)
ring0.pie(x, counterclock=False, startangle=90, colors=color1, wedgeprops={'linewidth': 2, 'edgecolor':"Black"}, radius=1.5)

center_circle = plt.Circle((0,0),0.6,color='Black', fc="White")
ring2 = fig1.add_subplot(111)
ring2.add_patch(center_circle)

# plt.pie(x, counterclock=False, startangle=90, colors=color1, wedgeprops={'linewidth': 2, 'edgecolor':"Black"})
# centre_circle = plt.Circle((0,0),0.6,color='black', fc='white',linewidth=1.25)
# fig = plt.gcf()
# fig.gca().add_artist(centre_circle)

buf = io.BytesIO()
fig1.savefig(buf, format='png')
im = Image.open(buf)

## When windows is closed.
def _destroyWindow():
    root.quit()
    root.destroy()
## Tkinter Class
root = tk.Tk()
root.withdraw()
root.protocol('WM_DELETE_WINDOW', _destroyWindow)  # When you close the tkinter window.
## Canvas
canvas = FigureCanvasTkAgg(fig1, master=root)  # Generate canvas instance, Embedding fig in root
canvas.draw()
canvas.get_tk_widget().pack()
##canvas._tkcanvas.pack()
## root
root.update()
root.deiconify()
root.mainloop()


## conn_r, conn_w = multiprocessing.Pipe(duplex=False)

# path = []
# number = [0]
# motion = [0]
# move = None
# dele = [False]

# root = tk.Tk()
# Pallet = Color_Pallet(master=root, path=path, number=number, motion=motion, move=move, dele=dele, connect_write=conn_w, connect_read=conn_r, image=[im])

## motion = [0]
## move = None
## Chara.set_interupt_motion(DEFAULT, motion, move, "Left", repeat=False)

## Chara.set_button_event((0, 0, 0), Pallet.pickup_Left, ("Left", "Motion"))

# Pallet.loop()