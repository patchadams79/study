# f = open("newfile.txt", 'w')
# f.close()

# f = open("newfile.txt", 'w', encoding='utf-8')
# for i in range(1, 11):
#     data = "%d번째 줄입니다.\n" % i  
#     f.write(data)
# f.close()

# f = open("newfile.txt", 'r')
# line = f.readline()
# print(line)
# f.close() 

# f = open("newfile.txt", 'r')
# while True:
#     line = f.readline()
#     if not line:
#         break
#     print(line)
# f.close()

# while True:
#     data = input()
#     if not data: # 입력값이 없으면
#         break
#     print(data)

# f = open("newfile.txt", 'r')
# lines = f.readlines()
# for line in lines:
#     line = line.strip() # 줄 끝의 줄 바꿈 문자를 제거
#     print(line)
# f.close()

# f = open("newfile.txt", 'r')
# data = f.read()
# print(data)
# f.close()

# f = open("newfile.txt", 'r')
# for line in f:
#     print(line)
# f.close()

# f = open("newfile.txt", 'a') # 파일을 추가 모드로 열기
# for i in range(11, 20):
#     data = "%d번째 줄입니다.\n" % i
#     f.write(data)
# f.close()

with open("foo.txt", "w") as f: 
    f.write("Life is too short, you need python") # with를 사용하여 파일을 열고 자동으로 닫음