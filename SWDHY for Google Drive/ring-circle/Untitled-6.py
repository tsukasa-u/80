import tkinter
from PIL import Image, ImageTk  

class Charactor(tkinter.Frame):
    def __init__(self,master, path):
        super().__init__(master)
        # self.pack()

        self.master = master

        self.width = 300
        self.height = 300
        self.pre_x = None
        self.pre_y = None
        self.x = None
        self.y = None
        self.root_x = None
        self.root_y = None
        
        self.set_image(path)
        self.set_label()
        self.set_master()
        self.set_time_event(self.label, 30000, 1, self.call_back_func)
        self.set_time_event(self.label, 16, 1, self.next_frame, 0)


    class Chara_Img():
        def __init__(self, path, num):
            self.number = num
            self.path = path
            self.read_image = Image.open(path)
            self.im = ImageTk.PhotoImage(image=self.read_image)
            self.image_width = self.read_image.size[0]
            self.image_height = self.read_image.size[1]
    
    class Chara_Event():
        def __init__(self, handle, time, count, func, *args, **kargs):
            self.value = []
            self.func = func
            self.handle = handle

        class p_ver():
            def __init__(self, ver):
                self.ver = [ver]

            def __repr__(self):
                return self.ver[0]

        def new_ver(self, value=None):
            self.value.append(self.p_ver(value))
            return self.value[-1]
        
        def __repr__(self):
            return "test"

    def set_time_event(self, handle, time, count, func, *args, **kargs):
        if not handle:
            handle = self.master
        
        handle.after(time, func, *args, **kargs)
        if count>1:
            handle.after(time, self.set_time_event, handle, time, count-1, func, *args, **kargs)
        return self 

    def set_image(self, path):
        self.img_li = []
        for li, path_li in enumerate(path):
            self.img_li.append(self.Chara_Img(path_li, li))
        return self

    def set_master(self, bg="black", w=None, h=None, pos_x=100, pos_y=100):
        self.master.geometry(str(w if w else self.width)+"x"+str(h if h else self.height)+"+"+str(pos_x)+"+"+str(pos_y))
        self.master.overrideredirect(True)
        self.master.wm_attributes("-topmost", True) 
        self.master.wm_attributes("-transparentcolor", "black") 
        return self

    def set_label(self):
        self.label = tkinter.Label(root, image=self.img_li[0].im, bg="black", width=64, height=64)
        self.label.pack()

        self.label.bind('<ButtonPress-1>', self.start_pickup)
        self.label.bind('<B1-Motion>', self.pickup_position)
        self.label.bind('<ButtonRelease-1>', self.stop_pickup)
        return self

    def get_pixel(self, x, y):
        if 0<x<self.img_li[0].read_image.size[0]:
            if 0<y<self.img_li[0].read_image.size[1]:
                self.rgb = self.img_li[0].read_image.getpixel((x, y))
                if self.rgb[0]+self.rgb[1]+self.rgb[2]>0:
                    return True
        return False
    
    def chatch_chara(self):
        pass
        return self
    
    def start_pickup(self, event):
        self.root_x, self.root_y = self.master.winfo_rootx(), self.master.winfo_rooty()
        self.pre_x, self.pre_y = event.x, event.y

    def pickup_position(self, event):
        self.root_x, self.root_y = self.master.winfo_rootx(), self.master.winfo_rooty()
        self.x, self.y = event.x, event.y
        # print(self.get_pixel(self.x, self.y))
        self.master.geometry(str(self.width)+"x"+str(self.height)+"+"+str(self.root_x+self.x-self.pre_x)+"+"+str(self.root_y+self.y-self.pre_y))
        # self.pre_x, self.pre_y = self.x, self.y
        print(self.root_x, self.root_y)

    def stop_pickup(self, event):
        # self.root_x, self.root_y = self.master.winfo_rootx, self.master.winfo_rooty
        # self.x, self.y = event.x, event.y
        pass

    def call_back_func(self):
        self.master.destroy()
        return 0

    def next_frame(self, i):
        # self.master.geometry("300x300+"+str(i)+"+0")
        self.master.after(16, self.next_frame, i+1)

    def __del__(self):
        pass

if __name__=="__main__":
    root = tkinter.Tk()
    Chara = Charactor(master=root, path=('あるとりあ.png',))
    print(Charactor)
    Chara.label.mainloop()