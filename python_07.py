import multiprocessing
import os
from sys import displayhook
import pandas
import sqlite3

############################### 병렬 처리 ####################################
list_param = list()
for idx in range(10):
    dic_param = dict()
    dic_param['index'] = idx
    list_param.append(dic_param)
    
p = multiprocessing.Pool(3)
# parallel_print 함수에 대한 정의는 .py파일에 별도로 지정되어 있어야 함
p.map(parallel_print, list_param)


############################### 함수 정의 ####################################
def parallel_print(p_args):
    import datetime
    import numpy
    import time
    index_value = p_args['index']
    sleep_time = numpy.random.rand()
    print(index_value, 'START', datetime.datetime.today(), sleep_time, flush=True)
    time.sleep(sleep_time)
    print(index_value, 'FINISH', datetime.datetime.today(), sleep_time, flush=True) 