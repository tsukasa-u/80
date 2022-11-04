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

fig1 = plt.Figure(figsize=(8,8),dpi=(128))
fig1.patch.set_facecolor('None')
ring0 = fig1.add_subplot(111)
ring0.pie(x, counterclock=False, startangle=90, colors=color1, wedgeprops={'linewidth': 2, 'edgecolor':"Black"}, radius=1.5)
center_circle = plt.Circle((0,0),0.65,color='Black', fc="White")
ring2 = fig1.add_subplot(111)
ring2.add_patch(center_circle)

# plt.pie(x, counterclock=False, startangle=90, colors=color1, wedgeprops={'linewidth': 2, 'edgecolor':"Black"})
# centre_circle = plt.Circle((0,0),0.6,color='black', fc='white',linewidth=1.25)
# fig = plt.gcf()
# fig.gca().add_artist(centre_circle)

buf = io.BytesIO()
fig1.savefig(buf, format='png')
im = Image.open(buf)

## center_circle = plt.Circle((0,0),0.4,color='Black', fc="White")
## ring1 = ring0.gcf()
## ring1.gca().add_artist(center_circle)

## When windows is closed.
# def _destroyWindow():
    # root.quit()
    # root.destroy()
## Tkinter Class
# root = tk.Tk()
# root.withdraw()
# root.protocol('WM_DELETE_WINDOW', _destroyWindow)  # When you close the tkinter window.
## Canvas
# canvas = FigureCanvasTkAgg(fig1, master=root)  # Generate canvas instance, Embedding fig in root
# canvas.draw()
# canvas.get_tk_widget().pack()
##canvas._tkcanvas.pack()
## root
# root.update()
# root.deiconify()
# root.mainloop()


conn_r, conn_w = multiprocessing.Pipe(duplex=False)

path = []
number = [0]
motion = [0]
move = None
dele = [False]

root = tk.Tk()
Pallet = Color_Pallet(master=root, path=path, number=number, motion=motion, move=move, dele=dele, connect_write=conn_w, connect_read=conn_r, image=[im])
Pallet.set_button_event((0, 0, 0), Pallet.start_Left, ("Left", "Press"))
Pallet.set_button_event((0, 0, 0), Pallet.pickup_Left, ("Left", "Motion"))


# root2 = tk.Tk()
root2 = tk.Toplevel()
Chara = system1.Charactor(master=root2, path=["teltel.png"], number=number, motion=motion, move=move, dele=dele, connect_write=conn_w, connect_read=conn_r)
Chara.set_button_event((0, 0, 0), Chara.start_Left, ("Left", "Press"))
Chara.set_button_event((0, 0, 0), Chara.pickup_Left, ("Left", "Motion"))

# Chara.loop()

Pallet.loop()