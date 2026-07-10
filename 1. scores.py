import numpy as np
student_scores = np.array([
    [85, 90, 78, 88],
    [75, 80, 85, 82],
    [92, 88, 91, 87],
    [70, 76, 80, 79]
])
subjects = ["Math", "Science", "English", "History"]
avg_scores = np.mean(student_scores, axis=0)
print("Average Scores:")
for i in range(len(subjects)):
    print(subjects[i], ":", avg_scores[i])
highest = np.argmax(avg_scores)
print("\nSubject with Highest Average Score:", subjects[highest])
print("Average Score:", avg_scores[highest])
