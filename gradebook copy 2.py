student = { 
    "Name": 'Michael Lee',
    "Class": '27F',
    "Grade": []
}
studentlist = student['name']
def students():
    students = (input("Enter Student's Name"))
    studentlist.append(students)
    students = (input("Enter Student's Class"))

gradelist = student['Grade']
def Grade():
    Grade = int(input('what is your grade?')) 
    gradelist.append(Grade)
    moregrade = input("Want to enter more grades? Y/N")
    if moregrade == 'Y':
        Grade()
    else:
        return 
    

    length = len(student['Grade'])
    gradetotal = sum(student['Grade'])
    avg = gradetotal/length
    print(avg)



