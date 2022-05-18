######################## 반복문 ##############################

# For 구문
list_to_log = list()
for index in range(10):
    list_to_log.append(index)
print(list_to_log)
print('---------------------------------------------------------------------------------')


# While 구문 (무한 반복 주의)
list_to_log = list()
MAX_LOOP_COUNT = 10
flag_loop = True
loop_count = 0
while flag_loop:
    list_to_log.append(loop_count)
    loop_count += 1
    if loop_count > MAX_LOOP_COUNT:
        flag_loop = False
print(list_to_log)
print('---------------------------------------------------------------------------------')


# Do-While 구문 (파이썬에는 없음)
list_to_log = list()
MAX_LOOP_COUNT = 10
flag_loop = True
loop_count = 0
list_to_log.append(loop_count)
loop_count += 1
while flag_loop:
    list_to_log.append(loop_count)
    loop_count += 1
    if loop_count > MAX_LOOP_COUNT:
        flag_loop = False
print(list_to_log)
print('---------------------------------------------------------------------------------')



