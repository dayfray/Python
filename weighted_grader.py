lloyd = {
    "name": "Lloyd",
    "homework": [90.0, 97.0, 75.0, 92.0],
    "quizzes": [88.0, 40.0, 94.0],
    "tests": [75.0, 90.0]
}
alice = {
    "name": "Alice",
    "homework": [100.0, 92.0, 98.0, 100.0],
    "quizzes": [82.0, 83.0, 91.0],
    "tests": [89.0, 97.0]
}
tyler = {
    "name": "Tyler",
    "homework": [0.0, 87.0, 75.0, 22.0],
    "quizzes": [0.0, 75.0, 78.0],
    "tests": [100.0, 100.0]
}


students = [lloyd,alice,tyler]

def average(list_of_numbers):
    return sum(list_of_numbers)/len(list_of_numbers) 
														

def get_average(student):
    avg_homework = average(student["homework"]) * 0.1 #weight of homework is 10%, this is just using the average function from above
    avg_quiz = average(student["quizzes"]) * 0.3 # weight of quiz grade is 30%
    avg_tests = average(student["tests"]) * 0.6 # weight of tests is 60%
    return avg_homework + avg_quiz + avg_tests
    
print get_average(alice) # this can be used with the input of any of the students' names (lloyd, alice, or tyler)





lloyd = {
    "name": "Lloyd",
    "homework": [90.0, 97.0, 75.0, 92.0],
    "quizzes": [88.0, 40.0, 94.0],
    "tests": [75.0, 90.0]
}
alice = {
    "name": "Alice",
    "homework": [100.0, 92.0, 98.0, 100.0],
    "quizzes": [82.0, 83.0, 91.0],
    "tests": [89.0, 97.0]
}
tyler = {
    "name": "Tyler",
    "homework": [0.0, 87.0, 75.0, 22.0],
    "quizzes": [0.0, 75.0, 78.0],
    "tests": [100.0, 100.0]
}

# Add your function below!
students = [lloyd,alice,tyler]

def average(list_of_numbers):
    return sum(list_of_numbers)/len(list_of_numbers)

def get_average(student):
    avg_homework = average(student["homework"]) * 0.1
    avg_quiz = average(student["quizzes"]) * 0.3
    avg_tests = average(student["tests"]) * 0.6
    return avg_homework + avg_quiz + avg_tests
    
def get_letter_grade(score):    
    if score >= 90:
        return "A"
    elif 80 <= score < 90:
        return "B"
    elif 70 <= score < 80:
        return "C"
    elif 60 <= score < 70: 
        return "D"  
    else:
        return "F"
    
score = get_average(lloyd)
print get_letter_grade(score)



lloyd = {
    "name": "Lloyd",
    "homework": [90.0, 97.0, 75.0, 92.0],
    "quizzes": [88.0, 40.0, 94.0],
    "tests": [75.0, 90.0]
}
alice = {
    "name": "Alice",
    "homework": [100.0, 92.0, 98.0, 100.0],
    "quizzes": [82.0, 83.0, 91.0],
    "tests": [89.0, 97.0]
}
tyler = {
    "name": "Tyler",
    "homework": [0.0, 87.0, 75.0, 22.0],
    "quizzes": [0.0, 75.0, 78.0],
    "tests": [100.0, 100.0]
}


students = [lloyd,alice,tyler]

def average(list_of_numbers):
    return sum(list_of_numbers)/len(list_of_numbers)

def get_average(student):
    avg_homework = average(student["homework"]) * 0.1
    avg_quiz = average(student["quizzes"]) * 0.3
    avg_tests = average(student["tests"]) * 0.6
    return avg_homework + avg_quiz + avg_tests
    
def get_letter_grade(score):    
    if score >=90:
        return "A"
    elif 80 <= score < 90:
        return "B"
    elif 70 <= score < 80:
        return "C"
    elif 60 <= score < 70: 
        return "D"  
    else:
        return "F"
    
score = get_average(lloyd)
print get_letter_grade(score)

def get_class_average(x):
    lloyd_avg = get_average(lloyd)
    alice_avg = get_average(alice)
    tyler_avg = get_average(tyler)
    return (lloyd_avg + alice_avg + tyler_avg)/3



print get_class_average(students)
