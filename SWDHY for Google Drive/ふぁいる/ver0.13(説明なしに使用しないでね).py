import io,pathlib,os,pprint,re
os.chdir('/Users')

#各種インポート

import tkinter as tk
from tkinter import messagebox
win1 = tk.Tk()
win2 = tk.Tk()

#プログラムタイトル

win1.title("試験運用") 
win2.title("検索結果")
#ウインドウサイズ

win1.geometry("800x600")
win2.geometry("800x600")
#拡張子検索

label = tk.Label(win1, text='拡張子で検索')
label.pack()
text1 = tk.Entry(win1)
text1.pack()
text1.insert(tk.END, 'キーワードを入力　例:txt,pdf')
def ok1_click():
    s = text1.get()
    for curDir, dirs, files in os.walk("/Users"):
        for file in files:
            if file.endswith(s):
                print(os.path.join(curDir, file))
                
                #問題点
                
                #label = tk.Label(win2, text=os.listdir(file))
                
                label.pack()
                win2.mainloop()
ok1Button = tk.Button(win1, text='OK', command=ok1_click)
ok1Button.pack()

#ファイル名検索

label = tk.Label(win1, text='ファイル名の一部で検索')
label.pack()
text2 = tk.Entry(win1)
text2.pack()
text2.insert(tk.END, 'キーワードを入力　例:test')
def ok2_click():
    s1 = text2.get()
    messagebox.showinfo('結果', s1 + 'は存在しません')
ok2Button = tk.Button(win1, text='OK', command=ok2_click)
ok2Button.pack()

#プログラムとして認識

win1.mainloop()