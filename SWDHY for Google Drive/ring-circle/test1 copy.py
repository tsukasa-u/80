import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from PIL import Image

# 円グラフを描画
# allmodule = ['chara', 'memo', 'calendar', 'fileseach', 'game', 'sample1', 'sample2']
allmodule = ['chara', 'memo', 'calendar', 'fileseach', 'game', 'sample1', 'sample2', 'sample3', 'sample4', 'sample5', 'sample6']
# n = 5
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
fig1 = plt.Figure()
fig1.patch.set_facecolor('None')

ring0 = fig1.add_subplot(111)
ring0.pie(x, counterclock=False, startangle=90, colors=color1)

img = Image.
img.show()