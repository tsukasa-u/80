import tkinter as tk
def hello() :
    win1=tk.Tk()
    win1.title("demo-win2")
    win1.geometry("1000x700")
    sche1 = tk.Label(win1,text="sample2",font=("MS Gosic",220))
    sche1.place(x=0,y=120)
    win1.mainloop()