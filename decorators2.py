#삼각형의 넓이 계산 함수
#사각형의 넓이 계산 함수
#입력값이 모두 양수인지 확인, 아닐경우 에러발생




def triangle(input_text):
    print(input_text)

triangle('x*y*0.5')

def ractangle(input_text):
    print(input_text)

ractangle('x*y')





def check_integer(func):
    def decorated(width, height):
        if width >= 0 and height >= 0:
            return func(width, height)
        else:
            raise ValueError('check_integer')
    return decorated


