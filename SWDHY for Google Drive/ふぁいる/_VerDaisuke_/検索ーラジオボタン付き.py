#各種インポート
import io,pathlib,os,pprint,re,pathlib
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk


#ディレクトリ移動
os.chdir('/Users')
files = os.listdir('/Users')



#ファイル選択画面の設定
enter1 = tk.Tk()
enter1.title("ファイル選択") 
enter1.geometry("400x300")

label = tk.Label(enter1, text='以下のファイルから、操作したいファイルを選択してください')#変更箇所
label.pack()
#label = tk.Label(enter1, text=files)
#label.pack()


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
l.pack()
#ラジオボタンの設定(文字列)
for i in range(len(files)):
    r = tk.Radiobutton(
        master=enter1,
        text=files[i],
        value=files[i],
        var=var,
        )
    r.pack()


def ok1_click():
    s = var.get() #変更箇所
    os.chdir('/Users/'+s)
#検索画面
    win1 = tk.Toplevel()
    win1.title("試験運用")
    win1.geometry("800x600")
#拡張子検索
    label1 = tk.Label(win1, text='拡張子で検索')
    label1.pack()
    text2 = tk.Entry(win1)
    text2.pack()
    text2.insert(tk.END, '入力例:txt,pdf')
    def ok2_click():
        s1 = text2.get()
        file_data_0 = []
        for curDir, dirs, files in os.walk('/Users/'+s):
            for file_0 in files:
                if file_0.endswith(s1):
                    #print(os.path.join(curDir, file))
                    file_data_0.append(file_0)
        file_data = file_data_0
        
        win2 = tk.Tk()
        win2.title("検索結果")
        win2.geometry("600x700")

        frame1 = tk.Frame(win2)
        frame1.grid()
        txtbox = tk.Listbox(frame1,width=50, height=40)
        for file_0 in file_data:
            txtbox.insert(tk.END,file_0)
            
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
        
#ウインドウの描画
        frame1.pack()
        win2.mainloop()

    ok2Button = tk.Button(win1, text='検索', command=ok2_click)
    ok2Button.pack()
#キーワード検索
    label3 = tk.Label(win1, text='キーワード検索')
    label3.pack()
    text3 = tk.Entry(win1)
    text3.pack()
    text3.insert(tk.END, '入力例:講義資料,課題2')
    def ok3_click():
        s2 = text3.get()
        import glob
        matchPath = glob.glob('**/'+s2+ '**', recursive=True)
        
        #おそらくここのやつ
        basenm = os.path.basename(matchPath)
        print(basenm)
        
        win3 = tk.Toplevel()
        win3.title("検索結果")
        win3.geometry("800x900")
        #label4 = tk.Label(win3,text= basename)
        #label4 = tk.Label(win3,text= matchPath)
        label4 = tk.Label(win3,text=s2+'の導入先は構成中')
        label4.pack()
        
        
        win3.mainloop()
    ok3Button = tk.Button(win1, text='検索', command=ok3_click)
    ok3Button.pack()
#ここまで
    win1.mainloop()
    
ok1Button = tk.Button(enter1, text='OK', command=ok1_click)
ok1Button.pack()
enter1.mainloop()