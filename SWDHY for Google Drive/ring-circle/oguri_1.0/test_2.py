import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
import io
from PIL import Image, ImageTk 

import multiprocessing
import system2

class Color_Pallet(system2.Charactor):
    def expand_pallet(self, event, num):
        self.set_bg(0, path=None, image=None, num=num)
        self.set_motion(0, [num], None, repeat=False)
        pass

    def shrink_pallet(self, evemt):
        self.set_bg(0, path=None, image=None, num=0)
        self.set_motion(0, [0], None, repeat=False)

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

# fig0 = plt.Figure(figsize=(8,8),dpi=(128))
# fig0.patch.set_facecolor('None')
# ring0 = fig0.add_subplot(111)
# ring0.pie(x, counterclock=False, startangle=90, colors=color1, wedgeprops={'linewidth': 2, 'edgecolor':"Black"}, radius=1.5)

# figlist = ["fig0", "fig1", "fig2", "fig3", "fig4", "fig5", "fig6", "fig7","fig8"]
# ringlist = ["ring0","ring1", "ring2", "ring3", "ring4", "ring5", "ring6", "ring7","ring8"]
# buflist = ["buf0", "buf1", "buf2", "buf3", "buf4", "buf5", "buf6", "buf7", "buf8"]
imlist = ["im0", "im1", "im2", "im3", "im4", "im5", "im6", "im7", "im8"]

explodes = []

center_circle = plt.Circle((0,0),0.65,color='Black', fc="White")

if len (partmodule) <= 8:
    for i in range(len(partmodule)-1):
        explodes.insert(0,0)
    for i in range(len(partmodule)+1):
        if i == 0:
            explodes.insert(0, 0)
        else:
            explodes.insert(0,0)
            explodes.pop(i-1)
            explodes.insert(i-1, 0.2)
            explodes.pop(i)
        # figlist[i] = plt.Figure(figsize=(8,8),dpi=(128))
        # figlist[i].patch.set_facecolor('None')
        # ringlist[i] = figlist[i].add_subplot(111)
        # ringlist[i].pie(x, counterclock=False, startangle=90, colors=color1, wedgeprops={'linewidth': 2, 'edgecolor':"Black"}, radius=1.4, explode=explodes)
        # center_circle = plt.Circle((0,0),0.65,color='Black', fc="White")
        # ringc = figlist[i].add_subplot(111)
        # ringc.add_patch(center_circle)
        # buflist[i] = io.BytesIO()
        # figlist[i].savefig(buflist[i], format='png')
        # imlist[i] = Image.open(buflist[i])
        fig = plt.Figure(figsize=(8,8),dpi=(128))
        fig.patch.set_facecolor('None')
        ring = fig.add_subplot(111)
        ring.pie(x, counterclock=False, startangle=90, colors=color1, wedgeprops={'linewidth': 2, 'edgecolor':"Black"}, radius=1.4, explode=explodes)
        center_circle = plt.Circle((0,0),0.65,color='Black', fc="White")
        ringc = fig.add_subplot(111)
        ringc.add_patch(center_circle)
        buf = io.BytesIO()
        fig.savefig(buf, format='png')
        imlist[i] = Image.open(buf)
        # buflist[i] = io.BytesIO()
        # fig.savefig(buflist[i], format='png')
        # imlist[i] = Image.open(buflist[i])
else:
    explodes = [0, 0, 0, 0, 0, 0, 0]
    for i in range(9):
        if i == 0:
            explodes.insert(0, 0)
        else:
            explodes.insert(0,0)
            explodes.pop(i-1)
            explodes.insert(i-1, 0.2)
            explodes.pop(i)
        # figlist[i] = plt.Figure(figsize=(8,8),dpi=(128))
        # figlist[i].patch.set_facecolor('None')
        # ringlist[i] = figlist[i].add_subplot(111)
        # ringlist[i].pie(x, counterclock=False, startangle=90, colors=color1, wedgeprops={'linewidth': 2, 'edgecolor':"Black"}, radius=1.4, explode=explodes)
        # center_circle = plt.Circle((0,0),0.65,color='Black', fc="White")
        # ringc = figlist[i].add_subplot(111)
        # ringc.add_patch(center_circle)
        # buflist[i] = io.BytesIO()
        # figlist[i].savefig(buflist[i], format='png')
        # imlist[i] = Image.open(buflist[i])
        fig = plt.Figure(figsize=(8,8),dpi=(128))
        fig.patch.set_facecolor('None')
        ring = fig.add_subplot(111)
        ring.pie(x, counterclock=False, startangle=90, colors=color1, wedgeprops={'linewidth': 2, 'edgecolor':"Black"}, radius=1.4, explode=explodes)
        center_circle = plt.Circle((0,0),0.65,color='Black', fc="White")
        ringc = fig.add_subplot(111)
        ringc.add_patch(center_circle)
        buf = io.BytesIO()
        fig.savefig(buf, format='png')
        imlist[i] = Image.open(buf)
        # buflist[i] = io.BytesIO()
        # fig.savefig(buflist[i], format='png')
        # imlist[i] = Image.open(buflist[i])


# ring0.add_patch(center_circle)


# buf = io.BytesIO()
# figlist[3].savefig(buf, format='png')
# im = Image.open(buf)

# im.show()

conn_r, conn_w = multiprocessing.Pipe(duplex=False)

path = []
# image = [
#     "imlist[0]"
#     "imlist[1]"
#     "imlist[2]"
#     "imlist[3]"
#     "imlist[4]"
#     "imlist[5]"
#     "imlist[6]"
#     "imlist[7]"
#     "imlist[8]"
#     ]
number = [0, 1, 2, 3, 4, 5, 6, 7, 8]
# number = [0, 1, 2, 3, 4, 5, 6, 7]
motion = [0]
# motion = [0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, ]
move = None
dele = [0, 0, 0, 0, 0, 0, 0, 0, 0]
# dele = [0, 0, 0, 0, 0, 0, 0, 0]

root = tk.Tk()
Pallet = Color_Pallet(master=root, path=path, number=number, motion=motion, move=move, dele=dele, connect_write=conn_w, connect_read=conn_r, image=imlist, width=256, height=256, root_x=100, root_y=200)
# Pallet = Color_Pallet(master=root, path=path, image=image, number=number, motion=motion, move=move, dele=dele, connect_write=conn_w, connect_read=conn_r)
Pallet.set_button_event((255, 255, 255), Pallet.start_Left, ("Left", "Press"))
Pallet.set_button_event((255, 255, 255), Pallet.pickup_Left, ("Left", "Motion"))
# Pallet.set_image(Color_Pallet.DEFAULT, [], [0], [False], [imlist[1]])
# print(Color_Pallet.DEFAULT)
# Pallet.set_bg(DEFAULT, path=None, image=None)
# Pallet.set_button_event((int("C7", 16), int("24", 16), int("3A", 16)), Pallet.expand_pallet, ("Default", "Motion"), 5)
Pallet.set_bg(0, path=None, image=None, num=0)
for j, cl in enumerate(["#FFFFFF"]+color0):
    cl = cl[1:]
    cl_rgb = [int(cl[i:i+2], 16) for i in range(0, 6, 2)]
    Pallet.set_button_event((cl_rgb[0], cl_rgb[1], cl_rgb[2]), Pallet.expand_pallet, ("Default", "Motion"), j)
Pallet.set_button_event(None, Pallet.shrink_pallet, ("Default", "Leave"))

Pallet.loop()