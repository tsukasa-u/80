import tkinter as tk
def hello(conn_r, conn_w) :
    win1=tk.Tk()
    win1.title("demo-win4")
    win1.geometry("900x600")
    sche1 = tk.Label(win1,text="sample4",font=("Perpetua",210))
    sche1.place(x=20,y=150)
    win1.mainloop()