import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import importlib

allmodule = {'module1':{'k1':'chara','k2':'キャラクター制御','k3':'a1'},
             'module2':{'k1':'memo','k2':'メモ帳','k3':'a2'},
             'module3':{'k1':'calender','k2':'カレンダー','k3':'a3'},
             'module4':{'k1':'fileseach','k2':'ファイル検索','k3':'a4'},
             'module5':{'k1':'game','k2':'ミニゲーム','k3':'a5'},
             'module6':{'k1':'sample1','k2':'サンプル1','k3':'b1'},
             'module7':{'k1':'sample2','k2':'サンプル2','k3':'b2'},
             'module8':{'k1':'sample3','k2':'サンプル3','k3':'b3'},
             'module9':{'k1':'sample4','k2':'サンプル4','k3':'b4'},
             'module10':{'k1':'sample5','k2':'サンプル5','k3':'b5'},
             'module11':{'k1':'sample6','k2':'サンプル6','k3':'b6'}
            }

partmodule = 