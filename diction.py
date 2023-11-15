
student_scores = {}
 

student_scores = {
    "davis": 90,
    "aiden": 85,
    "tegan": 78,
    "ethan": 92,
    "zack": 88
}
print("Student Scores:")
for student, score in student_scores.items():
    print(f"{student}: {score}")
average_score = sum(student_scores.values()) / len(student_scores)
print(f"average Test Score: {average_score}")
student_name = input("enter a students name to check their score ")
if student_name in student_scores:
    print(f"{student_name}s score is {student_scores[student_name]}")
else:
    print(f"student {student_name} not found in the dictonary")
update_student = input("enter the name of the student to update their score ")
if update_student in student_scores:
    new_score = int(input(f"enter {update_student}s new score: "))
    student_scores[update_student] = new_score
    print(f"{update_student}s score has been updated to {new_score}")
else:
    print(f"Student {update_student} not found in the dictionary")
remove_student = input("enter the name of the student to remove ")
if remove_student in student_scores:
    del student_scores[remove_student]
    print(f"{remove_student} has been removed from the disctonary")
else:
    print(f"student {remove_student} not found in the dictionary")
highscore = max(student_scores.values())
highscore = [student for student, score in student_scores.items() if score == highscore][0]
print(f"highest grade: {highscore} was done by {highscore}")
