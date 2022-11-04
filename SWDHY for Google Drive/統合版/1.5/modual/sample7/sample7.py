import tkinter as tk
def hello(conn_r, conn_w) :
    win1=tk.Tk()
    win1.title("demo-win7")
    win1.geometry("1300x600")
    sche1 = tk.Label(win1,text="sample7",font=("Berlin Sans FB",265))
    sche1.place(x=40,y=80)
    win1.mainloop()