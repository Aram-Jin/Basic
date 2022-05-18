import multiprocessing
import os
from sys import displayhook
import pandas
import sqlite3

# 데이터베이스 처리

# 데이터 베이스와 연결
print('connect to database')
conn = sqlite3.connect(':memory:')
curs = conn.cursor()


# 1. 테이블 생성
print('create table')
try:
    curs.execute('drop table sample')
    conn.commit()
except:
    pass
curs.execute('''
             create table sample(
                 c1 int,
                 c2 float,
                 c3 text)''')

conn.commit()
print('---------------------------------------------------------------------------------')

# 2. 데이터 입력
print('insert data to table')
df = pandas.DataFrame([
    {
        'c1':1,
        'c2':1.1,
        'c3':'2.2.2',
    },
])
# display(df)
print(df)
df.to_sql('sample', conn, if_exists='append', index=None)

print('---------------------------------------------------------------------------------')
print('check data in table')
df2 = pandas.read_sql('select*from sample', conn)
# display(df2)
print(df2)
print('---------------------------------------------------------------------------------')

# 3. 데이터 읽기
print('read data in table')
curs.execute('select*from sample')
rs = curs.fetchall()
for row in rs:
    print('c1:[', row[0], '], c2:[', row[1], '],c3:[', row[2],']')
print('---------------------------------------------------------------------------------')
