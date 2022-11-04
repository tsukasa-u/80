from PIL import Image, ImageDraw
import tkinter as tk

import multiprocessing
import system1

class Color_Pallet(system1.Charactor):
    pass

# im = Image.new('RGB', (600, 250), (128, 128, 128))
# draw = ImageDraw.Draw(im)

# im = Image.new('None', (300, 300), )
im = Image.new('RGBA', (1024,1024), (0, 0, 0, 0) )
draw = ImageDraw.Draw(im)

n = 8
i = 0

allmodule = ['chara', 'memo', 'calendar', 'fileseach', 'game', 'sample1', 'sample2', 'sample3', 'sample4', 'sample5', 'sample6']
# allmodule = ['chara', 'memo', 'calendar', 'fileseach', 'game', 'sample1']
# n = 5
per1 = []
label1 = []
partmodule = allmodule
partmodule.remove('chara')
color0 = ["#C7243A", "#EDAD0B", "#FFE600", "#A4C520", "#23AC0E", "#007FB1", "#3261AB", "#744199"]
if len(partmodule) <= 8:
    n = len(partmodule)
    for i in range(n):
        per1.insert(i, 1)
        label1.insert(i,partmodule[i])
        draw.pieslice((0, 0, 1024, 1024), start=360/n*i-90, end=360/n*(i+1)-90, fill=(color0[i]), outline=(color0[i]))
else:
    n = 8
    for i in range(8):
        per1.insert(i, 1)
        label1.insert(i,partmodule[i])
        draw.pieslice((0, 0, 1024, 1024), start=360/n*i-90, end=360/n*(i+1)-90, fill=(color0[i]), outline=(color0[i]))
# draw.arc((25, 50, 175, 200), start=30, end=270, fill=(255, 255, 0))
# draw.chord((225, 50, 375, 200), start=30, end=270, fill=(255, 255, 0), outline=(0, 0, 0))


# draw.pieslice((25, 25, 175, 175), start=360/n*i-90, end=360/n*(i+1)-90, fill=(color[i]), outline=(color[i]))

## im.show()

conn_r, conn_w = multiprocessing.Pipe(duplex=False)

path = []
number = [0]
motion = [0]
move = None
dele = [False]

root = tk.Tk()
Pallet = Color_Pallet(master=root, path=path, number=number, motion=motion, move=move, dele=dele, connect_write=conn_w, connect_read=conn_r, image=[im])

# Pallet.set_bg(DEFAULT, path=None, image=im)

# motion = [0]
# move = None
# Chara.set_interupt_motion(Color_Pallet.DEFAULT, motion, move, "Left", repeat=False)

Pallet.set_button_event((0, 0, 0), Pallet.start_Left, ("Left", "Press"))
Pallet.set_button_event((0, 0, 0), Pallet.pickup_Left, ("Left", "Motion"))

def set_motion():
    pass

# Pallet.set_button_event((0, 0, 0), Pallet.pickup_Left, ("Default", "Motion"))

Pallet.loop()

data = {
    "name"  : "GetModual",
    "modual": "Center",
    "info"  : {
        "list" : [
            modual1,
            modual2
        ]
    }
}

data = {
    "name"  : "GetPosition",
    "modual": "Charactor",
    "info"  : {
        "position" : {
            window_x : x,
            window_y : y
        }
    }
}