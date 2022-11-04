import tkinter as tk
def hello() :
    win1=tk.Tk()
    win1.title("demo-win8")
    win1.geometry("1400x460")
    sche1 = tk.Label(win1,text="sample8",font=("Courier New",250))
    sche1.place(x=0,y=40)
    win1.mainloop()