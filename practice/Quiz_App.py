"""
- build a quiz app using python dictionary
- Add static data of 5 questions in a list of dictionary
- Each element in list is 1 dictionary which contains all the data for 1 question(question, options, correct_answer) 
- Loop through the questions in list  and print them on screen(As below format) and record users answer using MCQ option like pattern.

# Q1: How many colors are there in a rainbow?
    A) 1
    B) 3
    C) 5
    D) 7
>> Type your answer here
quiz_questions = [
    {
        question:"How many colors in rainbow ?",
        options: {
            A:1
            B:3
            C:5
            D:7
        },
        correct_answer: "D"
    },
		{
        question:"How many wheels does a tricycle have?",
        options: {
            A:1
            B:3
            C:5
            D:7
        },
        correct_answer: "B"
    }
		.
		.
		.
		.
    .
]

- After each answer check if it was correct and update score, Then move to next question.
- after answering all questions display score. 

"""
"""
1) display questions.
2) display options.
3) take user input.
4) compare user input with given correct answer
5) if get match then increase score by +1
6) else decrese score by -1

#  quiz_questions - dictionary name
"""
def Quiz_game(quiz_questions):
    # score initially zero
    score = 0
    # to iterate elements in list use for loop.
    for question in quiz_questions:
        # print(question)
        print(question['question'])
        # print(question['options'])
        for opt in question['options']:
            print(opt, question['options'][opt] )
        # to access value of key(question) in dictionary(Question,Option)
        user_ans = input('Enter your answer: ')
        
        if user_ans == question['correct_answer']:
            score = score + 1
        else:
            score = score - 1
    print('Your score is: ',score)


def main():

   
    quiz_questions = [{'question': "How many colors in rainbow ?",
                        'options' : {'A':1,'B':3, 'c':5, 'D':7}, 'correct_answer' : "D"},

                        {'question':"How many wheels does a tricycle have?",
                         'options': {'A':1,'B':3, 'C':5, 'D': 7}, 'correct_answer' : "B"}]
    score = Quiz_game(quiz_questions)

main()