import tkinter as tk
def hello() :
    win1=tk.Tk()
    win1.title("demo-win3")
    win1.geometry("1000x300")
    sche1 = tk.Label(win1,text="sample3",font=("游明朝",150))
    sche1.place(x=150,y=0)
    win1.mainloop()