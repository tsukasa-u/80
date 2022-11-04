import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
import io
from PIL import Image, ImageTk 

import multiprocessing
import system3
import math
import copy
import time

class Color_Pallet(system3.Charactor):
    def expand_pallet(self, event, num):
        self.set_bg(0, path=None, image=None, num=num)
        self.set_motion(0, [num], None, repeat=False)
        pass

    def shrink_pallet(self, evemt):
        self.set_bg(0, path=None, image=None, num=0)
        self.set_motion(0, [0], None, repeat=False)

    def request_module_list(self):
        self.connect_write.send({
            "mainmethod": "UNI",
            "modual"    : "center",
            "submethod" : "REIEVE",
            "name"      : "GetModualList",
            "info"      : {}
        })
    
    def get_module_list(self):
        conn_data = self.connect_write.read()["info"]
        if "list" in conn_data.keys():
            return conn_data["list"]
        else:
            return None


    def exert_module(self, event, module):
        self.connect_write.send({
            "mainmethod": "UNI",
            "modual"    : "center",
            "submethod" : "SEND",
            "name"      : "RequestStartModual",
            "info"      : {
                "moudual" : module,
                "func"    : "main",
                "args"    : []
            }
        })

    def get_info(self):
        if self.connect_read.poll():
            data= self.connect_read.recv()
            name = data["name"]
            module = data["modual"]
            if name=="GetPosition":
                self.modual = module    #   果たしてselfでよいのか
                info = data["info"]
                repeat = False
                motion = [self.motion_schedual[0][2]]
                move = info["move"]

                self.set_motion(self.modual, motion, move, repeat=repeat)
                return True
        else:
            return False

# 円グラフを描画
# allmodule = ['chara', 'memo', 'calendar', 'fileseach', 'game', 'sample1', 'sample2']
allmodule = ['chara', 'memo', 'calendar', 'fileseach', 'game', 'sample1', 'sample2', 'sample3', 'sample4', 'sample5', 'sample6']

# root = tk.Tk()
# b_circle = plt.Circle((0,0),1.4,color='Black', fc="Black")
# figb = plt.Figure(figsize=(8,8),dpi=(128))
# figb.patch.set_facecolor('None')
# ringb = figb.add_subplot(111)
# ringb.add_patch(b_circle)
# bufb = io.BytesIO()
# figb.savefig(bufb, format='png')
# imlist = []
# imlist.insert(-1,"imb")
# imlist[-1] = Image.open(bufb)

# conn_r, conn_w = multiprocessing.Pipe(duplex=False)
# path = []
# motion = [0]
# move = None
# number = [-1]
# dele = [0]

# root = tk.Tk()
# Pallet = Color_Pallet(master=root, path=path, number=number, motion=motion, move=move, dele=dele, connect_write=conn_w, connect_read=conn_r, image=imlist, width=256, height=256, root_x=300, root_y=200)

# allmodule = []
# while allmodule:
#     allmodule = Pallet.get_module_list()
#     # allmodule = ['chara', 'memo', 'calendar', 'fileseach', 'game', 'sample1', 'sample2', 'sample3', 'sample4', 'sample5', 'sample6']
#     time.sleep(16)

per1 = []
label1 = []
partmodule = allmodule
partmodule.remove('chara')
color0 = ["#C7243A", "#EDAD0B", "#FFE600", "#A4C520", "#23AC0E", "#007FB1", "#3261AB", "#744199"]
color2 = ["#D5E0F1", "#E5D7EE", "#F6D4D8", "#FCF1D3", "#FFFBD5", "#EEF5D3", "#D1F1CC", "#CAE7F2"]
color3 = ["#BEC7D7", "#CBC0D4", "#DBBEC1", "#E1D6BD", "#E4E0BE", "#D4DBBC", "#BAD7B6", "#B4CDD8"]
color4 = ["#4D4500", "#313B0A", "#0B3404", "#002635", "#0F1D33", "#23132E", "#3C0B11", "#473403"]
color1 = []
if len(partmodule) <= 8:
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

# figlist = ["fig0", "fig1", "fig2", "fig3", "fig4", "fig5", "fig6", "fig7","fig8"]
# ringlist = ["ring0","ring1", "ring2", "ring3", "ring4", "ring5", "ring6", "ring7","ring8"]
# buflist = ["buf0", "buf1", "buf2", "buf3", "buf4", "buf5", "buf6", "buf7", "buf8"]
imlist = ["im0", "im1", "im2", "im3", "im4", "im5", "im6", "im7", "im8"]
lblist = []

explodes = []

if len(partmodule) <= 8:
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


conn_r, conn_w = multiprocessing.Pipe(duplex=False)
path = []
motion = [0]
move = None

if len (partmodule) <= 8:
    number = []
    dele = []
    for i in range(len(partmodule)+1):
        number.insert(i,i)
        dele.insert(i,0)
else:
    number = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    dele = [0, 0, 0, 0, 0, 0, 0, 0, 0]

