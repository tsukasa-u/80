import tkinter as tk
def hello(conn_r, conn_w) :
    win1=tk.Tk()
    win1.title("demo-win6")
    win1.geometry("1100x600")
    sche1 = tk.Label(win1,text="sample6",font=("Impact",200))
    sche1.place(x=80,y=100)
    win1.mainloop()