#各種インポート
import calendar,datetime
import tkinter as tk
from tkinter import messagebox,ttk


dt_now = datetime.datetime.now()
t1=dt_now.year
tm=dt_now.month
s = calendar.month(t1,tm)
month_range = calendar.monthrange(t1, tm)
top1 = tk.Tk()
top1.title("カレンダー")
top1.geometry("800x400")
label1 = tk.Label(top1, text=t1,fg="Blue",font=("Lucida Grande",20))
label1.place(x=145,y=0)
label2 = tk.Label(top1, text=str(tm)+"月",fg="Blue",font=("Lucida Grande",15))
label2.place(x=160,y=30)

frame1 = tk.Frame(top1)
frame1.place(x=400,y=0,height=400,width=400)
textt = tk.Listbox(frame1,height=20,width=60)
textt.place(x=0,y=0)
#スクロールバーの作成
xscrollt = tk.Scrollbar(frame1, orient=tk.HORIZONTAL, command=textt.xview)
xscrollt.place(x=0, y=325, width=370)
yscrollt = tk.Scrollbar(frame1, orient=tk.VERTICAL,command=textt.yview)
yscrollt.place(x=365,y=0,height=330)
#動きをスクロールバーに反映
textt["xscrollcommand"] = xscrollt.set
textt["yscrollcommand"] = yscrollt.set

for line in open("todo.dat",encoding="utf-8_sig"):
    a = eval(line[:-1])
    for n in range(1, month_range[1]+1):        
        if t1 in a[0].keys():
            if tm in a[0][t1].keys():
                if n in a[0][t1][tm].keys():
                    textt.insert(tk.END,str(t1)+"."+str(tm)+"."+str(n)+"."+str(a[0][t1][tm][n]["title"]))
dc = s[-2]
for i in range(180):
    yd = i+2020
    for md in range(13):
        for dd in range(32):
            dict1={yd:{md:{dd:{}}}}
from collections import defaultdict
comp_list = defaultdict(lambda: defaultdict(lambda : defaultdict(lambda: defaultdict(lambda : None))))

date = {0:"月",1:"火",2:"水",3:"木",4:"金",5:"土",6:"日"}
def callback(event):
    pass
    
youbi = []
for n in range(0,7):
    youbi.append(tk.Button(top1,text = date[n],height = 0,width = 5))
    youbi[-1].bind("<1>",callback)
    youbi[-1].place(x=45*(n+1/3),y=60)
