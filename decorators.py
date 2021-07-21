
def decorator(func):
    def decotated(input_text):
        print('함수 시작!')
        func(input_text)
        print('함수 끝!')
    return decotated

@decorator
def hello_world(input_text):
    print(input_text)

hello_world('Hello World!')