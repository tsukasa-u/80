import multiprocessing
import module.Chara.system3 as system3
# import system3
import tkinter as tk
import os

class Templete_Chara(system3.Charactor):
    def start_Left(self, event):
        # self.root_x, self.root_y = self.master.winfo_rootx(), self.master.winfo_rooty()
        self.pre_x, self.pre_y = event.x, event.y
        self.connect_write.send([
            [   
                "SetWindow",
                "UNI",
                "SEND",
                "Pallet",
                "unvisuable",
                (None, None)
            ]
        ])

    def pickup_Left(self, event):
        self.root_x, self.root_y = self.master.winfo_rootx(), self.master.winfo_rooty()
        self.x, self.y = event.x, event.y
        self.master.geometry(str(self.width)+"x"+str(self.height)+"+"+str(self.root_x+self.x-self.pre_x)+"+"+str(self.root_y+self.y-self.pre_y))

    def stop_Left(self, event):
        self.connect_write.send([
            [   
                "SetWindow",
                "UNI",
                "SEND",
                "Pallet",
                "visuable",
                (self.root_x, self.root_y)
            ]
        ])

def hello(conn_r, conn_w):
    # conn_r, conn_w = multiprocessing.Pipe(duplex=False)

    PATH = os.path.dirname(__file__)

    path = [
        PATH+"/chara-cc1.png",
        PATH+"/chara-cc1.png",
        PATH+"/chara-cc2.png",
        PATH+"/chara-cc3.png",
        PATH+"/chara-cc4.png"
        ]
    number = [0, 1, 2, 3, 4]
    motion = [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1]
    move = None
    dele = [0, 0, 0, 0, 0]

    root = tk.Tk()
    Chara = Templete_Chara(master=root, path=path, number=number, motion=motion, move=move, dele=dele, connect_write=conn_w, connect_read=conn_r, width=192, height=256, root_x=300, root_y=200)


    motion = [2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4]

    move = None

    Chara.set_interupt_motion(Chara.DEFAULT, motion, move, "Left", repeat=True)

    Chara.set_button_event((0, 0, 0), Chara.start_Left, ("Left", "Press"))
    Chara.set_button_event((0, 0, 0), Chara.pickup_Left, ("Left", "Motion"))
    Chara.set_button_event((0, 0, 0), Chara.stop_Left, ("Left", "Release"))

    Chara.loop()