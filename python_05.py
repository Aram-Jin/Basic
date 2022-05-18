import multiprocessing
import os
import pandas
import sqlite3

# 파일 처리

print('파일에 내용을 기록합니다.')
sample_file_name = 'smaple.csv'
with open(sample_file_name, 'w')as f:
    f.write('C1,C2\n')
    f.write('1,2\n')
    
print('---------------------------------------------------------------------------------')

print('파일 안의 내용을 확인합니다.')
#display(pandas.read_csv(sample_file_name))
print(pandas.read_csv(sample_file_name))

print('---------------------------------------------------------------------------------')

print('파일의 내용을 읽습니다.')
with open(sample_file_name, 'r')as f:
    print(f.read())
    
print('---------------------------------------------------------------------------------')

print('사용한 파일을 삭제합니다.')
os.remove(sample_file_name)