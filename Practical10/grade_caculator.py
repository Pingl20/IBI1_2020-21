def grade_caculator(name, code_grade, poster_grade, exam_grade):
    # caculate the final grade
    final_grade = 0.4 * code_grade + 0.3 * poster_grade + 0.3 * exam_grade

    return name, final_grade

# example
result = grade_caculator("Li Hua", 88, 89, 85)
print(str(result[0]) + "'s final grade is " + str(result[1]) + ".")