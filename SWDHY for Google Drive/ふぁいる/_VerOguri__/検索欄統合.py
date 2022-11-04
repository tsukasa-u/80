#各種インポート
import io,pathlib,os,pprint,re,pathlib
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk


#ディレクトリ移動
os.chdir('/Users')
files = os.listdir('/Users')


#ファイル選択画面の設定
center = tk.Tk()
center.title("ファイル選択") 
center.geometry("400x500")

enter1 = tk.Frame(center)
enter1.pack()

label = tk.Label(enter1, text='以下のファイルから、操作したいファイルを入力してください')
label.pack()
label = tk.Label(enter1, text=files)
label.pack()
text1 = tk.Entry(enter1)
text1.pack()
text1.insert(tk.END, '')


win1 = tk.Frame(center)
win1.pack()
label1 = tk.Label(win1, text='拡張子で検索')
label1.pack()
text2 = tk.Entry(win1)
text2.pack()
text2.insert(tk.END, '入力例:txt,pdf')

win2 = tk.Frame(center)
win2.pack()
label3 = tk.Label(win2, text='キーワード検索')
label3.pack()
text3 = tk.Entry(win2)
text3.pack()
text3.insert(tk.END, '入力例:講義資料,課題2')

frame1 = tk.Frame(center)
frame1.pack()
# frame1.grid()
txtbox = tk.Listbox(frame1,width=50, height=40)
txtbox.grid(row=0, column=0)

#縦方向スクロールバーの作成
yscroll = tk.Scrollbar(frame1, orient=tk.VERTICAL, command=txtbox.yview)
yscroll.grid(row=0, column=1, sticky=(tk.N, tk.S))
#yscroll.pack(side=tk.RIGHT, fill="y")
#横方向スクロールバーの作成
xscroll = tk.Scrollbar(frame1, orient=tk.HORIZONTAL, command=txtbox.xview)
xscroll.grid(row=1, column=0, sticky=(tk.E, tk.W))
#xscroll.pack(side=tk.BOTTOM, fill="x")
#動きをスクロールバーに反映
txtbox["yscrollcommand"] = yscroll.set
txtbox["xscrollcommand"] = xscroll.set

s = ""
def ok1_click():
    s = text1.get()
    os.chdir('/Users/'+s)
    
def ok2_click():
    s1 = text2.get()
    file_data_0 = []
    for curDir, dirs, files in os.walk('/Users/'+s):
        for file_0 in files:
            if file_0.endswith(s1):
                #print(os.path.join(curDir, file))
                file_data_0.append(file_0)
    file_data = file_data_0

    for file_0 in file_data:
        txtbox.insert(tk.END,file_0)
        

#キーワード検索
    
def ok3_click():
    s2 = text3.get()
    import glob
    matchPath = glob.glob('**/'+s2+ '**', recursive=True)
    
    #おそらくここのやつ
    basenm = os.path.basename(matchPath)
    print(basenm)
    
#ここまで

ok3Button = tk.Button(win2, text='検索', command=ok3_click)
ok3Button.pack()

ok2Button = tk.Button(win1, text='検索', command=ok2_click)
ok2Button.pack()
    
ok1Button = tk.Button(enter1, text='OK', command=ok1_click)
ok1Button.pack()
center.mainloop()