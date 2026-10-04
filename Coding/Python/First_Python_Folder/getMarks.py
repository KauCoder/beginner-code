from time import sleep

studentID = "GR510Y"
studentName = "Kaushal"

studentMarks = {
    "Science": 81,
    "Literacy": 92,
    "Math": 102,
    "Art": 65,
}

totalMarks = (studentMarks.get("Science") + studentMarks.get("Literacy") + studentMarks.get("Math") + studentMarks.get("Art")) / 4

if totalMarks >= 100:
    letterMarks = "A++"
elif totalMarks >= 80:
    letterMarks = "A"
elif totalMarks >= 70:
    letterMarks = "B+"
elif totalMarks >= 60:
    letterMarks = "B"
elif totalMarks >= 50:
    letterMarks = "C+"
elif totalMarks >= 40:
    letterMarks = "C"
elif totalMarks >= 30:
    letterMarks = "D+"
elif totalMarks >= 20:
    letterMarks = "D"
elif totalMarks >= 10:
    letterMarks = "F+"
elif totalMarks >= 5:
    letterMarks = "F"
elif totalMarks >= 0:
    letterMarks = "F-"

totalResults = (studentName, studentID, totalMarks)

print(f"Student: {studentName}. Student ID: {studentID}.\nMark is: {letterMarks} (Score is: totalMarks)")
sleep(1)
if totalMarks >= 60:
    print("Congratulations! You Passed!")
elif totalMarks < 60:
    print("You Failed. Don't Worry, You can take the test again!")