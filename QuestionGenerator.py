"""
This code will produce a .tex file with problems randomly
selected from pre-written .tex files.
"""
from random import sample

def parse_questions(file_path: str) -> list:
    '''returns a list of the questions in given file'''
    branching_file = open(file_path,'r')
    questions = []

    #go to first question
    line_data = ''
    while '%new_question' not in line_data:
        line_data = branching_file.readline()

    #prase questions
    while '%end_of_questions' not in line_data:
        new_question = ''
        line_data = branching_file.readline()
        
        #get all lines for a single question
        while '%new_question' not in line_data and '%end_of_questions' not in line_data:
            new_question += line_data
            line_data = branching_file.readline()

        questions.append(new_question)
    branching_file.close()
    return questions

def pick_questions(question_set: list, qty: int) -> list[str]:
    '''picks qty questions from question_set and returns as string'''
    if len(question_set) <= qty:
        return question_set
    return sample(question_set, qty)
    #return ''.join(sample(question_set, qty))

def write_quiz(questions, quiz_name:str, student_file:str, qty: int=3, more_question=[], more_qty=0):
    '''Generates a unique quiz for each student'''
 
    new_file = open(f'./quizFolder/{quiz_name}_quiz.tex','w')

    #all packages used should be written in skeleton file
    skeleton_file = open('./skeletonFile/skeleton.tex')

    #copies content of skeleton file to new_file
    #ie. writes up to begin document
    new_file.write(skeleton_file.read())
    skeleton_file.close()

    #code to write each person's unique quiz
    my_class = open(student_file)
    for person in my_class.readlines()[1:]:
        techid, last_name, first_name, section_number = person.strip().split(',')

        new_file.write(f'{first_name} {last_name} \hfill {quiz_name} quiz\\\\\n')
        new_file.write(f'section {section_number}\\\\\n')
        #new_file.write('\\noindent\makebox[\linewidth]{\\rule{\paperwidth}{0.4pt}}')
        
        new_file.write('\\begin{enumerate}\n')
        #new_file.write(pick_questions(branching_questions,3))
        new_file.write(''.join(pick_questions(questions,qty)))
        if more_question:
            new_file.write(''.join(pick_questions(more_question,more_qty)))
            
        new_file.write('\\end{enumerate}\n')
        new_file.write('\\pagebreak\n')

    new_file.write('\end{document}')
    new_file.close()

def write_retake(all_questions: list[list[str]], student_file:str, midterm: bool= True) -> None:
    from math import floor

    quiz_name = 'midterm retake' if midterm else 'final retake'
    new_file = open(f'./quizFolder/{quiz_name}_quiz.tex','w')

    #all packages used should be written in skeleton file
    skeleton_file = open('./skeletonFile/skeleton.tex')

    #copies content of skeleton file to new_file
    #ie. writes up to begin document
    new_file.write(skeleton_file.read())
    skeleton_file.close()

    #code to write each person's unique make up quiz
    my_class = open(student_file)


    for person in my_class.readlines()[1:]:
        data = person.strip().split(',')
        last_name = data[1]
        first_name = data[2]
        section = data[3]
        grades = data[4:]
        question_pool = []
        for index, grade in enumerate(grades):
            if float(grade) < 3:
                score = floor(float(grade))
                question_pool.extend(sample(all_questions[index], 3-score))
        
        if question_pool != []:
            new_file.write(f'{first_name} {last_name} \hfill {quiz_name} quiz\\\\\n')
            new_file.write(f'section {section}\\\\\n')
            #new_file.write('\\noindent\makebox[\linewidth]{\\rule{\paperwidth}{0.4pt}}')
            
            new_file.write('\\begin{enumerate}\n')
            new_file.write(''.join(pick_questions(question_pool,5)))

            new_file.write('\\end{enumerate}\n')
            new_file.write('\\pagebreak\n')

    new_file.write('\end{document}')
    new_file.close()

def main():

    #This parses all the questions in each latex file
    basic_IO_questions = parse_questions('./01_Basic_IO/basic_IO.tex')
    expresion_questions = parse_questions('./02_expressions/expressions.tex')
    branching_questions = parse_questions('./03_branching/branching.tex')
    loop_questions = parse_questions('./04_loops/loops.tex')
    function_questions = parse_questions('./05_1_functions/functions.tex')
    string_questions = parse_questions('./05_2_strings/strings.tex')
    list_questions = parse_questions('./06_lists/lists.tex')
    dictionary_questions = parse_questions('./07_dictionaries/dictionaries.tex')
    adv_fctns_questions = parse_questions('./08_advanced-functions/advanced_functions.tex')
    debugger_questions = parse_questions('./09_debugger/debugger.tex')
    classes1_questions = parse_questions('./10_classes1/classes1.tex')
    classes2_questions = parse_questions('./11_classes2/classes2.tex')
    classes3_questions = parse_questions('./12_classes3/classes3.tex')
    files_questions = parse_questions('./13_files/files.tex')

    #adds all questions to a common question pool. Used for retake
    all_questions = []
    all_questions.append(basic_IO_questions)
    all_questions.append(expresion_questions)
    all_questions.append(branching_questions)
    all_questions.append(loop_questions)
    all_questions.append(function_questions + string_questions)
    all_questions.append(list_questions)
    all_questions.append(dictionary_questions)

    #Make sure the following file name matches your file
    retake_student_file_name = 'MyClassWithGrades.csv'
    write_retake(all_questions, retake_student_file_name)

    #Make sure the following file name matches your file    
    student_name_file = "MyClass.csv"

    write_quiz(basic_IO_questions, 'Basics and Basic IO',student_name_file)
    write_quiz(expresion_questions, 'Expresions',student_name_file)
    write_quiz(branching_questions, 'Branching',student_name_file)
    write_quiz(loop_questions, 'Loop',student_name_file)
    write_quiz(function_questions, 'fctns and strings',student_name_file, 2, string_questions, 1)
    write_quiz(list_questions, 'Lists',student_name_file)
    write_quiz(dictionary_questions, 'Dictionaries',student_name_file)
    write_quiz(adv_fctns_questions, 'Advanced Functions',student_name_file)
    write_quiz(debugger_questions, 'Debugger', qty=2,student_file=student_name_file)
    write_quiz(classes1_questions, 'Classes Part 1', student_name_file)
    write_quiz(classes2_questions, 'Classes Part 2', qty=2, student_file=student_name_file)
    write_quiz(classes3_questions, 'Classes Part 3',student_name_file)
    write_quiz(files_questions, 'Files', student_name_file)


if __name__ == '__main__':
    main()