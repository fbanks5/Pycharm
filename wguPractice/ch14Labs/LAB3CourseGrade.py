# TODO: Declare any necessary variables here.
students = []
midterm1_scores = []
midterm2_scores = []
final_scores = []

# TODO: Read a file name from the user and read the tsv file here.
import os

file_name = input("Enter the name of the TSV file (e.g>, StudentInfo.tsv): ").strip()

if not os.path.exists(file_name):
    print(f"Error: File '{file_name}' not found.")
else:
    with open(file_name, "r") as file:
        for line in file:
            last_name, first_name, midterm1, midterm2, final = line.strip().split("\t")
            midterm1, midterm2, final = int(midterm1), int(midterm2), int(final)
            students.append((last_name, first_name, midterm1, midterm2, final))
            midterm1_scores.append(midterm1)
            midterm2_scores.append(midterm2)
            final_scores.append(final)

# TODO: Compute student grades and exam averages, then output results to a text file here.
letter_grades = []
for _, _, midterm1, midterm2, final in students:
    average_score = (midterm1 + midterm2 + final) / 3
    if average_score >= 90:
        grade = "A"
    elif average_score >= 80:
        grade = "B"
    elif average_score >= 70:
        grade = "C"
    elif average_score >= 60:
        grade = "D"
    else:
        grade = "F"
    letter_grades.append(grade)

# Computer averages for each exam
avg_midterm1 = sum(midterm1_scores) / len(midterm1_scores)
avg_midterm2 = sum(midterm2_scores) / len(midterm2_scores)
avg_final = sum(final_scores) / len(final_scores)

# Write results to the report.txt file
with open("report.txt", "w") as report_file:
    for (last_name, first_name, midterm1, midterm2, final), grade in zip(students, letter_grades):
        report_file.write(f"{last_name}\t{first_name}\t{midterm1}\t{midterm2}\t{final}\t{grade}\n")
    report_file.write(f"\nAverages: midterm1 {avg_midterm1:.2f}, midterm2 {avg_midterm2:.2f}, final {avg_final:.2f}\n")

print("Report has been written to report.txt.")