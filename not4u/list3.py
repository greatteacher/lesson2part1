School = [
    {'school_class':'4a', 'Marks': [5,5,5,5,5,5,4,4,5,5]},
    {'school_class':'4b', 'Marks': [4,4,4,4,5,4]},
    {'school_class':'4c', 'Marks': [3,3,3,3,3,3,2]},
    {'school_class':'4г', 'Marks': [2,3,2,2,2,2,2,2]}
    ]
Cur_class_students =0
Student_sum = 0 
School_score =0
for element in School:
    Student_sum += Cur_class_students
    Cur_class_score = 0
    Cur_class_students =0
    for Score in element['Marks']:
        Cur_class_students +=1
        Cur_class_score += Score
        School_score += Score
    if Cur_class_students == 0:
        Average_class == 0
    else:    
        Average_class = Cur_class_score / Cur_class_students
    print ('Средняя оценка ', element['school_class'],'класса: ', (int(Average_class*100)/100),' =  ',
        Cur_class_score,'/', Cur_class_students, ", где общий бал / всего в классе")
Average = (School_score) / Student_sum
print ('Средняя оценка по школе:', float("{0:.3f}".format(Average)))