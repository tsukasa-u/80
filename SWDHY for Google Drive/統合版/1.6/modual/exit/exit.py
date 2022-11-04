import multiprocessing
import tkinter
import copy
import time

def hello(conn_r, conn_w, pos_x, pos_y):

    def convert_pipe(conn_data, data):
        task_name, main_method, sub_method, modual, *conn_info = data
        for i, conn_data_i in enumerate(conn_data):
            sub_task_name, sub_main_method, sub_sub_method, sub_modual, *sub_conn_info = conn_data_i
            if task_name==sub_task_name and main_method==sub_main_method and sub_method==sub_sub_method and modual==sub_modual:
                del conn_data[i]
        conn_data.append(data)

    conn_data = []
    if conn_r.poll():
        conn_data = conn_r.recv()
    convert_pipe(
        conn_data,
        [
            "RequestactiveModual",
            "UNI",
            "RECIEVE",
            "center"
        ]
    )
    conn_w.send(conn_data)

    ver = "empty"
    while ver=="empty" or ver=="yet":
        # print(conn_data)
        time.sleep(0.016)
        if conn_r.poll():
            conn_data = conn_r.recv()
            # print(conn_data)
            for i, conn_li in enumerate(conn_data):
                task_name, main_method, sub_method, modual, *conn_info = conn_li
                if task_name=="RequestactiveModual" and sub_method=="SEND":
                    del conn_data[i]
                    conn_w.send(conn_data)
                    ver, = conn_info
                    break
            else:
                conn_w.send(conn_data)
                ver = "yet"
        else:
            ver = "empty"
    active_modual_list = ver
    active_modual_label = [i+"を終了" for i in ver] + ["全体の終了", "戻る"]
    # print(active_modual_list)

    def select_now(event):
        for i in LB.curselection(): #現在選択されている項目を取得
            if active_modual_label[i]=="戻る":
                root.destroy()
            else:
                if conn_r.poll():
                    conn_data = conn_r.recv()
                else:
                    conn_data = []
                convert_pipe(
                    conn_data,
                    [
                        "RequestModualEnd",
                        "UNI",
                        "SEND",
                        "center",
                        active_modual_list[i] if active_modual_label[i]!="全体の終了" else "center"
                    ]
                )
                conn_w.send(conn_data)
            root.destroy()

    root = tkinter.Tk()
    root.wm_attributes("-topmost", True) 
    root.title("exit")
    root.geometry("+"+str(pos_x)+"+"+str(pos_y))

    listarray = active_modual_label
    txt = tkinter.StringVar(value=listarray) 
    LB = tkinter.Listbox(root, listvariable=txt, width=28, height=15)
    LB.pack()
    LB.bind('<<ListboxSelect>>', select_now)

    root.mainloop()
