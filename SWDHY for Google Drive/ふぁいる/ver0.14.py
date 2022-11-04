#各種インポート
import io,pathlib,os,pprint,re
import tkinter as tk
from tkinter import messagebox
os.chdir('/Users')
files = os.listdir('/Users')

enter1 = tk.Tk()
enter1.title("ファイル選択") 
enter1.geometry("400x300")


label1 = tk.Label(enter1, text='以下のファイルから、操作したいファイルを入力してください')
label1.pack()
label2 = tk.Label(enter1, text=files)
label2.pack()
text1 = tk.Entry(enter1)
text1.pack()
text1.insert(tk.END, '')
def ok1_click():
    s = text1.get()
    os.chdir('/Users/'+s)
    files1 = os.listdir()
    print(files1)
ok1Button = tk.Button(enter1, text='OK', command=ok1_click)
ok1Button.pack()
enter1.mainloop()