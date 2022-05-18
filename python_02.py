#from C010_01_review_python_functions import *
import multiprocessing
import os
import pandas
import sqlite3

############################ 조건문 ################################

value1 = 1
value2 = 3.2
value3 = True
value4 = 'XX'


# 정수 값을 비교
condition_value = 2
if value1 > condition_value:
    print('value1 은', condition_value, '보다 작습니다.')
elif value1 == condition_value:
    print('value1 은', condition_value, '과 같습니다.')
else:
    print('value1 은', condition_value, '보다 큽니다.')
 
    
# 실수 값을 비교    
condition_value = 3
if value2 > condition_value:
    print('value2 은', condition_value, '보다 작습니다.')
elif value2 == condition_value:
    print('value2 은', condition_value, '과 같습니다.')
else:
    print('value2 은', condition_value, '보다 큽니다.')
    

# 참거짓 값을 비교
if value3:
    print('value3 은', value3, '참입니다.')
else:
    print('value3 은', value3, '거짓입니다.')
    

# 문자열 값을 비교
condition_value = 'YY'
if value4 > condition_value:
    print('value4 은', condition_value, '보다 작습니다.')
elif value4 == condition_value:
    print('value4 은', condition_value, '과 같습니다.')
else:
    print('value4 은', condition_value, '보다 큽니다.')
    