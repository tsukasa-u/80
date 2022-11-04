import numpy as np
import matplotlib.pyplot as plt
import importlib
import tkinter as tk
#from PIL import Image

# 円グラフを描画
allmodule = ['chara', 'memo', 'calendar', 'fileseach', 'game', 'sample1', 'sample2']
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

fig = plt.figure()
fig.patch.set_facecolor('None')
x = np.array(per1)
# plt.pie(x, labels=label1, counterclock=False, startangle=90, colors=color1)
plt.pie(x, counterclock=False, startangle=90, colors=color1)

# plt.show()


# ウィンドウ作成
root = tk.Tk()
root.title("榛名")
root.minsize(796, 816)
 
# 画像表示
#fileに適当なpng画像を指定してください。
# fig2 = tk.PhotoImage(data=plt)
fig2 = tk.PhotoImage(data="plt")
 
canvas = tk.Canvas(bg="black", width=796, height=816)
canvas.place(x=0, y=0)
canvas.create_image(0, 0, image=fig2, anchor=tk.NW)
 
# メインループ
root.mainloop()

#org = Image
#trans = Image.new('RGBA', org.size, (0, 0, 0, 0))
#width = org.size[0]
#height = org.size[1]
#for x in xrange(width):
#    for y in xrange(height):
#        pixel = org.getpixcel((x,y))
#        if pixel[0] == 225 and pixel[1] == 255 and pixcel[2] == 255:
#            continue
#        trans.putpixel((x,y),pixel)
#
#trans.show()