pmr = calendar.monthrange(t1-(13-tm)//12,tm-1+12*((13-tm)//12))    
nmr = calendar.monthrange(t1+tm//12,tm+1-12*(tm//12))
days = []
def callback2(event):
    evd = event.widget["text"]
    yy,mm,dd=t1,tm,evd
    if not comp_list[yy][mm][dd]:
        win1 = tk.Tk()
        win1.title("スケジュール")
        win1.geometry("700x600")
        sche1 = tk.Label(win1,text=str(tm)+"月"+str(evd)+"日のスケジュール",font=("Lucida Grande",20))
        sche1.place(x=0,y=0)
        sche4 = tk.Label(win1,text="新しい予定の記入",font=("Lucida Grande",20))
        sche4.place(x=20,y=80)
        sche3 = tk.Label(win1,text= "タイトル",font=("Lucida Grande",20))
        sche3.place(x=460,y=0)
        sche2 = tk.Entry(win1,width=50)
        sche2.place(x=360,y=50)
        sche6 = tk.Label(win1,text="内容",font=("Lucida Grande",20))
        sche6.place(x=400,y=80)
        sche7 = tk.Label(win1,text="設定済みのスケジュール",font=("Lucida Grande",20))
        sche7.place(x=20,y=180)
        sche5 = tk.Text(win1,font=("Lucida Grande",15),height=20,width=30)
        sche5.place(x=360,y=120)
        lbst = []
        def LBSC(evt):
            def delsc_click():
                for i in sche8.curselection():
                    with open("todo.dat", encoding="utf-8_sig") as f:
                        todot = f.read()
                    todot = todot.replace('"','')
                    lbstk=str({t1:{tm:{evd:lbst[int(i)]}}})
                    lbstt = str(lbstk.replace('"',''))
                    lbsta = lbstt.replace('\\\\','\\')
                    lbstb=(str(lbsta)+","+"\n")
                    todot = todot.replace(lbstb, "")
                    with open("todo.dat", mode="w", encoding="utf-8_sig") as f:
                        f.write(todot)
                sche8.delete(0,tk.END)
                textt.delete(0,tk.END)
                for line in open("todo.dat",encoding="utf-8_sig"):
                    a = eval(line[:-1])
                    if t1 in a[0].keys():
                        if tm in a[0][t1].keys(): 
                            if evd in a[0][t1][tm].keys():
                                sche8.insert(tk.END,str(a[0][t1][tm][evd]))
                    for n in range(1, month_range[1]+1):        
                        if t1 in a[0].keys():
                            if tm in a[0][t1].keys():
                                if n in a[0][t1][tm].keys():
                                    textt.insert(tk.END,str(t1)+"."+str(tm)+"."+str(n)+"."+str(a[0][t1][tm][n]["title"]))
            delscButton = tk.Button(win1,text="削除",command=delsc_click)
            delscButton.place(x=50,y=510)

        frame2 = tk.Frame(win1)
        frame2.place(x=20,y=240,height=260,width=310)
        sche8 = tk.Listbox(frame2,height=15,width=42)
        sche8.bind("<<ListboxSelect>>",LBSC)
        sche8.place(x=0,y=0)
        xscrolls8 = tk.Scrollbar(frame2, orient=tk.HORIZONTAL, command=sche8.xview)
        xscrolls8.place(x=0, y=240, width=260)
        yscrolls8 = tk.Scrollbar(frame2, orient=tk.VERTICAL,command=sche8.yview)
        yscrolls8.place(x=260,y=0,height=240)
        sche8["xscrollcommand"] = xscrolls8.set
        sche8["yscrollcommand"] = yscrolls8.set
        global LBSN
        LBSN = 0
        for line in open("todo.dat",encoding="utf-8_sig"):
            a = eval(line[:-1])
            if t1 in a[0].keys():
                if tm in a[0][t1].keys(): 
                    if evd in a[0][t1][tm].keys():
                        sche8.insert(tk.END,str(a[0][t1][tm][evd]))
                        lbst.insert(LBSN,str(a[0][t1][tm][evd]))
                        LBSN=LBSN+1

        def nsc_click():
            def ok1_click():
                s = sche2.get()
                sced=sche5.get(1.0,tk.END)
                with open('todo.dat', 'a',newline="\n",encoding="utf-8_sig") as f:
                    f.write(str({t1:{tm:{evd:{"title":s,"text":sced,}}}})+","+"\n")
                textt.delete(0, tk.END)
                sche8.delete(0,tk.END)
                for line in open("todo.dat",encoding="utf-8_sig"):
                    a = eval(line[:-1])
                    if t1 in a[0].keys():
                        if tm in a[0][t1].keys(): 
                            if evd in a[0][t1][tm].keys():
                                sche8.insert(tk.END,str(t1)+"."+str(tm)+"."+str(evd)+"."+str(a[0][t1][tm][evd]))
                                    
                for line in open("todo.dat",encoding="utf-8_sig"):   
                    a = eval(line[:-1])
                    for n in range(1, month_range[1]+1):     
                        if t1 in a[0].keys():
                            if tm in a[0][t1].keys(): 
                                if n in a[0][t1][tm].keys():
                                    textt.insert(tk.END,str(t1)+"."+str(tm)+"."+str(n)+"."+str(a[0][t1][tm][n]['title']))
            ok1Button = tk.Button(win1, text='OK', command=ok1_click,font=("Lucida Grande",12))
            ok1Button.place(x= 500,y=560)
        nscButton = tk.Button(win1,text='作成',command=nsc_click)
        nscButton.place(x=130,y=130)
def callback3(event):
    evd = event.widget["text"]
    py=t1-(13-tm)//12
    pm=tm-1+12*((13-tm)//12)
    yy,mm,dd=py,pm,evd
    if not comp_list[yy][mm][dd]:
        win1 = tk.Tk()
        win1.title("スケジュール")
        win1.geometry("800x600")
        sche1 = tk.Label(win1,text=str(pm)+"月"+str(evd)+"日のスケジュール",font=("Lucida Grande",20))
        sche1.place(x=0,y=0)
        sche4 = tk.Label(win1,text="新しい予定の記入",font=("Lucida Grande",20))
        sche4.place(x=20,y=80)
        sche3 = tk.Label(win1,text= "タイトル",font=("Lucida Grande",20))
        sche3.place(x=460,y=0)
        sche2 = tk.Entry(win1,width=50)
        sche2.place(x=360,y=50)
        sche6 = tk.Label(win1,text="内容",font=("Lucida Grande",20))
        sche6.place(x=400,y=80)
        sche7 = tk.Label(win1,text="設定済みのスケジュール",font=("Lucida Grande",20))
        sche7.place(x=20,y=180)
        sche5 = tk.Text(win1,font=("Lucida Grande",15),height=20,width=30)
        sche5.place(x=360,y=120)
        lbstp = []
        def LBSC(evt):
            def delsc_click():
                for i in sche8.curselection():
                    with open("todo.dat", encoding="utf-8_sig") as f:
                        todot = f.read()
                    todot = todot.replace('"','')
                    lbstk=str({py:{pm:{evd:lbstp[int(i)]}}})
                    lbstt = str(lbstk.replace('"',''))
                    lbsta = lbstt.replace('\\\\','\\')
                    lbstb=(str(lbsta)+","+"\n")
                    todot = todot.replace(lbstb, "")
                    with open("todo.dat", mode="w", encoding="utf-8_sig") as f:
                        f.write(todot)
                sche8.delete(0,tk.END)
                for line in open("todo.dat",encoding="utf-8_sig"):
                    a = eval(line[:-1])
                    if py in a[0].keys():
                        if pm in a[0][py].keys(): 
                            if evd in a[0][py][pm].keys():
                                sche8.insert(tk.END,str(a[0][py][pm][evd]))
            delscButton = tk.Button(win1,text="削除",command=delsc_click)
            delscButton.place(x=50,y=510)

        frame2 = tk.Frame(win1)
        frame2.place(x=20,y=240,height=260,width=310)
        sche8 = tk.Listbox(frame2,height=15,width=42)
        sche8.bind("<<ListboxSelect>>",LBSC)
        sche8.place(x=0,y=0)
        xscrolls8 = tk.Scrollbar(frame2, orient=tk.HORIZONTAL, command=sche8.xview)
        xscrolls8.place(x=0, y=240, width=260)
        yscrolls8 = tk.Scrollbar(frame2, orient=tk.VERTICAL,command=sche8.yview)
        yscrolls8.place(x=260,y=0,height=240)
        sche8["xscrollcommand"] = xscrolls8.set
        sche8["yscrollcommand"] = yscrolls8.set
        global LBSNp
        LBSNp = 0
        for line in open("todo.dat",encoding="utf-8_sig"):
            a = eval(line[:-1])
            if py in a[0].keys():
                if pm in a[0][py].keys(): 
                    if evd in a[0][py][pm].keys():
                        sche8.insert(tk.END,str(a[0][py][pm][evd]))
                        lbstp.insert(LBSNp,str(a[0][py][pm][evd]))
                        LBSNp=LBSNp+1
        def nsc_click():
            def ok1_click():
                s = sche2.get()
                sced=sche5.get(1.0,tk.END)
                with open('todo.dat', 'a',newline="\n",encoding="utf-8_sig") as f:
                    f.write(str({py:{pm:{evd:{"title":s,"text":sced}}}})+","+"\n")
                    # textt.delete(0, tk.END)
                    sche8.delete(0,tk.END)
                for line in open("todo.dat",encoding="utf-8_sig"):
                    a = eval(line[:-1])
                    if py in a[0].keys():
                        if pm in a[0][py].keys(): 
                            if evd in a[0][py][pm].keys():
                                sche8.insert(tk.END,str(py)+"."+str(pm)+"."+str(evd)+"."+str(a[0][py][pm][evd]))
                                    
            ok1Button = tk.Button(win1, text='OK', command=ok1_click,font=("Lucida Grande",12))
            ok1Button.place(x= 500,y=560)
        nscButton = tk.Button(win1,text='作成',command=nsc_click)
        nscButton.place(x=130,y=130)
    else:
        messagebox.showerror("注意", "書き込み可能領域が定義できません")
def callback4(event):
    evd = event.widget["text"]
    ny=t1+tm//12
    nm=tm+1-12*(tm//12)
    yy,mm,dd=ny,nm,evd
    if not comp_list[yy][mm][dd]:
        win1 = tk.Tk()
        win1.title("スケジュール")
        win1.geometry("800x600")
        sche1 = tk.Label(win1,text=str(nm)+"月"+str(evd)+"日のスケジュール",font=("Lucida Grande",20))
        sche1.place(x=0,y=0)
        sche4 = tk.Label(win1,text="新しい予定の記入",font=("Lucida Grande",20))
        sche4.place(x=20,y=80)
        sche3 = tk.Label(win1,text= "タイトル",font=("Lucida Grande",20))
        sche3.place(x=460,y=0)
        sche2 = tk.Entry(win1,width=50)
        sche2.place(x=360,y=50)
        sche6 = tk.Label(win1,text="内容",font=("Lucida Grande",20))
        sche6.place(x=400,y=80)
        sche7 = tk.Label(win1,text="設定済みのスケジュール",font=("Lucida Grande",20))
        sche7.place(x=20,y=180)
        sche5 = tk.Text(win1,font=("Lucida Grande",15),height=20,width=30)
        sche5.place(x=360,y=120)
        lbstq = []
        def LBSC(evt):
            def delsc_click():
                for i in sche8.curselection():
                    with open("todo.dat", encoding="utf-8_sig") as f:
                        todot = f.read()
                    todot = todot.replace('"','')
                    lbstk=str({ny:{nm:{evd:lbstq[int(i)]}}})
                    lbstt = str(lbstk.replace('"',''))
                    lbsta = lbstt.replace('\\\\','\\')
                    lbstb=(str(lbsta)+","+"\n")
                    todot = todot.replace(lbstb, "")
                    with open("todo.dat", mode="w", encoding="utf-8_sig") as f:
                        f.write(todot)
                sche8.delete(0,tk.END)
                for line in open("todo.dat",encoding="utf-8_sig"):
                    a = eval(line[:-1])
                    if ny in a[0].keys():
                        if nm in a[0][ny].keys(): 
                            if evd in a[0][ny][nm].keys():
                                sche8.insert(tk.END,str(a[0][ny][nm][evd]))
            delscButton = tk.Button(win1,text="削除",command=delsc_click)
            delscButton.place(x=50,y=510)

        frame2 = tk.Frame(win1)
        frame2.place(x=20,y=240,height=260,width=310)
        sche8 = tk.Listbox(frame2,height=15,width=42)
        sche8.bind("<<ListboxSelect>>",LBSC)
        sche8.place(x=0,y=0)
        xscrolls8 = tk.Scrollbar(frame2, orient=tk.HORIZONTAL, command=sche8.xview)
        xscrolls8.place(x=0, y=240, width=260)
        yscrolls8 = tk.Scrollbar(frame2, orient=tk.VERTICAL,command=sche8.yview)
        yscrolls8.place(x=260,y=0,height=240)
        sche8["xscrollcommand"] = xscrolls8.set
        sche8["yscrollcommand"] = yscrolls8.set
        global LBSNq
        LBSNq = 0
        for line in open("todo.dat",encoding="utf-8_sig"):
            a = eval(line[:-1])
            if ny in a[0].keys():
                if nm in a[0][ny].keys(): 
                    if evd in a[0][ny][nm].keys():
                        sche8.insert(tk.END,str(a[0][ny][nm][evd]))
                        lbstq.insert(LBSNq,str(a[0][ny][nm][evd]))
                        LBSNq=LBSNq+1
        def nsc_click():
            def ok1_click():
                s = sche2.get()
                sced=sche5.get(1.0,tk.END)
                with open('todo.dat', 'a',newline="\n",encoding="utf-8_sig") as f:
                    f.write(str({ny:{nm:{evd:{"title":s,"text":sced}}}})+","+"\n")
                    # textt.delete(0, tk.END)
                    sche8.delete(0,tk.END)
                for line in open("todo.dat",encoding="utf-8_sig"):
                    a = eval(line[:-1])
                    if ny in a[0].keys():
                        if nm in a[0][ny].keys(): 
                            if evd in a[0][ny][nm].keys():
                                sche8.insert(tk.END,str(ny)+"."+str(nm)+"."+str(evd)+"."+str(a[0][ny][nm][evd]))
                                    
                # for line in open("todo.dat",encoding="utf-8_sig"):   
                #     a = eval(line[:-1])
                #     for n in range(1, month_range[1]+1):     
                #         if ny in a[0].keys():
                #             if nm in a[0][ny].keys(): 
                #                 if n in a[0][ny][nm].keys():
                #                     textt.insert(tk.END,str(ny)+"."+str(nm)+"."+str(n)+"."+str(a[0][ny][nm][n]['title']))
            ok1Button = tk.Button(win1, text='OK', command=ok1_click,font=("Lucida Grande",12))
            ok1Button.place(x= 500,y=560)
        nscButton = tk.Button(win1,text='作成',command=nsc_click)
        nscButton.place(x=130,y=130)
    else:
        # print("データが不在")
        messagebox.showerror("注意", "書き込み可能領域が定義できません")

for n in range(1, month_range[1]+1):
    days.append(tk.Button(top1,text=n,height = 2,width=5))
    days[-1].bind("<1>",callback2)
    days[-1].place(x=45*((month_range[0]+n-1)%7+1/3), y=40*((month_range[0]+n-1)//7+2)+5)
for n in range(pmr[1]-month_range[0]+1,pmr[1]+1):
    days.append(tk.Button(top1,text=n,fg="gray",height = 2,width=5))
    days[-1].bind("<1>",callback3)
    days[-1].place(x=45*((month_range[0]+n-1-pmr[1])%7+1/3), y=40*(2)+5)
for n in range(1,(8-(month_range[1]+month_range[0])%7)):
    days.append(tk.Button(top1,text=n,fg="gray",height = 2,width=5))
    days[-1].bind("<1>",callback4)
    days[-1].place(x=45*((month_range[0]+n+month_range[1]-1)%7+1/3),y=40*((month_range[0]+n+month_range[1]%7-1)//7+6)+5)

top1.mainloop()

##from　大介
# last_month_range = calendar.monthrange(ty, tm-1)
# month_range = calendar.monthrange(ty, tm)
# next_month_range = calendar.monthrange(ty, tm+1)
# days = []

# t = 14
# td = 1 + t
# day = (month_range[0]+t)%7

# for n in range(td-day-14, td-day+21):
#     print(n)
#     if n <= 0:
#         days.append(tk.Button(top1,text=last_month_range[1]+n,fg="gray",height = 2,width=5))
#         days[-1].bind("<1>",callback2)
#         ## days.append(tk.Button(top1,text=n,height = 2,width=5,command=lambda : button_click(n)))
#         days[-1].place(x=45*((month_range[0]+n-1)%7+1), y=40*((n-td+day)//7+4)+5)
#     elif n == td:
#         days.append(tk.Button(top1,text=n,fg="red",height = 2,width=5))
#         days[-1].bind("<1>",callback2)
#         ## days.append(tk.Button(top1,text=n,height = 2,width=5,command=lambda : button_click(n)))
#         days[-1].place(x=45*((month_range[0]+n-1)%7+1), y=40*((n-td+day)//7+4)+5)
#     elif n <= month_range[1]:
#         days.append(tk.Button(top1,text=n,height = 2,width=5))
#         days[-1].bind("<1>",callback2)
#         ## days.append(tk.Button(top1,text=n,height = 2,width=5,command=lambda : button_click(n)))
#         days[-1].place(x=45*((month_range[0]+n-1)%7+1), y=40*((n-td+day)//7+4)+5)
#     else:
#         days.append(tk.Button(top1,text=n-month_range[1],fg="gray",height = 2,width=5))
#         days[-1].bind("<1>",callback2)
#         ## days.append(tk.Button(top1,text=n,height = 2,width=5,command=lambda : button_click(n)))
#         days[-1].place(x=45*((month_range[0]+n-1)%7+1), y=40*((n-td+day)//7+4)+5)

## 今月
# for n in range(1-month_range[0], 43-month_range[0]):
#     print(n)
#     if n <= 0:
#         days.append(tk.Button(top1,text=last_month_range[1]+n,fg="gray",height = 2,width=5))
#         days[-1].bind("<1>",callback2)
#         ## days.append(tk.Button(top1,text=n,height = 2,width=5,command=lambda : button_click(n)))
#         days[-1].place(x=45*((month_range[0]+n-1)%7+1), y=40*((n-1+month_range[0])//7+2)+5)
#     elif n == td:
#         days.append(tk.Button(top1,text=n,fg="red",height = 2,width=5))
#         days[-1].bind("<1>",callback2)
#         ## days.append(tk.Button(top1,text=n,height = 2,width=5,command=lambda : button_click(n)))
#         days[-1].place(x=45*((month_range[0]+n-1)%7+1), y=40*((n-1+month_range[0])//7+2)+5)
#     elif n <= month_range[1]:
#         days.append(tk.Button(top1,text=n,height = 2,width=5))
#         days[-1].bind("<1>",callback2)
#         ## days.append(tk.Button(top1,text=n,height = 2,width=5,command=lambda : button_click(n)))
#         days[-1].place(x=45*((month_range[0]+n-1)%7+1), y=40*((n-1+month_range[0])//7+2)+5)
#     else:
#         days.append(tk.Button(top1,text=n-month_range[1],fg="gray",height = 2,width=5))
#         days[-1].bind("<1>",callback2)
#         ## days.append(tk.Button(top1,text=n,height = 2,width=5,command=lambda : button_click(n)))
#         days[-1].place(x=45*((month_range[0]+n-1)%7+1), y=40*((n-1+month_range[0])//7+2)+5)