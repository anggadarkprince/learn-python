# comprehensive iteration
grades = [75, 78, 96, 67, 80]
print(grades)
grades = [grade + 5 for grade in grades]
print grades

words = ['NOW', 'IS', 'THE', 'TIME']
print words
words = [word.lower() for word in words]
print words

# from file
file = open('grades.txt', 'r')
grades = file.readlines();
print(grades)
for i in range(len(grades)):
    grades[i] = grades[i].rstrip()
print(grades)

# with condition
N = range(1, 101)
EN = [x for x in N if x % 2 == 0]
print EN
