students = []

def avg(studentgrades):
    return (studentgrades)/len(studentgrades)
def createstudent(name, classroom, grades):
    avg = avg(grades)
    return {"Name": name, "classroom": classroom, "Grades":grades, "Student Average": avg}


createmorestudents = "Yes"
while createmorestudents == "Yes":
    studentname = (input("Enter Student's Name"))
    studentclass = (input("Enter Student's class"))
    studentgrades = int(input('what is your grade?')) 
    newstudent = createmorestudents(studentname, studentclass, studentgrades)
    students.append (newstudent)
    print(students)
    for student in students:
        print(student)
    createmorestudents = (input("Want to create more students? Y/N"))

    if createmorestudents == "Y":
        createmorestudents()


    

     


    




    