root = tk.Tk()
Pallet = Color_Pallet(master=root, path=path, number=number, motion=motion, move=move, dele=dele, connect_write=conn_w, connect_read=conn_r, image=imlist, width=256, height=256, root_x=300, root_y=200)
# Pallet = Color_Pallet(master=root, path=path, image=image, number=number, motion=motion, move=move, dele=dele, connect_write=conn_w, connect_read=conn_r)
Pallet.set_button_event((255, 255, 255), Pallet.start_Left, ("Left", "Press"))
Pallet.set_button_event((255, 255, 255), Pallet.pickup_Left, ("Left", "Motion"))
# Pallet.set_image(Color_Pallet.DEFAULT, [], [0], [False], [imlist[1]])
# print(Color_Pallet.DEFAULT)
# Pallet.set_bg(DEFAULT, path=None, image=None)
# Pallet.set_button_event((int("C7", 16), int("24", 16), int("3A", 16)), Pallet.expand_pallet, ("Default", "Motion"), 5)
Pallet.set_bg(0, path=None, image=None, num=0)

for i, modi in enumerate(label1[:8]):
    lblist.append(tk.Label(text=modi, foreground=color4[i], background=color3[i]))
    lblist[-1].place(x=80*math.cos(2*math.pi*(i+0.5)/len(label1)-math.pi/2)+Pallet.width/2-20, y=90*math.sin(2*math.pi*(i+0.5)/len(label1)-math.pi/2)+Pallet.height/2-10)

if len(partmodule)>=1 : lblist[0].bind("<Motion>", lambda event: Pallet.expand_pallet(event, 1))
if len(partmodule)>=2 : lblist[1].bind("<Motion>", lambda event: Pallet.expand_pallet(event, 2))
if len(partmodule)>=3 : lblist[2].bind("<Motion>", lambda event: Pallet.expand_pallet(event, 3))
if len(partmodule)>=4 : lblist[3].bind("<Motion>", lambda event: Pallet.expand_pallet(event, 4))
if len(partmodule)>=5 : lblist[4].bind("<Motion>", lambda event: Pallet.expand_pallet(event, 5))
if len(partmodule)>=6 : lblist[5].bind("<Motion>", lambda event: Pallet.expand_pallet(event, 6))
if len(partmodule)>=7 : lblist[6].bind("<Motion>", lambda event: Pallet.expand_pallet(event, 7))
if len(partmodule)>=8 : lblist[7].bind("<Motion>", lambda event: Pallet.expand_pallet(event, 8))

if len(partmodule)>=1 : lblist[0].bind('<ButtonPress-1>', lambda event: Pallet.expand_pallet(event, 1))
if len(partmodule)>=2 : lblist[1].bind('<ButtonPress-1>', lambda event: Pallet.expand_pallet(event, 2))
if len(partmodule)>=3 : lblist[2].bind('<ButtonPress-1>', lambda event: Pallet.expand_pallet(event, 3))
if len(partmodule)>=4 : lblist[3].bind('<ButtonPress-1>', lambda event: Pallet.expand_pallet(event, 4))
if len(partmodule)>=5 : lblist[4].bind('<ButtonPress-1>', lambda event: Pallet.expand_pallet(event, 5))
if len(partmodule)>=6 : lblist[5].bind('<ButtonPress-1>', lambda event: Pallet.expand_pallet(event, 6))
if len(partmodule)>=7 : lblist[6].bind('<ButtonPress-1>', lambda event: Pallet.expand_pallet(event, 7))
if len(partmodule)>=8 : lblist[7].bind('<ButtonPress-1>', lambda event: Pallet.expand_pallet(event, 8))

for j, cl in enumerate(["#FFFFFF"]+color1):
    cl = cl[1:]
    cl_rgb = [int(cl[i:i+2], 16) for i in range(0, 6, 2)]
    Pallet.set_button_event((cl_rgb[0], cl_rgb[1], cl_rgb[2]), Pallet.expand_pallet, ("Default", "Motion"), j)
    # if j != 0:
    #     lblist[-1].bind("<Motion>", lambda event: Pallet.expand_pallet(event, copy.copy(str(j))))
Pallet.set_button_event(None, Pallet.shrink_pallet, ("Default", "Leave"))

# root2 = tk.Toplevel()
# Chara = system3.Charactor(master=root2, path=["teltel.png"], number=number, motion=motion, move=move, dele=dele, connect_write=conn_w, connect_read=conn_r)
# Chara.set_button_event((0, 0, 0), Chara.start_Left, ("Left", "Press"))
# Chara.set_button_event((0, 0, 0), Chara.pickup_Left, ("Left", "Motion"))

# # Pallet.set_interupt_motion(DEFAULT, motion, move, "Left", repeat=False)
# for i in [1, 2, 3, 4, 5, 6, 7, 8]:
# #     #copyed_i = copy.copy(i)
# #     lblist.append(tk.Label(text=modi, foreground='#ff0000', background='#ffaacc'))
# #     lblist[-1].place(x=80*math.cos(2*math.pi*(i+0.5)/len(label1)-math.pi/2)+Pallet.width/2-20, y=90*math.sin(2*math.pi*(i+0.5)/len(label1)-math.pi/2)+Pallet.height/2-10)
#     # lblist[-1].bind("<Motion>", lambda event: Pallet.expand_pallet(event, copyed_i))
#     print(id(copy.copy(i)), id(i), i)




print(lblist[-1].cget("width"))

Pallet.loop()