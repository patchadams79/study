# test_list = ["one", "two", "three"]
# for i in test_list: # i에 test_list의 요소를 하나씩 대입
#     print(i) # one two three # test_list의 요소를 하나씩 출력한다.

# a = [(1, 2), (3, 4), (5, 6)] # a에 튜플을 요소로 갖는 리스트를 대입
# for (first, last) in a: # a의 요소를 하나씩 대입하여 first와 last에 대입
#     print(first + last) # 3 7 11 # a의 요소를 하나씩 대입하여 first와 last에 대입하고 first와 last의 합을 출력한다.

# marks = [90, 25, 67, 45, 80] # marks에 리스트를 대입
# number = 0 # number에 0을 대입
# for mark in marks: # marks의 요소를 하나씩 대입
#     number = number + 1
#     if mark >= 60:
#         print("%d student is pass" % number)
#     else:
#         print("%d student is failed" % number)

# marks = [90, 25, 67, 45, 80] # marks에 리스트를 대입
# number = 0
# for mark in marks:
#     number = number + 1
#     if mark < 60:
#         continue # mark가 60보다 작으면 다음 반복으로 넘어간다.
#     print("%d student is pass" % number) 

# add = 0 
# for i in range(1, 11) : # 1부터 10까지 반복
#     add = add + i # add에 i를 더한다.

# for i in range(2, 10):
#     for j in range(1, 10):
#         print(i * j, end=" ") # end=" "를 사용하여 줄바꿈을 하지 않고 공백을 출력한다.
#     print('')

# a = [1, 2, 3, 4]
# result = []
# for num in a:
#     result.append(num * 3) # num에 3을 곱한 값을 result에 추가
# print(result) # [3, 6, 9, 12]

# a = [1, 2, 3, 4]
# result = [num * 3 for num in a] # a의 요소를 num에 대입하여 num에 3을 곱한 값을 리스트에 추가
# print(result) # [3, 6, 9, 12] # a의 요소를 3을 곱한 값으로 리스트를 만들어 출력한다.

# a = [1, 2, 3, 4]
# result = [num * 3 for num in a if num % 2 == 0] # a의 요소를 num에 대입하여 num이 짝수인 경우에만 num에 3을 곱한 값을 리스트에 추가
# print(result) # [6, 12] # a의 요소 중 짝수인 요소만 3을 곱한 값을 리스트로 만들어 출력한다.