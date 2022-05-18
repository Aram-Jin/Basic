#from C010_01_review_python_functions import *
import multiprocessing
import os
import pandas
import sqlite3

# 데이터
value1 = 1.1
value2 = '1.2'
value3 = 1.3
value4 = 1
value5 = 0

# 1. 정수/실수/참거짓/문자열 예시
print('정수유형')
print('실제값', value1, '(',type(value1),')을 정수로 표현하면', int(value1), '입니다.')
print('---------------------------------------------------------------------------------')
print('실수유형')
print('실제값', value2,'(',type(value2),')을 실수로 표현하면', float(value2),'입니다.')
print('---------------------------------------------------------------------------------')
print('참/거짓 유형')
print('실제값', value4,'(',type(value4),')을 참/거짓으로 표현하면',bool(value4),'입니다.')
print('실제값', value5,'(',type(value5),')을 참/거짓으로 표현하면',bool(value5),'입니다.')
print('---------------------------------------------------------------------------------')
print('문자유형')
print('실제값',value3,'(',type(value3),')을 문자열로 표현하면',str(value3),'입니다.')
print('---------------------------------------------------------------------------------')


# 2. set 유형 예시
set_sample = set()
set_sample.add(1)
set_sample.add(2)
set_sample.add(3)
set_sample.add(4)
set_sample.add(5)
set_sample.add(1)
print('---------------------------------------------------------------------------------')
print('set 유형 (값이 중복되지 않습니다.)')
print(set_sample)
print('---------------------------------------------------------------------------------')


# 3. list 유형 예시
list_sample = list()
list_sample.append(1)
list_sample.append(2)
list_sample.append(3)
list_sample.append(4)
list_sample.append(5)
list_sample.append(1)
print('---------------------------------------------------------------------------------')
print('list 유형 (중복을 허용합니다.)')
print(list_sample)
print('---------------------------------------------------------------------------------')


# 4. dict 유형 예시
dict_sample = dict()
dict_sample['key:1'] = 1
dict_sample['key:2'] = 2
dict_sample['key:3'] = 3
dict_sample['key:4'] = 4
dict_sample['key:5'] = 5
dict_sample['key:6'] = 6
print('---------------------------------------------------------------------------------')
print('dict 유형 (key에서는 중복을 허용하지 않고, value에서는 중복을 허용합니다.)')
print(dict_sample)
print('---------------------------------------------------------------------------------')


# 5. DataFrame 유형 예시
df_sample = pandas.DataFrame([
    {'C1':1, 'C2':2},
    {'C1':3, 'C2':4},
    {'C1':5, 'C2':6},
    {'C1':7, 'C2':8}
])
print('---------------------------------------------------------------------------------')
print('DataFrame 유형 (jupyter에서는 display를 사용하면 조금 더 확이니 쉽습니다.)')
# display(df_sample)
print(df_sample)
print('---------------------------------------------------------------------------------')


# 6. Series 유형 예시
print('Series 유형 (DataFrame의 부분 집합입니다.)')
print(type(df_sample['C1']), df_sample['C1'])


