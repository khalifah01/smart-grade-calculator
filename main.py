# Smart Grade Calculator

test_score = float(input("Enter test score: "))
assignment_score = float(input("Enter assignment score: "))
exam_score = float(input("Enter exam score: "))

total_score = test_score + assignment_score + exam_score
average_score = total_score / 3

print("\n--- Student Result ---")
print("Total Score:", total_score)
print("Average Score:", average_score)

if average_score >= 50:
    print("Status: PASSED")
else:
    print("Status: FAILED")

if average_score >= 70 and exam_score >= 60:
    print("Award Status: QUALIFIES FOR AWARD 🎉")
else:
    print("Award Status: DOES NOT QUALIFY FOR AWARD")
