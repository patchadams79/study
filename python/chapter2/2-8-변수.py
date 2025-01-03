# a = [1, 2, 3]
# b = a
# print(id(a)) # 140239366366784
# print(id(b)) # 140239366366784

# a = [1, 2, 3]
# b = a
# a[1] = 4
# print(a) # [1, 4, 3]
# print(b) # [1, 4, 3]

# a = [1, 2, 3]
# b = a[:]
# a[1] = 4
# print(a) # [1, 4, 3]
# print(b) # [1, 2, 3] # a와 b는 다른 객체이다. a의 값을 변경해도 b는 영향을 받지 않는다.

# a, b = ('python', 'Life')
# print(a) # python # 튜플은 괄호를 생략해도 된다.
# print(b) # Life

# [a, b] = ['python', 'Life']
# print(a) # python # 리스트는 괄호를 생략할 수 없다.
# print(b) # Life

# a = b = 'python'
# print(a) # python
# print(b) # python # a와 b는 같은 객체이다. a의 값을 변경하면 b도 변경된다.

# a = 3
# b = 5
# a, b = b, a
# print(a) # 5 # a와 b의 값을 바꿀 때 임시 변수를 사용하지 않아도 된다.
# print(b) # 3 # 파이썬에서는 이렇게 간단하게 값을 바꿀 수 있다.

