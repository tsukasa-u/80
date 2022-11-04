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
center.title("ファイル検索") 
center.geometry("800x500")
enter1 = tk.Frame(center)
enter1.grid()

label = tk.Label(enter1, text='以下のファイルから、操作したいファイルを入力してください')
label.grid(row=0,column=0)
#ラジオボタン
#変数の設定(文字列)
var = tk.StringVar(
    master=enter1,
    value="ファイル選択",
    ) 
#選択値表示用ラベルの設定
l = tk.Label(
    master=enter1,
    bg="Lightblue",
    width=10,
    textvariable=var,
    )
l.grid()
#ラジオボタンの設定(文字列)
for i in range(len(files)):
    r = tk.Radiobutton(
        master=enter1,
        text=files[i],
        value=files[i],
        var=var,
        )
    r.grid()

#ディレクトリ移動
def ok1_click():
    s = var.get() 
    os.chdir('/Users/'+s)

    win1 = tk.Frame(center)
    win1.grid(row=3,column=0)
    label1 = tk.Label(win1, text='拡張子で検索')
    label1.grid(row=4,column=0)
    text2 = tk.Entry(win1)
    text2.grid(row=5,column=0)
    text2.insert(tk.END, '入力例:txt,pdf')

    win2 = tk.Frame(center)
    win2.grid()
    label3 = tk.Label(win2, text='キーワード検索')
    label3.grid()
    text3 = tk.Entry(win2)
    text3.grid()
    text3.insert(tk.END, '入力例:講義資料,課題2')

    frame1 = tk.Frame(center)
    frame1.grid(row=0,column=2,rowspan=5)
    txtbox = tk.Listbox(frame1,width=45, height=30)
    txtbox.grid(row=1,column=2)

    #縦方向スクロールバーの作成
    yscroll = tk.Scrollbar(frame1, orient=tk.VERTICAL, command=txtbox.yview)
    yscroll.grid(row=0, column=3,rowspan=5, sticky=tk.N+tk.S)
    #横方向スクロールバーの作成
    xscroll = tk.Scrollbar(frame1, orient=tk.HORIZONTAL, command=txtbox.xview)
    xscroll.grid(row=6, column=2, sticky=(tk.E, tk.W))
    #動きをスクロールバーに反映
    txtbox["yscrollcommand"] = yscroll.set
    txtbox["xscrollcommand"] = xscroll.set

    #拡張子検索
    def ok2_click():
        txtbox.delete(0, tk.END)  
        s1 = text2.get()
        file_data_0 = []
        for curDir, dirs, files in os.walk('/Users/'+s):
            for file_0 in files:
                if file_0.endswith('.'+s1):
                    #print(os.path.join(curDir, file))
                    file_data_0.append(file_0)
        file_data = file_data_0

        for file_0 in file_data:
            txtbox.insert(tk.END,file_0)

    #キーワード検索   
    def ok3_click():
        txtbox.delete(0, tk.END)  
        s2 = text3.get()
        import glob
        basenm = []
        for matchPath in glob.glob('**/'+s2+ '**', recursive=True):
            basenm.append(os.path.basename('/Users/'+s+'/'+ matchPath))
        for i in basenm:
                txtbox.insert(tk.END,i)
    #ここまで

    ok3Button = tk.Button(win2, text='検索', command=ok3_click)
    ok3Button.grid()

    ok2Button = tk.Button(win1, text='検索', command=ok2_click)
    ok2Button.grid()

ok1Button = tk.Button(enter1, text='OK', command=ok1_click)
ok1Button.grid()

center.mainloop()