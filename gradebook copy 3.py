student = { 
    "Name": 'Michael Lee',
    "Class": '27F',
    "Grade": [100, 99, 85]
}


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

