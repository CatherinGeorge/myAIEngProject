marks = [78, 85, 62, 90, 55, 88]
print("highest marks", max(marks))
print("lowest marks", min(marks))
average = sum(marks) / len(marks)
print("average marks", average)
for i in marks:
  if i>=75:
    print("distinction", i)
marks.append(95)
marks.remove(55)
marks.sort()
print(marks)

