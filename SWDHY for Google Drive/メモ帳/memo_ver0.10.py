#実行のために、[memo1.txt,memo2.txt,memo3.txt,memo4.txt,memo5.txt]
#という5つのテキストファイルを[pythonプログラムと同ディレクトリ]に用意してください

#各種インポート
import tkinter as tk
from tkinter import messagebox,ttk

top1 = tk.Tk()
top1.title("メモ帳")
top1.geometry("600x400")
nb = ttk.Notebook(width=800, height=700)
tab1 = tk.Frame(nb)
tab2 = tk.Frame(nb)
tab3 = tk.Frame(nb)
tab4 = tk.Frame(nb)
tab5 = tk.Frame(nb)
nb.add(tab1, text='メモ1', padding=5)
nb.add(tab2, text='メモ2', padding=5)
nb.add(tab3, text='メモ3', padding=5)
nb.add(tab4, text='メモ4', padding=5)
nb.add(tab5, text='メモ5', padding=5)
nb.pack(expand=1, fill='both')

#tab1設定
frame1 = tk.Frame(tab1)
frame1.grid(row=0,column=0)
text1 = tk.Text(frame1)
text1.grid(row=1,column=1,columnspan=3,ipadx=4,ipady=10)
for line in open("memo1.txt",encoding="utf-8_sig"):
    text1.insert(tk.END,line)
text1.insert(tk.END, '')
    #スクロールバーの作成
yscroll = tk.Scrollbar(frame1, orient=tk.VERTICAL, command=text1.yview)
yscroll.grid(row=1, column=4, sticky=tk.N+tk.S)
    #動きをスクロールバーに反映
text1["yscrollcommand"] = yscroll.set

#tab2設定
frame2 = tk.Frame(tab2)
frame2.grid(row=0,column=0)
text2 = tk.Text(frame2)
text2.grid(row=1,column=1,columnspan=3,ipadx=4,ipady=10)
for line in open("memo2.txt",encoding="utf-8_sig"):
    text2.insert(tk.END,line)
text2.insert(tk.END, '')
    #スクロールバーの作成
yscroll2 = tk.Scrollbar(frame2, orient=tk.VERTICAL, command=text2.yview)
yscroll2.grid(row=1, column=4, sticky=tk.N+tk.S)
    #動きをスクロールバーに反映
text2["yscrollcommand"] = yscroll2.set

#tab3設定
frame3 = tk.Frame(tab3)
frame3.grid(row=0,column=0)
text3 = tk.Text(frame3)
text3.grid(row=1,column=1,columnspan=3,ipadx=4,ipady=10)
for line in open("memo3.txt",encoding="utf-8_sig"):
    text3.insert(tk.END,line)
text3.insert(tk.END, '')
    #スクロールバーの作成
yscroll3 = tk.Scrollbar(frame3, orient=tk.VERTICAL, command=text3.yview)
yscroll3.grid(row=1, column=4, sticky=tk.N+tk.S)
    #動きをスクロールバーに反映
text3["yscrollcommand"] = yscroll3.set

#tab4設定
frame4 = tk.Frame(tab4)
frame4.grid(row=0,column=0)
text4 = tk.Text(frame4)
text4.grid(row=1,column=1,columnspan=3,ipadx=4,ipady=10)
for line in open("memo4.txt",encoding="utf-8_sig"):
    text4.insert(tk.END,line)
text4.insert(tk.END, '')
    #スクロールバーの作成
yscroll4 = tk.Scrollbar(frame4, orient=tk.VERTICAL, command=text4.yview)
yscroll4.grid(row=1, column=4, sticky=tk.N+tk.S)
    #動きをスクロールバーに反映
text4["yscrollcommand"] = yscroll4.set

#tab5設定
frame5 = tk.Frame(tab5)
frame5.grid(row=0,column=0)
text5 = tk.Text(frame5)
text5.grid(row=1,column=1,columnspan=3,ipadx=4,ipady=10)
for line in open("memo5.txt",encoding="utf-8_sig"):
    text5.insert(tk.END,line)
text5.insert(tk.END, '')
    #スクロールバーの作成
yscroll5 = tk.Scrollbar(frame5, orient=tk.VERTICAL, command=text5.yview)
yscroll5.grid(row=1, column=4, sticky=tk.N+tk.S)
    #動きをスクロールバーに反映
text5["yscrollcommand"] = yscroll5.set


#コマンド
def save1_click():
    txt1=text1.get(1.0,tk.END)
    with open("memo1.txt", mode="w", encoding="utf-8_sig") as f:
        f.write(txt1)
save1Button = tk.Button(frame1, text='保存', command=save1_click)
save1Button.grid(row=2,column=1)
def delete1_click():
    text1.delete(1.0,tk.END)
delete1Button = tk.Button(frame1,text='削除',command=delete1_click)
delete1Button.grid(row=2,column=2)

def save2_click():
    txt2=text2.get(1.0,tk.END)
    with open("memo2.txt", mode="w", encoding="utf-8_sig") as f:
        f.write(txt2)
save2Button = tk.Button(frame2, text='保存', command=save2_click)
save2Button.grid(row=2,column=1)
def delete2_click():
    text2.delete(1.0,tk.END)
delete2Button = tk.Button(frame2,text='削除',command=delete2_click)
delete2Button.grid(row=2,column=2)

def save3_click():
    txt3=text3.get(1.0,tk.END)
    with open("memo3.txt", mode="w", encoding="utf-8_sig") as f:
        f.write(txt3)
save3Button = tk.Button(frame3, text='保存', command=save3_click)
save3Button.grid(row=2,column=1)
def delete3_click():
    text3.delete(1.0,tk.END)
delete3Button = tk.Button(frame3,text='削除',command=delete3_click)
delete3Button.grid(row=2,column=2)

def save4_click():
    txt4=text4.get(1.0,tk.END)
    with open("memo4.txt", mode="w", encoding="utf-8_sig") as f:
        f.write(txt4)
save4Button = tk.Button(frame4, text='保存', command=save4_click)
save4Button.grid(row=2,column=1)
def delete4_click():
    text4.delete(1.0,tk.END)
delete4Button = tk.Button(frame4,text='削除',command=delete4_click)
delete4Button.grid(row=2,column=2)
def destroy4_click():
    text4.delete(1.0,tk.END)
    txt4=text4.get(1.0,tk.END)
    with open("memo4.txt", mode="w", encoding="utf-8_sig") as f:
        f.write(txt4)
destroy4Button = tk.Button(frame4,text='削除して保存',bg='orangered',command=destroy4_click)
destroy4Button.grid(row=2,column=3)

def save5_click():
    txt5=text5.get(1.0,tk.END)
    with open("memo5.txt", mode="w", encoding="utf-8_sig") as f:
        f.write(txt5)
save5Button = tk.Button(frame5, text='保存', command=save5_click)
save5Button.grid(row=2,column=1)
def delete5_click():
    text5.delete(1.0,tk.END)
delete5Button = tk.Button(frame5,text='削除',command=delete5_click)
delete5Button.grid(row=2,column=2)
def reload5_click():
    text5.delete(1.0,tk.END)
    for line in open("memo5.txt",encoding="utf-8_sig"):
        text5.insert(tk.END,line)
    text5.insert(tk.END, '')
reload5Button = tk.Button(frame5,text='読み込み',command=reload5_click)
reload5Button.grid(row=2,column=3)


top1.mainloop()