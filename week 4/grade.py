def average_grade(records):
    total_grade = sum(record[2]for record in records)
    return total_grade/ len(records)

students = (
    ("jot",20,85),
    ("reet",2,88),
    ("peet",22,85)
)
 
def main():
    avg_grade=average_grade(students)
    print("average grade:",avg_grade)
main()