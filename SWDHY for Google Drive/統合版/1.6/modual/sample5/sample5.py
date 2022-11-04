import tkinter as tk
def hello(conn_r, conn_w) :
    win1=tk.Tk()
    win1.title("demo-win5")
    win1.geometry("1350x600")
    sche1 = tk.Label(win1,text="sample5",font=("High Tower Text",300))
    sche1.place(x=0,y=40)
    win1.mainloop()