grades = [4, 5, 3, 5, 4, 2, 5]
print("Средня оценка:", (4+5+3+5+4+2+5)/7)

min = grades[0]
for n in grades:
    if n < min:
        min = n
print("Минимальная оценка:", min)

max = grades[0]
for m in grades:
    if m > max:
        max = m
print("Максимальная оценка:", max)
