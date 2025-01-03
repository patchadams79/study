# def add(a, b): # def를 사용하여 함수를 정의
#     return a + b # return을 사용하여 함수의 결과값을 반환

# print(add(3, 4)) 

# def add_many(*argu): # *를 사용하여 매개변수를 튜플로 만들어줌
#     result = 0
#     for i in argu:  # argu에 있는 값을 하나씩 더함
#         result = result + i
#     return result

# result = add_many(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# print(result)

# def add_mul(choice, *args):
#     if choice == "add":
#         result = 0
#         for i in args:
#             result = result + i
#     elif choice == "mul":
#         result = 1
#         for i in args:
#             result = result * i
#     return result

# result = add_mul("mul", 1, 2, 3, 4, 5)
# print(result)


# def print_kwargs(**kwargs):
#     print(kwargs)
# print_kwargs(a=1, b=2) # {'a': 1, 'b': 2} 출력

# def add_and_mul(a, b):
#     return a+b, a*b
# print(add_and_mul(3,4)) # (7, 12) 출력

# def say_myself(name, old, man=True): # 매개변수에 초깃값을 미리 설정
#     print("나의 이름은 %s 입니다." % name) 
#     print("나이는 %d살입니다." % old)
#     if man:
#         print("남자입니다.")
#     else:
#         print("여자입니다.")

# say_myself("Patch", 45, False)

# a = 1 
# def vartest(a): # 함수 안에서 선언한 변수는 함수 안에서만 사용됨
#     a = a + 1
#     return a # return을 사용하여 함수의 결과값을 반환
# a = vartest(a) # a에 vartest(a)의 결과값을 대입
# print(a) # 2 출력

# a = 1
# def vartest():
#     global a # global을 사용하여 함수 밖의 변수를 직접 사용
#     a = a + 1
# vartest()
# print(a) # 2 출력

# b = [1, 2, 3, 4]
# def vartest2(b):
#     b = b.append(5) # append는 반환값이 없음
#     return b 
# vartest2(b)
# print(b) # [1, 2, 3, 4, 5] 출력

# a = [1, 2, 3, 4]
# result = a.pop() # pop은 반환값이 있음
# print(result) # 4 출력
# print(a) # [1, 2, 3] 출력  # pop은 리스트의 마지막 요소를 돌려주고 그 요소는 삭제함

# add = lambda a, b: a+b # lambda를 사용하여 함수를 간단하게 표현
# result = add(3, 4)
# print(result) # 7 출력

# a = [lambda a, b: a+b, lambda a, b: a*b] # lambda를 리스트에 넣어서 사용
# print(a[0](3, 4)) # 7 출력 # fashion coding