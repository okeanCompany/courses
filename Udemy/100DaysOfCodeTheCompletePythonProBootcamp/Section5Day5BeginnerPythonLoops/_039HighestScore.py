student_scores = [180, 124, 165, 173, 189, 169, 146]

total_exam_score = sum(student_scores)

sum = 0
for score in student_scores:
    sum += score

print(sum)

max_score = 0
for score in student_scores:
    if score > max_score:
        max_score = score

print(max_score)
