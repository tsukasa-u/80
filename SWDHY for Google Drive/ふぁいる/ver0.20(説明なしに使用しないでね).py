#日本語導入

import io

#各種インポート

import tkinter as tk
import tkinter.font as font
root = tk.Tk()
labelFont = font.Font(size=12,weight="normal")
import glob

#パス生成

import pathlib,re,os,pprint
#import os
#import pprint

#プログラムタイトル

root.title("試験運用")

#ウインドウサイズ

root.geometry("800x600+100+100")

#拡張子検索

label1 = tk.Label(root, text='拡張子で検索',font=labelFont)
label1.pack()
text1 = tk.Entry(root)
text1.pack()
text1.insert(tk.END, 'キーワードを入力　例:txt,pdf')	
ok1button = tk.Button(root,text="検索")
def ok1_click():
    s = text1.get()
    os.chdir('/Users')
    #path = '/Users'
    for curDir, dirs, files in os.walk("/Users"):
        for file in files:
            if file.endswith(s):
                print(os.path.join(curDir, file))

    #win3 = tk.Tk()
    #win3.title("エラー")
    #win3.geometry("400x100+300+200")
    #label2=tk.Label(win3,text='指定されたファイルは存在しません',font=labelFont)
    #label2.pack(anchor="center")
    #win3.mainloop()
ok1button["command"]=ok1_click
ok1button.pack()

#ファイル名検索

label3 = tk.Label(root, text='ファイル名の一部で検索',font=labelFont)
label3.pack()
text2 = tk.Entry(root)
text2.pack()
text2.insert(tk.END, 'キーワードを入力　例:test')	
ok2button = tk.Button(root,text="検索")
def ok2_click():
    #s = text1.get()
    win6 = tk.Tk()
    win6.title("エラー")
    win6.geometry("400x100+300+200")
    label4=tk.Label(win6,text='指定されたファイルは存在しません',font=labelFont)
    label4.pack(anchor="center")
    win6.mainloop()
ok2button["command"]=ok2_click
ok2button.pack()

#zipファイルの解凍
#zipファイルの生成
#os.chdir('/Users')
 #os.chdir('/Users/takami/desktop/')
#path = '/Users'
 #path='/Users/takami/desktop/'
#print(os.listdir(path))
#for txt in os.walk(path):
    #print('')
    #print('── {}'.format(txt))
    #print(' └── {}'.format(s))
    #print('   └── {}'.format(f))


#プログラムとして認識

root.mainloop()