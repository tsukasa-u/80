#各種インポート
import io,pathlib,os,pprint,re,pathlib,shutil
import tkinter as tk
from tkinter import messagebox,ttk

def hello(conn_r, conn_w):
    #ディレクトリ移動
    os.chdir('/Users')
    files = os.listdir('/Users')


    #ファイル選択画面の設定
    center = tk.Tk()
    center.title("ファイル検索") 
    center.geometry("950x500")
    enter1 = tk.Frame(center)
    enter1.grid(row=0,column=0)

    label = tk.Label(enter1, text='以下のファイルから、操作したいファイルを選択してください')
    label.grid(row=0,column=0)
    #ラジオボタン
    #変数の設定(文字列)
    var = tk.StringVar(
        master=enter1,
        value="ファイル選択",
        ) 
    #選択値表示用ラベルの設定
    lab = tk.Label(enter1,bg="Lightblue",width=10,textvariable=var)
    lab.grid(row=1,column=0)
    #ラジオボタンの設定(文字列)
    for i in range(len(files)):
        r = tk.Radiobutton(
            master=enter1,
            text=files[i],
            value=files[i],
            var=var,
            )
        r.grid(row=2+i,column=0)

    #ディレクトリ移動
    def ok1_click():
        s = var.get()
        lab.destroy()
        l = tk.Label(
            master=enter1,
            bg="Lightblue",
            width=10,
            text=s,
            )
        l.grid(row=1,column=0) 
        os.chdir('/Users/'+s)

        frame6 = tk.Frame(center)
        frame6.grid(row=1,column=0)
        sflabel = tk.Label(frame6,text="選択中のファイル")
        sflabel.grid(row=0,column=0)
        sldf = tk.Listbox(frame6,height=1,width=30)
        sldf.grid(row=1,column=0)

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

        frame3 = tk.Frame(center)
        frame3.grid(row=0,column=5)
        label4=tk.Label(frame3,text="ファイル数")
        label4.grid(row=0,column=0)
        filenum = tk.Listbox(frame3,width=6,height=1)
        filenum.grid(row=1,column=0)

        frame6 = tk.Frame(center)
        frame6.grid(row=2,column=5)

        frame1 = tk.Frame(center)
        frame1.grid(row=0,column=2,rowspan=5)
        txtbox = tk.Listbox(frame1,width=40, height=30)
        txtbox.grid(row=1,column=2,sticky=tk.N)

        #縦方向スクロールバーの作成
        yscroll = tk.Scrollbar(frame1, orient=tk.VERTICAL, command=txtbox.yview)
        yscroll.grid(row=0, column=3,rowspan=5, sticky=tk.N+tk.S)
        #横方向スクロールバーの作成
        xscroll = tk.Scrollbar(frame1, orient=tk.HORIZONTAL, command=txtbox.xview)
        xscroll.grid(row=6, column=2, sticky=(tk.E, tk.W))
        #動きをスクロールバーに反映
        txtbox["yscrollcommand"] = yscroll.set
        txtbox["xscrollcommand"] = xscroll.set   

    ## ウインドウ追加用
        frame2 = tk.Frame(center)
        frame2.grid(row=0,column=4,rowspan=5,sticky=tk.N)
        txtbox1 = tk.Listbox(frame2,width=40, height=25)
        txtbox1.grid(row=1,column=4,sticky=tk.N)
        frame5 = tk.Frame(center)
        frame5.grid(row=4,column=4)
        dirp2 = tk.Label(frame5,text="ファイルの存在ディレクトリ")
        dirp2.grid(row=0,column=0)
        dirp1 = tk.Listbox(frame5,width=40, height=1)
        dirp1.grid(row=1,column=0,sticky=tk.N)
        xscroll3 = tk.Scrollbar(frame5,orient=tk.HORIZONTAL,command=dirp1.xview)
        xscroll3.grid(row=2,column=0,sticky=(tk.E,tk.W))
        dirp1["xscrollcommand"] = xscroll3.set

    ##    縦方向スクロールバーの作成
        yscroll2 = tk.Scrollbar(frame2, orient=tk.VERTICAL, command=txtbox1.yview)
        yscroll2.grid(row=0, column=5,rowspan=5, sticky=tk.N+tk.S)
    ##    横方向スクロールバーの作成
        xscroll2 = tk.Scrollbar(frame2, orient=tk.HORIZONTAL, command=txtbox1.xview)
        xscroll2.grid(row=6, column=4, sticky=(tk.E, tk.W))
    ##    動きをスクロールバーに反映
        txtbox1["yscrollcommand"] = yscroll2.set
        txtbox1["xscrollcommand"] = xscroll2.set

        global dicpw
        dicpw = 0
        dicp = []

        #拡張子検索
        def ok2_click():
            txtbox.delete(0, tk.END)
            txtbox1.delete(0,tk.END)
            dirp1.delete(0,tk.END)
            filenum.delete(0,tk.END)
            s1 = text2.get()
            file_data_0 = []
            fildir = []
            global fdn
            fdn = 0
            global dirp2
            dirp2 = -1
            for curDir, dirs, files in os.walk('/Users/'+s):
                for file_0 in files:
                    if file_0.endswith('.'+s1):
                        fdn = fdn +1
                        txtbox1.insert(tk.END,str(fdn)+":|"+str(os.path.join(curDir, file_0)))
                        fildir.insert(fdn,os.path.join(curDir,file_0))
                        file_data_0.append(file_0)
            file_data = file_data_0
            for file_0 in file_data:
                dirp2=dirp2+1
                txtbox.insert(tk.END,str(dirp2)+":|"+file_0)
            filenum.insert(tk.END,fdn)
            frame4 = tk.Frame(center)
            frame4.grid(row=1,column=5)
            def pls_click():
                dirp1.delete(0,tk.END)
                for i in txtbox.curselection():
                    dirp1.insert(tk.END,fildir[int(i)])
                    def fmm_click():
                        global dicpw
                        shutil.move(fildir[int(i)],dicp[int(dicpw-1)])            
                        cfdlab.destroy()
                        fmmButton.destroy()
                    cfdlab=tk.Label(frame6,text="指定ディレクトリに移動させる")
                    cfdlab.grid(row=0,column=0)
                    fmmButton = tk.Button(frame6,text="移動",command=fmm_click)
                    fmmButton.grid(row=1,column=0)
            plsButton = tk.Button(frame4, text='場所を表示', command=pls_click)
            plsButton.grid()
            
        #キーワード検索   
        def ok3_click():
            txtbox.delete(0, tk.END)
            txtbox1.delete(0,tk.END)
            dirp1.delete(0,tk.END)
            filenum.delete(0,tk.END)
            s2 = text3.get()
            import glob
            basenm = []
            fildir = []
            global fdn
            fdn = 0
            global dirp2
            dirp2 = 0
            for matchPath in glob.glob('**/*'+s2+ '**', recursive=True):
                fdn=fdn+1
                basenm.append(os.path.basename('/Users/'+s+'/'+ matchPath))
                txtbox1.insert(tk.END,str(fdn)+':|/Users/'+s+'/'+ matchPath)
                fildir.insert(fdn,'/Users/'+s+'/'+ matchPath)
            for i in basenm:
                dirp2=dirp2+1
                txtbox.insert(tk.END,str(dirp2)+":|"+i)
            filenum.insert(tk.END,fdn)        
            frame4 = tk.Frame(center)
            frame4.grid(row=1,column=5)
            def pls_click():
                dirp1.delete(0,tk.END)
                for i in txtbox.curselection():
                    dirp1.insert(tk.END,fildir[int(i)])
                    if os.path.isdir(fildir[int(i)]) ==True:
                        def fmp_click():
                            global dicpw
                            dicpw = dicpw +1
                            sldf.delete(0,tk.END)
                            sldf.insert(tk.END,fildir[int(i)])
                            dirp1.insert(tk.END,fildir[int(i)])
                            dicp.insert(dicpw,fildir[int(i)])
                            cfdlab.destroy()
                            fmmButton.destroy()
                            label4.destroy()
                            fmpButton.destroy()
                        label4=tk.Label(frame6,text="移動先ディレクトリに指定")
                        label4.grid(row=0,column=0)
                        fmpButton = tk.Button(frame6,text="指定",command=fmp_click)
                        fmpButton.grid(row=1,column=0)
                        def fmm_click():
                            global dicpw
                            shutil.move(fildir[int(i)],dicp[int(dicpw-1)])
                            cfdlab.destroy()
                            fmmButton.destroy()
                            label4.destroy()
                            fmpButton.destroy()
                        cfdlab=tk.Label(frame6,text="指定ディレクトリに移動させる")
                        cfdlab.grid(row=2,column=0)
                        fmmButton = tk.Button(frame6,text="移動",command=fmm_click)
                        fmmButton.grid(row=3,column=0)
                    else:
                        def fmm_click():
                            global dicpw
                            shutil.move(fildir[int(i)],dicp[int(dicpw-1)])
                            cfdlab.destroy()
                            fmmButton.destroy()
                        cfdlab=tk.Label(frame6,text="指定ディレクトリに移動させる")
                        cfdlab.grid(row=0,column=0)
                        fmmButton = tk.Button(frame6,text="移動",command=fmm_click)
                        fmmButton.grid(row=1,column=0)
                        
            plsButton = tk.Button(frame4, text='場所を表示', command=pls_click)
            plsButton.grid()       
        #ここまで

        ok3Button = tk.Button(win2, text='検索', command=ok3_click)
        ok3Button.grid()

        ok2Button = tk.Button(win1, text='検索', command=ok2_click)
        ok2Button.grid()

    ok1Button = tk.Button(enter1, text='OK', command=ok1_click)
    ok1Button.grid()

    center.mainloop()