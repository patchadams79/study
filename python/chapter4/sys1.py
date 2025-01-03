# import sys
# args = sys.argv[0:]
# for i in args:
#     print(i)

# import sys
# sum = 0
# args = sys.argv[1:]
# for i in args:
#     sum = sum + int(i)
# print(sum)

# import sys
# args = sys.argv[1:]
# for i in args:
#     print(i.upper(), end=' ')

def up(*args):
    for i in args:
        print(i.upper(), end=' ')

up("hello", "world", "python") # HELLO WORLD PYTHON 출력