import os
import multiprocessing
import time
import importlib
import time

# py -m pip install watchdog でインストール
# py -m pip install psutil でインストール
# def main():

PATH = os.path.dirname(__file__)+"/module"

# PATH = "./module"
FILES = os.listdir(PATH)

MODULE_LIST = [f for f in FILES if os.path.isdir(os.path.join(PATH, f))]
MODULE = [importlib.import_module("module."+mod_li+"."+mod_li) for mod_li in MODULE_LIST]
METHOD = {mod_li : getattr(mod, 'hello') for mod, mod_li in zip(MODULE, MODULE_LIST)}

CENTER  = "center"

UNI     = "UNI"
BROAD   = "BROAD"
RECEIVE = "receive"
SEND    = "send"

MAX_PROCESS = 8

def reset_module():
    FILES = os.listdir(PATH)
    MODULE_LIST = [f for f in FILES if os.path.isdir(os.path.join(PATH, f))]
    MODULE = [importlib.import_module(PATH[2:]+"."+mod_li+"."+mod_li) for mod_li in MODULE_LIST]
    METHOD = {mod_li : getattr(mod, 'hello') for mod, mod_li in zip(MODULE, MODULE_LIST)}
    return 1

def init_func():
    pass

def exert_func(connect, n):
    print("in exert_func :", connect.recv())
    return

def init_process(p):
    for n in range(MAX_PROCESS):
        p[n][0] = multiprocessing.Process(target=init_func,args=tuple())
        p[n][0].start()
    for n in range(MAX_PROCESS):
        p[n][0].join()
    return 1

