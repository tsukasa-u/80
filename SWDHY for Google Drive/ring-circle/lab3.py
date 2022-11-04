import tkinter as tk

zahyo=[]

def pos(event):
    cvs.delete("line")
    if len(zahyo)>0:
        cvs.create_line(zahyo[-2], zahyo[-1], event.x, event.y ,tag="line")

def click(event):
    zahyo.append(event.x)
    zahyo.append(event.y)
    if len(zahyo)==2:
        cvs.create_oval(event.x-5, event.y-5, event.x+5, event.y+5,fill='green',tag="start")

    if len(zahyo)>2:
        cvs.create_oval(event.x-5, event.y-5, event.x+5, event.y+5,fill='RED')
        cvs.create_line(zahyo[-4], zahyo[-3], event.x, event.y)


window = tk.Tk()
window.title('サンプル')

cvs = tk.Canvas(window, height=600, width=1000, bg='white',bd=1,relief="ridge")
cvs.grid(row=0, column=0)
cvs.bind('<Motion>', pos)
cvs.bind('<Button-1>', click)

window.mainloop()