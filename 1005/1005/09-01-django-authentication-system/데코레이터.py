def preFunc():
    print('전처리')

def aftFunc():
    print('후처리')

# 전처리, 후처리 코드가 너무 중복된다
# 이걸 없애는 방법이 없을까 ? 
# 파이썬에서는 데코레이터를 사용한다

def myFunc():
    # 전처리
    preFunc()

    print("안녕~~")

    # 후처리 
    aftFunc()




# 데코레이터 function
# 메인 로직(func 함수)을 감싸주는 새로운 함수를 만든다

is_logined = False

def my_decorator(func):
    def wrapper():
        if not is_logined:
            print('로그인 하고 와라')
            return
        
        print('전처리')
        func()
        print('후처리')
    return wrapper



@my_decorator
def myFunc3():
    print('my func3')

myFunc3()