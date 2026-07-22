#! python3
# randomQuizGenerator.py - Creates quizzes with questions and answers in
# random order, along with the answer key.

import random
import os

def main():

    os.makedirs("quizzes", exist_ok=True)
    os.makedirs("answers", exist_ok=True)

    capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
    'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
    'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
    'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois': 'Springfield', 
    'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas': 'Topeka', 
    'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine': 'Augusta', 
    'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan': 'Lansing', 
    'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri': 'Jefferson City', 
    'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':'Carson City', 
    'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 
    'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
    'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
    'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
    'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee': 'Nashville', 
    'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont': 'Montpelier', 
    'Virginia': 'Richmond', 'Washington': 'Olympia', 
    'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

    exam_count = int(input("plz inter the number of exams: "))

    for i in range(1, exam_count + 1):
        quizzes, key_answers = generateQuizzes(capitals)
        printer(quizzes, key_answers, i)


def generateQuizzes(capitals):
    #making quizzes
    questions = list(capitals.keys())
    random.shuffle(questions)
    quizzes = {}
    key_answers = {}

    #make options and answer
    question_number = 0
    option_name = ["a", "b", "c", "d"]
    for question in questions:

        question_number += 1
        answer = capitals[question]

        values = list(capitals.values())
        values.remove(answer)
        wrong_options = random.sample(values, 3)

        options = [answer] + wrong_options
        random.shuffle(options)
        
        key_answer = option_name[options.index(answer)]

        quizzes[question] = options
        key_answers[question_number] = key_answer

    return quizzes, key_answers

def printer(quizzes, key_answers, exam_num):
    #print quizzes
    file_name = f"exam{exam_num}.txt"
    path = ".\\quizzes\\" + file_name

    file = open(path, "w")
    quiz_number = 0
    option_name = ["a", "b", "c", "d"]
    for k, v in quizzes.items():
        
        quiz_number += 1
        file.write(f"{quiz_number}." + k + " :\n")

        for i in range(len(v)):
            file.write(option_name[i] + "." + v[i] + "\n")

        file.write("\n")

    file.close()

    #print answers
    file_name = f"answer{exam_num}.txt"
    path = ".\\answers\\" + file_name
    
    file = open(path, "w")
    
    for k, v in key_answers.items():
    
        file.write(f"{k} : {v}\n")
    
    file.close()
    
main()