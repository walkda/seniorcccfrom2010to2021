import sys
raw_input = sys.stdin.readline
n = int(raw_input())
student_answers = []
teacher_answers = []
c = 0
for i in range(n):
    student_answers.append(raw_input())
for i in range(n):
    teacher_answers.append(raw_input())

for i in range(n):
    if student_answers[i] == teacher_answers[i]:
        c += 1

print(c)
