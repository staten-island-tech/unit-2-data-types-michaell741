studentlist = []
gradelist = [] 
def avg():
    return sum(gradelist)/len(gradelist)
def createstudent(name, classroom, grades):
    gpa = avg()
    return {"Name": name, "classroom": classroom, "Grades":grades, "Student Average": gpa}


createmorestudents = "Y"
while createmorestudents == "Y":
    studentname = (input("Enter Student's Name"))
    studentclass = (input("Enter Student's class"))
    studentgrades = int(input('what is your grade?')) 
    gradelist.append(studentgrades)
    newstudent = createstudent(studentname, studentclass, studentgrades)
    studentlist.append (newstudent)
    print(studentlist)
    createmorestudents = (input("Want to create more students? Y/N"))
  
    if createmorestudents == "Y": 
        gradelist = [] 
        continue


    

     


    
for student in studentlist:
        print(student)
        break



    