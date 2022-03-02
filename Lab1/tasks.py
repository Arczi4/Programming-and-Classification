import numpy as np

def task1():
    num = input("Enter a number:")
    if num.isdigit():
        if float(num) % 2 == 0:
            print("even number")
        else:
            print("odd number")
    else:
        print("Its not a number!")

def task2():
    return np.random.randint(10, 100, size=(20)).mean()

# Write a function that computes cosine of the angle between twod-dimensional vec-tors.
def task3(v1, v2):
    v1 = np.array(v1)
    v2 = np.array(v2)
    
    i = np.inner(v1, v2)
    n = np.linalg.norm(v1) * np.linalg.norm(v2)
    
    cos = i / n
    rad = np.arccos(np.clip(cos, -1.0, 1.0))
    return np.rad2deg(rad)

# Write a function that for a given set of integers{a, . . . , b}and 
# an integer c lists all integers greater than a and smaller than b that are divisible by c.
def task4(l, c):
    a = l[0]
    b = l[-1]
    
    res = []
    for x in l:
        if x > a and x < b and x % c == 0:
            res.append(x)
    print(res)

# Write a program that for two listsxandy(possibly of different sizes) returns 
# a list of elements that are common between the lists.

def task5(x, y):
    return list(set(x).intersection(y))

# Write a function that removes all a letters form a given stringx. 
# For example, for x = abracadabra we expect x = brcdbr
def task6(s:str) -> str:
    return s.replace("a", "")

# Write a program that accepts a sentence and calculates 
# the number of letters and digits. Hint: you can use functions isalpha() and isdigit().
def task7(s:str) -> tuple:
    count_alpha = len(list(filter(lambda l: l.isalpha(), s)))
    count_digits = len(list(filter(lambda l: l.isdigit(), s)))
    return count_alpha, count_digits

def task8():
    pass
# task1()
# print(task2())
# print(task3([0, 1], [1, 0]))
# task4(list(np.random.randint(0, 20, size=(20))), 2)
# print(task5([1, 2, 3, 5, 423], [5, 1, 3, 122, 423, 1]))
# print(task6('abracadabra'))
# print(task7('aa5511c'))

