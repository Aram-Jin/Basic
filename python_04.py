############################# 예외 처리 ################################
value1 = '1.2'
try:
    print('문자열( 값', value1, ')을 정수 유형으로 변경합니다.')
    print('값을 출력합니다.[', int(value1),']')
    print('첫 시도에서 데이터 유형 변경에 성공하였습니다.')
except:
    print('데이터 유형 변환에 실패하여, 실수형으로 먼저 변경한 후 정수형으로 변경합니다.')
    print('값을 출력합니다.[', int(float(value1)),']')
    print('예외 처리로 데이터 유형 변경에 성공하였습니다.')
    
        
    
########################### 함수 선언 및 사용 #############################
def function_sample(p_args):
    print(type(p_args), p_args)
    
value1 = 1
value2 = 1.2
value3 = '2.3'
value4 = {'key':'value'}
value5 = ['element']

function_sample(value1)
function_sample(value2)
function_sample(value3)
function_sample(value4)
function_sample(value5)


########################## 클래스 선언 및 사용 ###################################
class class_sample():
    def method_sample(self, p_args):
        print(type(p_args),p_args)
        
value1 = 1
value2 = 1.2
value3 = '2.3'
value4 = {'key':'value'}
value5 = ['element']

sample = class_sample()
sample.method_sample(value1)
sample.method_sample(value2)
sample.method_sample(value3)
sample.method_sample(value4)
sample.method_sample(value5)



    
    