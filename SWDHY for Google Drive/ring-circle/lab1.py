#from tkinter import *
import tkinter as tk

class CustomButton(tk.Canvas):
       def __init__(self, parent, width, height, color, command=None):
           tk.Canvas.__init__(self, parent, borderwidth=1, 
               relief="raised", highlightthickness=0)
           self.command = command

           padding = 4
           __id = self.create_oval((padding,padding,
               width+padding, height+padding), outline=color, fill=color)
           (x0,y0,x1,y1)  = self.bbox("all")
           width = (x1-x0) + padding
           height = (y1-y0) + padding
           self.configure(width=width, height=height)
           self.bind("<ButtonPress-1>", self._on_press)
           self.bind("<ButtonRelease-1>", self._on_release)
           self.loadimage = tk.PhotoImage(file="日章旗.png")
           self.roundedbutton = tk.Button(self, image=self.loadimage)
           self.roundedbutton["bg"] = "white"
           self.roundedbutton["border"] = "0"
           self.roundedbutton.pack(side="top")

       def _on_press(self, event):
           self.configure(relief="sunken")

       def _on_release(self, event):
           self.configure(relief="raised")
           if self.command is not None:
               self.command()
#app = CustomButton()
app = tk.Tk()
button = CustomButton(app, 100, 25, 'red')
button.pack()
app.mainloop()
app.mainloop()