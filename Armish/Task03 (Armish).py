marks=int(input("Enter your marks 1-100:"))
if marks>=90 or marks==100:
    print("\nGrade A")
elif marks>=80 or marks<90:
    print("\nGrade B")
elif marks>=70 or marks<80:
    print("\nGrade C")
elif marks>=60 or marks<90:
    print("\nGrade D")
elif marks>=50 or marks<60:
    print("\nGrade E")
elif marks>=0 or marks<50:
    print("\nGrade F")
else:
    print("\nInvalid Entry")

