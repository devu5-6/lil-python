student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}
for name,value in student_scores.items():
    # print(name,value)
    if (91<value<100):
        grade= 'outstanding'
    elif 81<value<90:
        grade= "Exceeds Expectations"
    elif 71<value<80:
        grade= "Acceptable"
    else:
        grade= "Fail"
    student_grades[name] =grade
print(student_grades)    
    


