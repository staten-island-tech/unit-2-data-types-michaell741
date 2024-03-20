students = []

def avg(grades):
    return sum(grades)/len(grades)
def createstudent(name, classroom, grades):
    avg = avg(grades)
    return {"Name": name, "classroom": classroom, "Grades":grades, "Student Average": avg}


createmorestudents = "Yes"
while createmorestudents == "Yes":
    studentname = (input("Enter Student's Name"))
    studentclass = (input("Enter Student's class"))
    studentgrades = [int(i) for i in input("Enter Student's class")]
    newstudent = createmorestudents(studentname, studentclass, studentgrades)
    students.append (newstudent)
    print(students)
    for student in students:
        print(student)
    createmorestudents = (input("Want to create more students? Y/N"))

    if createmorestudents == "Y":
        createmorestudents()


    

     


    




    