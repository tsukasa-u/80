import os
import multiprocessing
import time
import importlib
import time

# py -m pip install watchdog でインストール
# py -m pip install psutil でインストール

PATH = os.path.dirname(__file__)+"/modual"

# PATH = "./modual"
FILES = os.listdir(PATH)

MODUAL_LIST = [f for f in FILES if os.path.isdir(os.path.join(PATH, f))]
MODUAL = [importlib.import_module("modual."+mod_li+"."+mod_li) for mod_li in MODUAL_LIST]
METHOD = {mod_li : getattr(mod, 'hello') for mod, mod_li in zip(MODUAL, MODUAL_LIST)}

CENTER  = "center"

UNI     = "UNI"
BROAD   = "BROAD"
RECEIVE = "receive"
SEND    = "send"

MAX_PROCESS = 8

def reset_modual():
    FILES = os.listdir(PATH)
    MODUAL_LIST = [f for f in FILES if os.path.isdir(os.path.join(PATH, f))]
    MODUAL = [importlib.import_module(PATH[2:]+"."+mod_li+"."+mod_li) for mod_li in MODUAL_LIST]
    METHOD = {mod_li : getattr(mod, 'hello') for mod, mod_li in zip(MODUAL, MODUAL_LIST)}
    return 1

def init_func(n):
    print(n)
    return

def exert_func(connect, n):
    print("in exert_func :", connect.recv())
    return

def init_process(p):
    for n in range(MAX_PROCESS):
        p[n][0] = multiprocessing.Process(target=init_func,args=(n,))
        p[n][0].start()
        # p[n][0].join()
    return 1

if __name__ == "__main__":
    #reset_modual()

    #------------------------
    print("in main function")
    #------------------------
    
    p = [[None, None] for i in range(8)]
    init_process(p)
    
    # print("interval_1")
    #---------------------------------------------------------------------------------------------------------------------------
    task_que = [[f, METHOD[f], []] for f in FILES if os.path.isdir(os.path.join(PATH, f))]
    #---------------------------------------------------------------------------------------------------------------------------
    active_modual_list = []
    connection = {}
    for mod_li in MODUAL_LIST:
        conn_r, conn_w = multiprocessing.Pipe(duplex=False)
        conn_w.send([])
        connection[mod_li] = [conn_r, conn_w]
    requests = {RECEIVE : {},
                SEND    : {}}
    
    # print("interval_2")
    print(connection)

    def reset_requests():
        requests[RECEIVE].clear()
        requests[SEND].clear()
        requests[RECEIVE] = {mod_li : [] for mod_li in [CENTER]+active_modual_list}
        return 1
    
    # print("interval_3")

    # print(task_que)
    # print(p)

    n = 0
    while True:
        time.sleep(0.016)
        while task_que:
            if not p[n][0].is_alive():
                print(task_que[0])
                if task_que[0][0] in MODUAL_LIST:
                    p[n][0] = multiprocessing.Process(target=task_que[0][1], args=tuple(connection[task_que[0][0]]+task_que[0][2]))
                    p[n][0].start()

                    if p[n][1] in active_modual_list:
                        active_modual_list.remove(p[n][1])
                    p[n][1] = task_que[0][0]
                    active_modual_list.append(p[n][1])
                    
                    del task_que[0]
            
            n += 1
            if n == MAX_PROCESS:
                break
                
        conn_data = {name : [] for  name in active_modual_list}
        reset_requests()

        for mod_li in active_modual_list:
            conn_r, conn_w = connection[mod_li]
            if conn_r.poll():
                # print(conn_data)
                conn_data[mod_li] = conn_r.recv()
            else:
                conn_data[mod_li] = []

        # print(conn_data)

        for mod_li in active_modual_list:
            if conn_data[mod_li]:
                for i, conn_data_li in enumerate(conn_data[mod_li]):
                    task_name, main_method, sub_method, modual, *conn_info = conn_data_li
                    if main_method == UNI:
                        if modual in active_modual_list:
                            if modual!=mod_li:
                                # print("##")
                                del conn_data[mod_li][i]
                                # print("##", conn_data[modual])
                                for j, conn_data_lj in enumerate(conn_data[modual]):
                                    sub_task_name, sub_main_mathod, sub_sub_method, sub_modual, *sub_conn_info = conn_data_lj
                                    if task_name==sub_task_name and modual==sub_modual and main_method==sub_main_mathod and sub_method==sub_sub_method:
                                        del conn_data[modual][j]
                                conn_data[modual].append([
                                    task_name,
                                    main_method,
                                    sub_method,
                                    modual,
                                    *conn_info
                                ])
                                # print("##")
                        elif modual == CENTER:
                            if task_name=="GetModualList":
                                # print("#")
                                del conn_data[mod_li][i]
                                conn_data[mod_li].append([
                                    "GetModualList",
                                    "UNI",
                                    "SEND",
                                    mod_li,
                                    MODUAL_LIST
                                ])
                            elif task_name=="RequestStartModual":
                                sub_modual, sub_func, sub_args = conn_info
                                del conn_data[mod_li][i]
                            
                                task_que.append([sub_modual, sub_func, sub_args])
                            else:
                                print("error : cannot find the command")
                        else:
                            print("error : cannot find the active process")
                            if not conn_data[0] in MODUAL_LIST:
                                print("error : cannot find the modual in exertable moduales.")
                    elif main_method == BROAD:  #   工事中
                        if sub_method == RECEIVE:
                            requests[sub_method][mod_li].append(modual)
                        elif sub_method == SEND:
                            requests[sub_method][modual] = [
                                task_name,
                                main_method,
                                sub_method,
                                modual,
                                *conn_info
                            ]
                        else:
                            print("error : third argment passed is invalid. set \'%s\' or \'%s\'." %(RECEIVE, SEND))
                    else:
                        print("error : first argment passed is invalid. set \'%s\' or \'%s\'." %(UNI, BROAD))
                        
        for mod_li, name_li in requests[RECEIVE].items():
            for sub_name in name_li:
                sub_args = requests[SEND][sub_name]

                # conn_r, conn_w = connection[mod_li]
                # conn_w.send(sub_args)
                conn_data[mod_li].append([sub_args])
        
        for mod_li in active_modual_list:
            if conn_data[mod_li]:
                conn_r, conn_w = connection[mod_li]
                conn_w.send(conn_data[mod_li])
                # conn_data[mod_li].clear()
        
        n = 0

    print("end of program")


# data = [
#     "GetModualList",
#     "UNI",  #"BROAD"
#     "SEND", #"RECEIVE"
#     "modual1",  #to
#     ["modual1", "modual2"]
# ]

# data = [
#     "RequestStartModual",
#     "UNI",  #"BROAD"
#     "SEND", #"RECEIVE"
#     "modual1",  #to
#     function
#     args
# ]


