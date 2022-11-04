# import P_Ver
import modual.Chara.P_Ver as P_Ver

import tkinter
from PIL import Image, ImageTk 
import multiprocessing
import copy

DEFAULT = 10
class Charactor(tkinter.Frame):
    def __init__(self,master, path, number, motion, move, dele, connect_write, connect_read, image=None, width=128, height=128, root_x=0, root_y=0, centerpoint=None):
        super().__init__(master)
        # self.pack()

        self.master = master
    
        self.DEFAULT = 0

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
        self.modual = self.DEFAULT
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

        self.width = width
        self.height = height
        self.pre_x = None
        self.pre_y = None
        self.x = None
        self.y = None
        self.root_x = root_x
        self.root_y = root_y

        self.set_image(self.DEFAULT, self.path, self.number, dele, self.image, centerpoint=centerpoint)
        self.set_bg(self.DEFAULT, path=None, image=None)
        self.set_motion(self.DEFAULT, self.motion, self.move, repeat=True)
        self.load_image(self.DEFAULT)
        self.set_canvas()
        self.set_master(pos_x=self.root_x, pos_y=self.root_y)
        self.set_time_event(self.call_back_func, name="end", handle=self.canvas, time=10000, count=1)
        self.set_time_event(self.frame, name="frame", handle=self.canvas, time=16, count=10000000)


    class Chara_Img():
        def __init__(self, path, num, dele=True, width=None, height=None, image=None, centerpoint=None):
            self.number = num
            self.path = path
            self.width = width
            self.height = height
            self.delete = dele
            self.read_image = image
            self.image_resized = None
            self.im = None
            self.centerpoint=centerpoint

        def read(self):
            if not self.read_image:
                if self.path:
                    self.read_image = Image.open(self.path)
                    self.image_resized = self.read_image.resize((self.width, self.height))
                else:
                    self.read_image = Image.new('RGB', (self.width, self.height), (0, 0, 0))
                    self.image_resized = self.read_image
                self.im = ImageTk.PhotoImage(image=self.image_resized)
            else:
                self.image_resized = self.read_image.resize((self.width, self.height))
                self.im = ImageTk.PhotoImage(image=self.image_resized)
            # print("&&&", self.im)
    
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
                (i,j) : {} for i in ["Default", "Left", "Wheel", "Right"] for j in ["Press", "Motion", "Release", "Double", "Enter", "Leave"]
            }
        self.button_event[self.modual][name][color] = self.Chara_Button_Event(color, func, *args)
        return self 

    def set_image(self, modual, path, number, delete, image, centerpoint=None):
        if not modual in self.img_li.keys():
            self.img_li[modual] = {}
        if path:
            if centerpoint:
                for li, path_li, dele, point in zip(number, path, delete, centerpoint):
                    self.img_li[modual][li] = self.Chara_Img(path_li, li, dele=dele, width=self.width, height=self.height, centerpoint=point)
                return self
            else:
                for li, path_li, dele in zip(number, path, delete):
                    self.img_li[modual][li] = self.Chara_Img(path_li, li, dele=dele, width=self.width, height=self.height, centerpoint=None)
                return self
        else:
            if image:
                if centerpoint:
                    for li, image_li, dele, point in zip(number, image, delete, centerpoint):
                        self.img_li[modual][li] = self.Chara_Img(None, li, dele=dele, width=self.width, height=self.height, image=image_li, centerpoint=point)
                    return self
                else:
                    for li, image_li, dele in zip(number, image, delete):
                        self.img_li[modual][li] = self.Chara_Img(None, li, dele=dele, width=self.width, height=self.height, image=image_li)
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

    def load_image(self, modual, num=None):
        if num==None:
            for im_li in self.img_li[modual].values():
                im_li.read()
        else:
            self.img_li[modual][num].read()
        return self

    def set_bg(self, modual, path=None, image=None, num=None):
        # if self.img_li[modual][-1]:
        #     del self.img_li[modual][-1]
        if num==None:
            self.img_li[modual][-1] = self.Chara_Img(path=path, num=-1, dele=True, width=self.width, height=self.height, image=image)
        else:
            self.img_li[modual][-1] = copy.copy(self.img_li[modual][num])
        return self

    def set_master(self, bg="black", w=None, h=None, pos_x=100, pos_y=100):
        self.master.geometry(str(w if w else self.width)+"x"+str(h if h else self.height)+"+"+str(pos_x)+"+"+str(pos_y))
        self.master.overrideredirect(True)
        self.master.wm_attributes("-topmost", True) 
        self.master.wm_attributes("-transparentcolor", "black") 
        return self

    def set_canvas(self):
        self.canvas = tkinter.Canvas(self.master, bg="black", width=self.width, height=self.height, bd=0, highlightthickness=0)
        self.id = self.canvas.create_image(0, 0, image=self.img_li[self.DEFAULT][0].im, anchor='nw')
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
        self.canvas.bind('<Enter>',            lambda event: self.select_func(event, ("Default","Enter"   )))
        self.canvas.bind('<Leave>',            lambda event: self.select_func(event, ("Default","Leave"   )))
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
        
        if name[1]=="Enter" or name[1]=="Leave":
            if self.modual in self.button_event:
                if None in self.button_event[self.modual][name].keys():
                    eve = self.button_event[self.modual][name][None]
                    eve.func(event, *eve.args)
        else:
            self.x, self.y = event.x, event.y
            color = self.get_pixel(self.x, self.y)
            if self.modual in self.button_event:
                if color in self.button_event[self.modual][name].keys():
                    eve = self.button_event[self.modual][name][color]
                    eve.func(event, *eve.args)
    
    def start_Left(self, event):
        # self.root_x, self.root_y = self.master.winfo_rootx(), self.master.winfo_rooty()
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

    def get_info(self):
        if self.connect_read.poll():
            conn_data= self.connect_read.recv()
            task_name, main_method, sub_method, modual, *conn_info = conn_data
            if task_name=="SetMotion":
                self.modual = modual    #   果たしてselfでよいのか
                repeat, motion, move = conn_info

                self.set_motion(self.modual, motion, move, repeat=repeat)
            elif task_name=="SetInteruptMotion":
                self.modual = modual    #   果たしてselfでよいのか
                ope, repeat, motion, move = conn_info

                self.set_interupt_motion(self.modual, motion, move, ope, repeat=repeat)
            elif task_name=="SetPath":
                path, number, delete = conn_info

                self.set_image(modual=modual, path=path, number=number, delete=delete, image=None)
        
        # self.connect_write.send([
        #     "GetPosition",
        #     "UNI",
        #     "SEND",
        #     "Pallet",
        #     (self.root_x, self.root_y)
        # ])

    def frame(self):

        self.get_info()
        self.master.lift()

        if self.event_occurence in ["Left", "Wheel", "Right"]:
            for button in ["Left", "Wheel", "Right"]:
                if self.interupt_mo_sche[button] and self.event_occurence==button:
                    if not(self.interupt_count>=self.interupt_mo_sche_len[button]-1 and self.interupt_is_repeat[button]==False):
                        previous_image = self.interupt_mo_sche[button][self.interupt_count%self.interupt_mo_sche_len[button]]
                        self.interupt_count += 1
                        current_image = self.interupt_mo_sche[button][self.interupt_count%self.interupt_mo_sche_len[button]]
                        if previous_image!=current_image or self.interupt_mo_sche_len==1:
                            self.canvas.delete(self.id)
                            self.id = self.canvas.create_image(0, 0, image=self.img_li[self.modual][current_image].im, anchor='nw')
                        if self.img_li[self.modual][current_image].centerpoint:
                            center_x, center_y = self.img_li[self.modual][current_image].centerpoint
                            self.master.geometry(str(self.width)+"x"+str(self.height)+"+"+str(self.root_x+self.x-center_x)+"+"+str(self.root_y+self.y-center_y))
        else:
            if not(self.count>=self.motion_sche_len-1 and self.is_repeat==False):
                previous_image = self.motion_schedual[self.count%self.motion_sche_len]
                self.count += 1
                current_image = self.motion_schedual[self.count%self.motion_sche_len]
                if previous_image[2]!=current_image[2] or self.motion_sche_len==1:
                    self.canvas.delete(self.id)
                    # print("\r"+str(self.img_li[self.modual]), end="")
                    self.id = self.canvas.create_image(0, 0, image=self.img_li[self.modual][current_image[2]].im, anchor='nw')
                win_info = self.master.winfo_geometry()
                win_wh, win_x, win_y = win_info.split("+")
                set_win_geo = win_wh+"+"+str(int(win_x)+int(current_image[0]))+"+"+str(int(win_y)+int(current_image[1]))
                self.master.geometry(set_win_geo)

    def convert_data(self, conn_data, data):
        task_name, main_method, sub_method, modual, *conn_info = data
        for i, conn_data_i in enumerate(conn_data):
            sub_task_name, sub_main_method, sub_sub_method, sub_modual, *sub_conn_info = conn_data_i
            if task_name==sub_task_name and main_method==sub_main_method and sub_method==sub_sub_method and modual==sub_modual:
                del conn_data[i]
        conn_data.append(data)

# data = {
#   "mainmethod": "UNI",  #"BROAD",
#   "submethod" : "SEND", #"RECEIVE"
#   "name"      : "SetMotion",
#   "modual"    : "modual1",
#   "info"      : {
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
#   "mainmethod": "UNI",  #"BROAD",
#   "submethod" : "SEND", #"RECEIVE"
#   "name"  : "SetInteruptMotion",
#   "modual": "modual1",
#   "info"  : {
#       "ope"       : ("Left", "Double")
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
#   "mainmethod": "UNI",  #"BROAD",
#   "submethod" : "SEND", #"RECEIVE"
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