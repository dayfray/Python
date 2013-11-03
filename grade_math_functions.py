# statistical program comparing grades and computing their sums, averages, variance, and standard deviation
# using custom functions


grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def print_grades(grades):
    for grade in grades:
        print grade

def grades_sum(grades):
    total = 0
    for grade in grades: 
        total += grade
    return total
    
def grades_average(grades):
    sum_of_grades = grades_sum(grades)
    average = sum_of_grades / len(grades)
    return average

def grades_variance(scores, average): 
    variance = 0
    for i in scores:
        variance += (average-i)**2
    return variance/len(scores)

def grades_std_deviation(variance):
    return variance**(0.5)

print print_grades(grades)
print grades_sum(grades)
print grades_average(grades)
print grades_variance(grades,grades_average(grades))
print grades_std_deviation(grades_variance(grades,grades_average(grades)))