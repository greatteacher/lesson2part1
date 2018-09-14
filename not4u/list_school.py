school=[
	{'school_class': '4a', 'scores': [5,5,5,5,5,5]},
	{'school_class': '4b', 'scores': [3,4,5,2,4,2,5]},
	{'school_class': '4c', 'scores': [5,4,5,2,3,4]},
    {'school_class': '4d', 'scores': [3,4,5,2,5,5,5,3,5]},
    {'school_class': '4г', 'scores': [2,2,2,2,2,2,2]}]
Student_sum = 0 
School_score = 0

for element in school:
    Cur_class_students = len(element['scores'])
    Student_sum += Cur_class_students
    Cur_class_score = 0
print(Student_sum)
for score in school:
	School_score+=score
print(School_score)
for Score in element['scores']:
        Cur_class_score += Score
        School_score += Score   
print (School_score)

Students_sum =0
marks_sum=0
mark=0
for mark in school:
    Students_sum +=mark
    marks_sum+=1
print(marks_sum)
print (Students_sum)
print('average = ', Students_sum/ marks_sum)

	{'school_class': '4a', 'scores': [5,5,5,5,5,5,5]},
	{'school_class': '4b', 'scores': [4,4,4,4,4,4,4]},
    {'school_class': '4г', 'scores': [2,2,2,2,2,2,2]}]