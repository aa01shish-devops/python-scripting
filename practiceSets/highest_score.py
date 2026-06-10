student_score = [
                 100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 
                 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79,
                 78, 77, 76, 75, 74, 73, 72, 71, 70, 69, 68,
                 67, 66, 65, 64, 63, 62, 61, 60, 59, 58, 57,
                 56, 55, 54, 53, 52
                 ]

total_score = 0 

for scores in student_score:
   # print(scores)
    total_score += scores
    
print(total_score)

sorted_student_score = sorted(student_score)

print(sorted_student_score[-1])

for score in range(1, 100):
    total_score += score

print(total_score)

