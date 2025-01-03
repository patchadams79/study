# s1 = set([1, 2, 3])
# print(type(s1)) # <class 'set'>

# s1 = set("Hello")
# print(s1) # {'H', 'e', 'l', 'o'}

# s1 = set("Hello")
# print(s1[0]) # TypeError: 'set' object is not subscriptable

# s1 = set([1, 2, 3, 4, 5, 6])
# s2 = set([4, 5, 6, 7, 8, 9])
# print(s1 & s2) # {4, 5, 6}

# s1 = set([1, 2, 3, 4, 5, 6])
# s2 = set([4, 5, 6, 7, 8, 9])
# print(s1.intersection(s2)) # {4, 5, 6}

# s1 = set([1, 2, 3, 4, 5, 6])
# s2 = set([4, 5, 6, 7, 8, 9])
# print(s1 | s2) # {1, 2, 3, 4, 5, 6, 7, 8, 9}

# s1 = set([1, 2, 3, 4, 5, 6])
# s2 = set([4, 5, 6, 7, 8, 9])
# print(s1.union(s2)) # {1, 2, 3, 4, 5, 6, 7, 8, 9}

# s1 = set([1, 2, 3, 4, 5, 6])
# s2 = set([4, 5, 6, 7, 8, 9])
# print(s1-s2) # {1, 2, 3}

# s1 = set([1, 2, 3, 4, 5, 6])
# s2 = set([4, 5, 6, 7, 8, 9])
# print(s1.difference(s2)) # {1, 2, 3}

# s1 = set([1, 2, 3])
# s1.add(4)
# print(s1) # {1, 2, 3, 4}

# s1 = set([1, 2, 3])
# s1.update([4, 5, 6])
# print(s1) # {1, 2, 3, 4, 5, 6}

# s1 = set([1, 2, 3])
# s1.remove(2)
# print(s1) # {1, 3}

# l1 = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
# s1 = set(l1)
# print(s1) # {1, 2, 3, 4}

l1 = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
li = list(set(l1))
print(li) # [1, 2, 3, 4]
