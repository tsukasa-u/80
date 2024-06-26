import zipfile,os,shutil,datetime
import tkinter as tk
# import pyminizip

cwd = os.getcwd()
os.chdir("/Users")
files = os.listdir("/Users")
center = tk.Tk()
center.geometry("950x500")
center.title("ファイルの圧縮・解凍")
enter1 = tk.Frame(center)
enter1.grid(row=0,column=0)
label = tk.Label(enter1, text='以下のファイルから、操作したいファイルを選択してください')
label.grid(row=0,column=0)
var = tk.StringVar(enter1,value="ファイル選択")
lab = tk.Label(enter1,bg="Lightblue",width=10,textvariable=var)
lab.grid(row=1,column=0)
for i in range(len(files)):
    r = tk.Radiobutton(enter1,text=files[i],value=files[i],var=var)
    r.grid(row=2+i,column=0)
def ok1_click():
    lab.destroy()
    s = var.get()
    os.chdir('/Users/'+s)
    l = tk.Label(enter1,bg="Lightblue",width=10,text=s)
    l.grid(row=1,column=0)

    if os.path.isdir("/Users/"+s+"/desktop/zipoutput")== True:
        pass
    else:
        os.mkdir("/Users/"+s+"/desktop/zipoutput")
    if os.path.isdir("/Users/"+s+"/desktop/output")== True:
        pass
    else:
        os.mkdir("/Users/"+s+"/desktop/output")

    frame6 = tk.Frame(center)
    frame6.grid(row=1,column=0)
    sflabel = tk.Label(frame6,text="選択中のファイル")
    sflabel.grid(row=0,column=0)
    # sldf = tk.Listbox(frame6,height=1,width=30)
    # sldf.grid(row=1,column=0)

    win1 = tk.Frame(center)
    win1.grid(row=3,column=0)
    label1 = tk.Label(win1, text='zipファイルを検索')
    label1.grid(row=1,column=0)

    win2 = tk.Frame(center)
    win2.grid(row=4,column=0)
    label3 = tk.Label(win2, text='フォルダ検索')
    label3.grid(row=0,column=0)
    text3 = tk.Entry(win2)
    text3.grid(row=1,column=0)
    text3.insert(tk.END, 'キーワードを入力')

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

    # global dicpw
    # dicpw = 0
    dicp = []

    #ファイル解凍
    def ok2_click():
        txtbox.delete(0, tk.END)
        txtbox1.delete(0,tk.END)
        dirp1.delete(0,tk.END)
        filenum.delete(0,tk.END)
        file_data_0 = []
        fildir = []
        global fdn
        fdn = 0
        global dirp2
        dirp2 = 0
        for curDir, dirs, files in os.walk('/Users/'+s):
            for file_0 in files:
                if file_0.endswith('.zip'):
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
                    uff.destroy()
                    cfdlab.destroy()
                    pwdentry.destroy()
                    fmpButton.destroy()
                    fmmButton.destroy()
                    nfn=file_data[int(i)]
                    efc = os.listdir("/Users/"+s+"/desktop/output/")
                    with zipfile.ZipFile(fildir[int(i)], 'r')as zf:
                        zf.extractall('/Users/'+s+'/desktop/output/'+str(len(efc)+1)+"_"+nfn.rstrip('.zip'))
                    fmmButton.destroy()
                uff=tk.Label(frame6,text="zipファイルを解凍")
                uff.grid(row=0,column=0)
                fmmButton = tk.Button(frame6,text="解凍",command=fmm_click)
                fmmButton.grid(row=1,column=0)
                def fmp_click():
                    efc = os.listdir("/Users/"+s+"/desktop/output/")
                    paswd = pwdentry.get()
                    uff.destroy()
                    cfdlab.destroy()
                    pwdentry.destroy()
                    fmpButton.destroy()
                    fmmButton.destroy()
                    nfn=file_data[int(i)]
                    with zipfile.ZipFile(fildir[int(i)], 'r')as zf:
                        zf.extractall('/Users/'+s+'/desktop/output/'+str(len(efc)+1)+"_"+nfn.rstrip('.zip'), pwd=paswd.encode())
                cfdlab=tk.Label(frame6,text="パスワード設定されたファイルを解凍")
                cfdlab.grid(row=2,column=0)
                pwdentry = tk.Entry(frame6,text="パスワードを入力")
                pwdentry.grid(row=3,column=0)
                fmpButton = tk.Button(frame6,text="移動",command=fmp_click)
                fmpButton.grid(row=4,column=0)
        plsButton = tk.Button(frame4, text='場所を表示', command=pls_click)
        plsButton.grid()
        
    #ファイル圧縮
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
            if os.path.isdir(matchPath) ==True:
                fdn=fdn+1
                basenm.append(os.path.basename('/Users/'+s+'/'+ matchPath))
                txtbox1.insert(tk.END,str(fdn)+':|/Users/'+s+'/'+ matchPath)
                fildir.insert(fdn,'/Users/'+s+'/'+ matchPath)
                dicp.insert(fdn,matchPath)
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
                def fmp_click():
                    efcz = os.listdir("/Users/"+s+"/desktop/zipoutput/")
                    dirp1.insert(tk.END,fildir[int(i)])
                    # cfdlab.destroy()
                    # fmmButton.destroy()
                    label4.destroy()
                    fmpButton.destroy()
                    # pwdentry.destroy()
                    shutil.make_archive("/Users/"+s+"/desktop/zipoutput/"+str(len(efcz)+1)
                                            +"_"+dicp[int(i)], 'zip',fildir[int(i)])
                label4=tk.Label(frame6,text="zipファイルに圧縮")
                label4.grid(row=0,column=0)
                fmpButton = tk.Button(frame6,text="圧縮",command=fmp_click)
                fmpButton.grid(row=1,column=0)

                #未実装
                # def fmm_click():
                #     efcz = os.listdir("/Users/"+s+"/desktop/zipoutput/")
                #     cfdlab.destroy()
                #     fmmButton.destroy()
                #     label4.destroy()
                #     fmpButton.destroy()
                #     paswd = pwdentry.get()
                #     pwdentry.destroy()
                #     coflis = os.listdir(fildir[int(i)])
                #     pyminizip.compress_multiple(coflis, "/Users/"+s+"/desktop/zipoutput/"+str(len(efcz)+1)+"_"+dicp[int(i)]+".zip",paswd, 2)
                # cfdlab=tk.Label(frame6,text="パスワードを付けて圧縮")
                # cfdlab.grid(row=2,column=0)
                # pwdentry = tk.Entry(frame6,text="パスワードを入力")
                # pwdentry.grid(row=3,column=0)
                # # complevel = tk.Entry(frame6,text="圧縮レベル選択(1~9)")
                # fmmButton = tk.Button(frame6,text="暗号化圧縮",command=fmm_click)
                # fmmButton.grid(row=4,column=0)

                    
        plsButton = tk.Button(frame4, text='場所を表示', command=pls_click)
        plsButton.grid()       
    #ここまで

    ok3Button = tk.Button(win2, text='検索', command=ok3_click)
    ok3Button.grid()

    ok2Button = tk.Button(win1, text='検索', command=ok2_click)
    ok2Button.grid()

ok1Button = tk.Button(enter1, text='OK', command=ok1_click)
ok1Button.grid(row =len(files)+2,column=0)

center.mainloop()