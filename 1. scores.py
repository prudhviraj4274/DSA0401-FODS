1. Scenario: You are working on a project that involves analyzing student performance data for a
class of 32 students. The data is stored in a NumPy array named student_scores, where each row
represents a student and each column represents a different subject. The subjects are arranged in the
following order: Math, Science, English, and History. Your task is to calculate the average score for
each subject and identify the subject with the highest average score.
Question: How would you use NumPy arrays to calculate the average score for each subject and
determine the subject with the highest average score? Assume 4x4 matrix that stores marks of each
student in given order.
    
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
