import P_Ver

import tkinter
from PIL import Image, ImageTk 
import multiprocessing

DEFAULT = 0
class Charactor(tkinter.Frame):
    
    DEFAULT = 0
    def __init__(self,master, path, number, motion, move, dele, connect_write, connect_read, image=None):
        super().__init__(master)
        # self.pack()

        self.master = master

        self.time_event = {}
        self.button_event = {}
        self.img_li = {}
        self.motion_schedual = []
        self.motion_sche_len = 0
        self.interupt_mo_sche = {
            "Left" : [],
            "Wheel" : [],
            "Right" : []
        }
        self.interupt_mo_sche_len = {}
        self.modual = DEFAULT
        self.interupt_count = -1
        self.count = -1
        self.id = None
        self.event_occurence = "Default"
        self.is_repeat = True
        self.interupt_is_repeat = {}

        self.connect_write = connect_write
        self.connect_read = connect_read
        self.path = path
        self.number = number
        self.motion = motion
        self.move = move
        self.image = image

        self.width = 128
        self.height = 128
        self.pre_x = None
        self.pre_y = None
        self.x = None
        self.y = None
        self.root_x = None
        self.root_y = None
        
        self.set_image(DEFAULT, self.path, self.number, dele, self.image)
        self.set_bg(DEFAULT, path=None, image=None)
        self.set_motion(DEFAULT, self.motion, self.move, repeat=True)
        self.load_image(DEFAULT)
        self.set_canvas()
        self.set_master()
        self.set_time_event(self.call_back_func, name="end", handle=self.canvas, time=10000, count=1)
        self.set_time_event(self.frame, name="frame", handle=self.canvas, time=16, count=10000000)


    class Chara_Img():
        def __init__(self, path, num, dele=True, width=None, height=None, image=None):
            self.number = num
            self.path = path
            self.width = width
            self.height = height
            self.path = path
            self.delete = dele
            self.read_image = image

        def read(self):
            if not self.read_image:
                if self.path:
                    self.read_image = Image.open(self.path)
                else:
                    self.read_image = Image.new('RGB', (self.width, self.height), (0, 0, 0))
            self.image_resized = self.read_image.resize((self.width, self.height))
            self.im = ImageTk.PhotoImage(image=self.image_resized)
    
    class Chara_Time_Event():
        def __init__(self, handle, time, count, func, *args):
            self.func = func
            self.handle = handle
            self.time = time
            self.count = count
            self.args = P_Ver.P_Ver(args)
            self.exert()

        def exert(self):
            self.handle.after(self.time, self.func, *self.args)
            if self.count>1:
                self.count -=1
                self.handle.after(self.time, self.exert)
            elif self.count<0:
                self.handle.after(self.time, self.exert)
            return self

    class Chara_Button_Event():
        def __init__(self, color, func, *args):
            self.color = color
            self.func = func
            self.args = P_Ver.P_Ver(args)

    def set_time_event(self, func, name, handle, time, count, *args):
        if not handle:
            handle = self.master
        if not time:
            time = 16
        if not count:
            count = 1
        if not self.modual in self.time_event.keys():
            self.time_event[self.modual] = {}
        self.time_event[self.modual][name] = self.Chara_Time_Event(handle, time, count, func, *args)
        return self 

    def set_button_event(self, color, func, name, *args):
        if not self.modual in self.button_event.keys():
            self.button_event[self.modual] = {
                (i,j) : {} for i in ["Default", "Left", "Wheel", "Right"] for j in ["Press", "Motion", "Release", "Double"]
            }
        self.button_event[self.modual][name][color] = self.Chara_Button_Event(color, func, *args)
        return self 

    def set_image(self, modual, path, number, delete, image):
        if not modual in self.img_li.keys():
            self.img_li[modual] = {}
        if path:
            for li, path_li, dele in zip(number, path, delete):
                self.img_li[modual][li] = self.Chara_Img(path_li, li, dele=dele, width=self.width, height=self.height)
            return self
        else:
            if image:
                for li, path_li, dele in zip(number, path, delete):
                    self.img_li[modual][li] = self.Chara_Img(path_li, li, dele=dele, width=self.width, height=self.height)
                return self
            else:
                raise Exception("Error : cannot find image data")
            

    def set_motion(self, modual, motion, move, repeat=False):
        self.count = -1
        self.is_repeat = repeat
        if move:
            motion_len = len(motion)
            for move_x , move_y, times in move:
                self.motion_schedual += [(move_x, move_y, motion[i%motion_len]) for i in range(times)]
        else:
            self.motion_schedual = [(0, 0, mo) for mo in motion]
        self.motion_sche_len = len(self.motion_schedual)
        return self

    def set_interupt_motion(self, modual, motion, move, button, repeat=False):
        self.interupt_count = -1
        self.interupt_is_repeat[button] = repeat
        if move:
            motion_len = len(motion)
            self.interupt_mo_sche[button] = []
            for move_x , move_y, times in move:
                self.interupt_mo_sche[button] += [(move_x, move_y, motion[i%motion_len]) for i in range(times)]
        else:
            self.interupt_mo_sche[button] = motion
        self.interupt_mo_sche_len[button] = len(self.interupt_mo_sche[button])
        return self

    def load_image(self, modual):
        for im_li in self.img_li[modual].values():
            im_li.read()
        return self

    def set_bg(self, modual, path=None, image=None):
        self.img_li[modual][-1] = self.Chara_Img(path=path, num=-1, dele=dele, width=self.width, height=self.height, image=image)
        return self

    def set_master(self, bg="black", w=None, h=None, pos_x=100, pos_y=100):
        self.master.geometry(str(w if w else self.width)+"x"+str(h if h else self.height)+"+"+str(pos_x)+"+"+str(pos_y))
        self.master.overrideredirect(True)
        self.master.wm_attributes("-topmost", True) 
        self.master.wm_attributes("-transparentcolor", "black") 
        return self

    def set_canvas(self):
        self.canvas = tkinter.Canvas(root, bg="black", width=self.width, height=self.height, bd=0, highlightthickness=0)
        self.id = self.canvas.create_image(0, 0, image=self.img_li[DEFAULT][0].im, anchor='nw')
        self.canvas.pack()

        self.canvas.bind('<ButtonPress-1>',     lambda event: self.select_func(event, ("Left",   "Press"    )))
        self.canvas.bind('<B1-Motion>',         lambda event: self.select_func(event, ("Left",   "Motion"   )))
        self.canvas.bind('<ButtonRelease-1>',   lambda event: self.select_func(event, ("Left",   "Release"  )))
        self.canvas.bind('<Double-1>',          lambda event: self.select_func(event, ("Left",   "Double"   )))
        self.canvas.bind('<ButtonPress-2>',     lambda event: self.select_func(event, ("Wheel",  "Press"    )))
        self.canvas.bind('<B2-Motion>',         lambda event: self.select_func(event, ("Wheel",  "Motion"   )))
        self.canvas.bind('<ButtonRelease-2>',   lambda event: self.select_func(event, ("Wheel",  "Release"  )))
        self.canvas.bind('<Double-2>',          lambda event: self.select_func(event, ("Wheel",  "Double"   )))
        self.canvas.bind('<ButtonPress-3>',     lambda event: self.select_func(event, ("Right",  "Press"    )))
        self.canvas.bind('<B3-Motion>',         lambda event: self.select_func(event, ("Right",  "Motion"   )))
        self.canvas.bind('<ButtonRelease-3>',   lambda event: self.select_func(event, ("Right",  "Release"  )))
        self.canvas.bind('<Double-3>',          lambda event: self.select_func(event, ("Right",  "Double"   )))
        self.canvas.bind('<Motion>',            lambda event: self.select_func(event, ("Default","Motion"   )))
        return self

    def get_pixel(self, x, y):
        if -1 in self.img_li[self.modual].keys():
            if 0<x<self.width:
                if 0<y<self.height:
                    self.rgb = self.img_li[self.modual][-1].image_resized.getpixel((x, y))
                    return self.rgb[0], self.rgb[1], self.rgb[2]
            return None, None, None
        else:
            raise Exception("Error : cannot find background image")

    def select_func(self, event, name):
        if name[1]=="Press":
            self.interupt_count = -1
            self.event_occurence = name[0]
        if name[1]=="Release":
            self.count = -1
            self.event_occurence = "Default"
        
        self.x, self.y = event.x, event.y
        color = self.get_pixel(self.x, self.y)
        if self.modual in self.button_event:
            if color in self.button_event[self.modual][name].keys():
                eve = self.button_event[self.modual][name][color]
                eve.func(event, *eve.args)
    
    def start_Left(self, event):
        self.root_x, self.root_y = self.master.winfo_rootx(), self.master.winfo_rooty()
        self.pre_x, self.pre_y = event.x, event.y

    def pickup_Left(self, event):
        self.root_x, self.root_y = self.master.winfo_rootx(), self.master.winfo_rooty()
        self.x, self.y = event.x, event.y
        self.master.geometry(str(self.width)+"x"+str(self.height)+"+"+str(self.root_x+self.x-self.pre_x)+"+"+str(self.root_y+self.y-self.pre_y))

    def call_back_func(self):
        self.master.destroy()
        return 0

    def __del__(self):
        # 通信処理
        pass

    def loop(self):
        self.canvas.mainloop()

    def frame(self):
        if self.connect_read.poll():
            data= self.connect_read.recv()
            name = data["name"]
            modual = data["modual"]
            if name=="SetMotion":
                self.modual = modual
                info = data["info"]
                repeat = info["repeat"]
                motion = info["motion"]
                move = info["move"]

                self.set_motion(self.modual, motion, move, repeat=repeat)
            elif name=="SetPath":
                info = info["info"]
                path = info["path"]
                number = info["number"]
                delete = info["delete"]

                self.set_image(modual=modual, path=path, number=number, delete=delete, image=None)

        # print("\r"+self.event_occurence, end="")
        if self.event_occurence in ["Left", "Wheel", "Right"]:
            for button in ["Left", "Wheel", "Right"]:
                if self.interupt_mo_sche[button] and self.event_occurence==button:
                    if not(self.interupt_count>=self.interupt_mo_sche_len[button]-1 and self.interupt_is_repeat[button]==False):
                        previous_image = self.interupt_mo_sche[button][self.interupt_count%self.interupt_mo_sche_len[button]]
                        self.interupt_count += 1
                        current_image = self.interupt_mo_sche[button][self.interupt_count%self.interupt_mo_sche_len[button]]
                        if previous_image!=current_image:
                            self.canvas.delete(self.id)
                            self.id = self.canvas.create_image(0, 0, image=self.img_li[self.modual][current_image].im, anchor='nw')
        else:
            if not(self.count>=self.motion_sche_len-1 and self.is_repeat==False):
                previous_image = self.motion_schedual[self.count%self.motion_sche_len]
                self.count += 1
                current_image = self.motion_schedual[self.count%self.motion_sche_len]
                if previous_image[2]!=current_image[2]:
                    self.canvas.delete(self.id)
                    self.id = self.canvas.create_image(0, 0, image=self.img_li[self.modual][current_image[2]].im, anchor='nw')
                win_info = self.master.winfo_geometry()
                win_wh, win_x, win_y = win_info.split("+")
                set_win_geo = win_wh+"+"+str(int(win_x)+int(current_image[0]))+"+"+str(int(win_y)+int(current_image[1]))
                self.master.geometry(set_win_geo)

