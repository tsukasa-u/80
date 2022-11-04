import tkinter as tk

# ウィンドウ作成
root = tk.Tk()
root.title("榛名")
root.minsize(796, 816)
 
# 画像表示
#fileに適当なpng画像を指定してください。
# fig2 = tk.PhotoImage(data=plt)
fig2 = tk.PhotoImage(file="Figure_2.png")
 
canvas = tk.Canvas(bg="black", width=796, height=816)
canvas.place(x=0, y=0)
canvas.create_image(0, 0, image=fig2, anchor=tk.NW)
 
# メインループ
root.mainloop()