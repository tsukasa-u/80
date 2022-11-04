import tkinter as tk
def hello() :
    win1=tk.Tk()
    win1.title("demo-win1")
    win1.geometry("700x600")
    sche1 = tk.Label(win1,text="sample1",font=("Lucida Grande",100))
    sche1.place(x=80,y=200)
    win1.mainloop()