if __name__ == "__main__":
    #reset_module()

    #------------------------
    print("in main function")
    #------------------------
    
    p = [[None, None] for i in range(8)]
    init_process(p)
    
    # print("interval_1")
    #---------------------------------------------------------------------------------------------------------------------------
    task_que = [[f, METHOD[f], []] for f in FILES if os.path.isdir(os.path.join(PATH, f)) and (f=="Chara" or f=="Pallet")]
    #---------------------------------------------------------------------------------------------------------------------------
    active_module_list = []
    connection = {}
    for mod_li in MODULE_LIST:
        conn_r, conn_w = multiprocessing.Pipe(duplex=False)
        conn_w.send([])
        connection[mod_li] = [conn_r, conn_w]
    requests = {RECEIVE : {},
                SEND    : {}}
    
    # print(MODULE_LIST)
    # print(connection)
    # for i in MODULE_LIST:
    #     print(connection[i][0].recv())

    def reset_requests():
        requests[RECEIVE].clear()
        requests[SEND].clear()
        requests[RECEIVE] = {mod_li : [] for mod_li in [CENTER]+active_module_list}
        return 1
    
    # print("interval_3")

    # print(task_que)
    # print(p)

    n = 0
    while True:
        time.sleep(0.016)
        while task_que:
            if not p[n][0].is_alive():
                p[n][0].close()
                # print(task_que[0])
                if task_que[0][0] in MODULE_LIST:
                    p[n][0] = multiprocessing.Process(target=task_que[0][1], args=tuple(connection[task_que[0][0]]+task_que[0][2]))
                    p[n][0].start()

                    if p[n][1] in active_module_list:
                        active_module_list.remove(p[n][1])
                    p[n][1] = task_que[0][0]
                    active_module_list.append(p[n][1])
                    
                    del task_que[0]
            
            n += 1
            if n == MAX_PROCESS:
                break
        
        active_module_list = []
        for p_i in p:
            if p_i[0].is_alive():
                active_module_list.append(p_i[1])
                
        conn_data = {name : [] for  name in active_module_list}
        # print(conn_data)
        reset_requests()
        
        for mod_li in active_module_list:
            conn_r, conn_w = connection[mod_li]
            if conn_r.poll():
                # print(conn_data)
                conn_data[mod_li] = conn_r.recv()
            else:
                conn_data[mod_li] = []

        # print(conn_data)

        for mod_li in active_module_list:
            if conn_data[mod_li]:
                for i, conn_data_li in enumerate(conn_data[mod_li]):
                    task_name, main_method, sub_method, module, *conn_info = conn_data_li
                    if main_method == UNI:
                        if module in active_module_list:
                            if module!=mod_li:
                                # print("##")
                                del conn_data[mod_li][i]
                                # print("##", conn_data[module])
                                for j, conn_data_lj in enumerate(conn_data[module]):
                                    sub_task_name, sub_main_mathod, sub_sub_method, sub_module, *sub_conn_info = conn_data_lj
                                    if task_name==sub_task_name and module==sub_module and main_method==sub_main_mathod and sub_method==sub_sub_method:
                                        del conn_data[module][j]
                                conn_data[module].append([
                                    task_name,
                                    main_method,
                                    sub_method,
                                    module,
                                    *conn_info
                                ])
                                # print("##")
                        elif module == CENTER:
                            if task_name=="GetModuleList":
                                # print("#")
                                ver_list = MODULE_LIST.copy()
                                ver_list.remove("Chara")
                                ver_list.remove("Pallet")
                                del conn_data[mod_li][i]
                                conn_data[mod_li].append([
                                    "GetModuleList",
                                    "UNI",
                                    "SEND",
                                    mod_li,
                                    ver_list
                                ])
                            elif task_name=="RequestactiveModule":
                                ver_list = active_module_list.copy()
                                ver_list.remove("exit")
                                del conn_data[mod_li][i]
                                conn_data[mod_li].append([
                                    "RequestactiveModule",
                                    "UNI",
                                    "SEND",
                                    mod_li,
                                    ver_list
                                ])
                            elif task_name=="RequestModuleEnd":
                                sub_module, = conn_info
                                del conn_data[mod_li][i]
                                for i in range(MAX_PROCESS):
                                    if sub_module==p[i][1] and p[i][0].is_alive():
                                        conn_r, conn_w = connection[sub_module]
                                        # conn_r.close()  #?
                                        # conn_w.close()  #?
                                        # del conn_r
                                        # del conn_w
                                        p[i][0].terminate()
                                        conn_r, conn_w = multiprocessing.Pipe(duplex=False)
                                        conn_w.send([])
                                        connection[mod_li] = [conn_r, conn_w]
                                else:
                                    if sub_module==CENTER:
                                        for i in range(MAX_PROCESS):
                                            if p[i][0].is_alive():
                                                conn_r, conn_w = connection[p[i][1]]
                                                # conn_r.close()  #?
                                                # conn_w.close()  #?
                                                # del conn_r
                                                # del conn_w
                                                p[i][0].terminate()
                                        exit()
                                        # return -80
                            elif task_name=="RequestStartModule":
                                sub_module, sub_args = conn_info
                                sub_func = METHOD[sub_module]
                                del conn_data[mod_li][i]
                            
                                task_que.append([sub_module, sub_func, sub_args])
                            else:
                                print("error : cannot find the command")
                        else:
                            print("error : cannot find the active process")
                            if not conn_data[0] in MODULE_LIST:
                                print("error : cannot find the module in exertable modules.")
                    elif main_method == BROAD:  #   工事中
                        if sub_method == RECEIVE:
                            requests[sub_method][mod_li].append(module)
                        elif sub_method == SEND:
                            requests[sub_method][module] = [
                                task_name,
                                main_method,
                                sub_method,
                                module,
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
        
        for mod_li in active_module_list:
            if conn_data[mod_li]:
                conn_r, conn_w = connection[mod_li]
                conn_w.send(conn_data[mod_li])
                # conn_data[mod_li].clear()
        
        n = 0

    print("end of program")


# data = [
#     "GetModuleList",
#     "UNI",  #"BROAD"
#     "SEND", #"RECEIVE"
#     "module1",  #to
#     ["module1", "module2"]
# ]

# data = [
#     "RequestStartModule",
#     "UNI",  #"BROAD"
#     "SEND", #"RECEIVE"
#     "module1",  #to
#     function
#     args
# ]


