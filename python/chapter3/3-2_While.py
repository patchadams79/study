# treehit = 0
# while treehit < 10:
#     treehit = treehit + 1
#     print("treehit %d" % treehit)
#     if treehit == 10:
#         print("treehit is down") # treehit is down # treehit이 10이 되면 treehit is down이 출력된다.

# treehit = 0
# while treehit < 10:
#     treehit += 1 # treehit = treehit + 1과 같은 의미이다.
#     print("treehit %d" % treehit) # treehit 1 ~ treehit 10까지 출력된다.
#     if treehit == 10: # treehit이 10이 되면
#         print("treehit is down") # treehit is down # treehit이 10이 되면 treehit is down이 출력된다.

# coffee = 10
# money = 300
# while money:
#     print("you received money and give you coffee") 
#     coffee = coffee - 1 # coffee -= 1과 같은 의미이다.
#     print("remain coffee %d" % coffee)
#     if coffee == 0:
#         print("coffee is sold out") 
#         break # break문을 사용하여 while문을 빠져나간다.

# coffee = 10
# while True:
#      money = int(input("insert money"))
#     if money == 300:
#         print("you received money and give you coffee")
#         coffee -= 1
#     elif money > 300:
#         print("you give me change %d" % (money - 300))
#         coffee -= 1
#     else:
#         print("you give me money back, don't give you coffee")
#         print("remain coffee %d" % coffee)
#     if coffee == 0:
#         print("coffee is sold out", "stop selling coffee")
#         break

# a = 0
# while a < 10:
#     a = a + 1
#     if a % 2 == 0: # a를 2로 나누었을 때 나머지가 0이면
#         continue # continue문을 사용하여 while문의 처음으로 돌아간다.
#     print(a) # 1 3 5 7 9 # a가 2로 나누어 떨어지지 않는 경우에만 a를 출력한다.

# a = 0
# while a < 10:
#     a = a + 1
#     if a % 2 == 0:
#         continue
#     print(a) # 1 3 5 7 9 # a가 2로 나누어 떨어지지 않는 경우에만 a를 출력한다.

