#各種インポート
import io,pathlib,os,pprint,re
import tkinter as tk
from tkinter import messagebox

#ディレクトリ移動
os.chdir('/Users')
files = os.listdir('/Users')

#ファイル選択画面の設定
enter1 = tk.Tk()
enter1.title("ファイル選択") 
enter1.geometry("400x300")

label = tk.Label(enter1, text='以下のファイルから、操作したいファイルを入力してください')
label.pack()
label = tk.Label(enter1, text=files)
label.pack()
text1 = tk.Entry(enter1)
text1.pack()
text1.insert(tk.END, '')
def ok1_click():
    s = text1.get()
    os.chdir('/Users/'+s)
#検索画面
    win1 = tk.Tk()
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
        file_data = ""
        for curDir, dirs, files in os.walk('/Users/'+s):
            for file in files:
                if file.endswith(s1):
                    #print(os.path.join(curDir, file))
                    file_data += file + "\n"
        win2 = tk.Tk()
        win2.title("検索結果")
        win2.geometry("800x900")
        label2 = tk.Label(win2,text=file_data)
        label2.pack()
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
        #import glob
        #matchPath = glob.glob('**/'+s2+ '**', recursive=True)
        #print(matchPath)




        win3 = tk.Tk()
        win3.title("検索結果")
        win3.geometry("800x900")
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


#if regex.search(name):
    #txtfiles.append(name)