if __name__=="__main__":

    conn_r, conn_w = multiprocessing.Pipe(duplex=False)

    path = [
        "A1.png",
        "A2.png",
        "B1.png",
        "B2.png"
        ]
    number = [0, 1, 2, 3]
    motion = [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1]
    # move = [
        # (0, -1, 20),
        # (1, -2, 10)
    # ]
    move = None
    dele = [0, 0, 0, 0]

    root = tkinter.Tk()
    Chara = Charactor(master=root, path=path, number=number, motion=motion, move=move, dele=dele, connect_write=conn_w, connect_read=conn_r)

    motion = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
    move = None

    Chara.set_interupt_motion(DEFAULT, motion, move, "Left", repeat=False)

    Chara.set_button_event((0, 0, 0), Chara.start_Left, ("Left", "Press"))
    Chara.set_button_event((0, 0, 0), Chara.pickup_Left, ("Left", "Motion"))

    a = P_Ver.P_Ver(2.0)

    Chara.loop()


# data = {
#   "name"  : "SetMotion",
#   "modual": "modual1",
#   "info"  : {
#       "repeat"    : True,
#       "motion"    : [0, 0, 1, 1],
#       "move"      : [
#           (  0, -10,  1),
#           (100, -20, 10)
#       ]
#   }
# }
#
# data = {
#   "name"  : "SetInteruptMotion",
#   "modual": "modual1",
#   "info"  : {
#       "repeat"    : True,
#       "motion"    : [0, 0, 1, 1],
#       "move"      : [
#           (  0, -10,  1),
#           (100, -20, 10)
#       ]
#   }
# }
# 
# data = {
#   "name"  : "SetPath",
#   "modual": "modual1",
#   "info"  : {
#       delete  : [True, True]
#       number  : [0, 1]
#       path    : [
#           "soundonly_6.png",
#           "soundonly_5.png"
#       ]
#   }
# }  