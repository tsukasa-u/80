import os
import multiprocessing
import time
import importlib

# py -m pip install watchdog でインストール
# py -m pip install psutil でインストール

PATH = "./modual"
FILES = os.listdir(PATH)


MODUAL_LIST = [f for f in FILES if os.path.isdir(os.path.join(PATH, f))]
MODUAL = [importlib.import_module(PATH[2:]+"."+mod_li+"."+mod_li) for mod_li in MODUAL_LIST]
METHOD = {mod_li : getattr(mod, 'hello') for mod, mod_li in zip(MODUAL, MODUAL_LIST)}

CENTER  = "center"

UNI     = "UNI"
BROAD   = "BROAD"
RECEIVE = "receive"
SEND    = "send"

MAX_PROCESS = 2 # 8

def reset_modual():
    FILES = os.listdir(PATH)
    MODUAL_LIST = [f for f in FILES if os.path.isdir(os.path.join(PATH, f))]
    MODUAL = [importlib.import_module(PATH[2:]+"."+mod_li+"."+mod_li) for mod_li in MODUAL_LIST]
    METHOD = {mod_li : getattr(mod, 'hello') for mod, mod_li in zip(MODUAL, MODUAL_LIST)}
    return 1

def init_func():
    pass
    return

def exert_func(connect, n):
    print(connect.recv())
    return

def init_process(p):
    for n in range(MAX_PROCESS):
        p[n][0] = multiprocessing.Process(target=init_func,args=tuple())
        p[n][0].start()
    for n in range(MAX_PROCESS):
        p[n][0].join()
    return 1

if __name__ == "__main__":
    #reset_modual()

    #------------------------
    print("in main function")
    #------------------------
    
    p = [[None, None] for i in range(10)]
    init_process(p)
    
    task_que = [[f, METHOD[f], [1]] for f in FILES if os.path.isdir(os.path.join(PATH, f))] #------------------
    active_modual_list = []
    connection = {mod_li : multiprocessing.Pipe(duplex=False) for mod_li in MODUAL_LIST}
    requests = {RECEIVE : {},
                SEND    : {}}

    def reset_requests():
        requests[RECEIVE].clear()
        requests[SEND].clear()
        requests[RECEIVE] = {mod_li : [] for mod_li in [CENTER]+active_modual_list}
        return 1

    while True:
        while task_que:
            for n in range(MAX_PROCESS):
                if p[n][0].exitcode != None:
                    if task_que[0][1] in MODUAL_LIST:
                        p[n][0] = multiprocessing.Process(target=task_que[0][1], args=tuple([connection[task_que[0][0]][1]]+task_que[0][2]))
                        p[n][0].start()

                        if p[n][1] in active_modual_list:
                            active_modual_list.remove(p[n][1])
                        p[n][1] = task_que[0][0]
                        active_modual_list.append(p[n][1])
                        
                        del task_que[0]
        
        while not task_que:
            reset_requests()
            for mod_li in active_modual_list:
                conn_r, conn_w = connection[mod_li]
                if conn_r.poll():
                    conn_data = conn_r.recv()
                    main_method = conn_data["mainmethod"]
                    sub_method = conn_data["submethod"]
                    modual = conn_data["modual"]
                    conn_info = conn_data["info"]
                    task_name = conn_data["name"]
                    if main_method == UNI:
                        if modual in active_modual_list:
                            conn_data["modual"] = mod_li    #str(mod_li)
                            
                            conn_r, conn_w = connection[modual]
                            conn_w.send(conn_data)
                        elif modual == CENTER:
                            if task_name=="GetModualList":
                                conn_r, conn_w = connection[modual]
                                conn_w.send({
                                    "method"    : "UNI",
                                    "modual"    : "center",
                                    "submethod" : "SEND",
                                    "name"      : "GetModualList",
                                    "info"      : {
                                        "list" : ["modual1", "modual2"]
                                    }
                                })
                            elif task_name=="RequestStartModual":
                                sub_modual = conn_info["modual"]
                                sub_func = conn_info["func"]
                                sub_args = list(conn_info["args"])
                            
                                task_que.append([sub_modual, sub_func, sub_args])
                            else:
                                print("error : cannot find the command")
                        else:
                            print("error : cannot find the active process")
                            if not conn_data[0] in MODUAL_LIST:
                                print("error : cannot find the modual in exertable moduales.")
                    elif main_method == BROAD:
                        if sub_method == RECEIVE:
                            requests[sub_method][mod_li].append(modual)
                        elif sub_method == SEND:
                            conn_data["modual"] = mod_li
                            requests[sub_method][modual] = conn_data
                        else:
                            print("error : third argment passed is invalid. set \'%s\' or \'%s\'." %(RECEIVE, SEND))
                    else:
                        print("error : first argment passed is invalid. set \'%s\' or \'%s\'." %(UNI, BROAD))
            
            for mod_li, name_li in requests[RECEIVE].items():
                for sub_name in name_li:
                    sub_args = requests[SEND][sub_name]

                    conn_r, conn_w = connection[mod_li]
                    conn_w.send(sub_args)

    print("end of program")


# data = {
#     "mainmethod": "UNI",  #"BROAD"
#     "modual"    : "modual1",  #to
#     "submethod" : "SEND", #"RECEIVE"
#     "name"      : "GetModualList",
#     "info"      : {
#         "list" : ["modual1", "modual2"]
#     }
# }

# data = {
#     "mainmethod"    : "UNI",  #"BROAD"
#     "modual"    : "modual1",  #to
#     "submethod" : "SEND", #"RECEIVE"
#     "name"      : "RequestStartModual",
#     "info"      : {
#         "modual" : "modual1",
#         "func"   : "function1",
#         "args"   : "argments1"
#     }
# }


