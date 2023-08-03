import random
from time import sleep
# Import statement below used playsound2 library. The orignial playsound library has bugs not allowing certain audio to be played. 
from playsound import playsound

print('\nHello welcome to the program! This is a quiz game about random trivia and math problems.')
name = input('What is your name?: ')

trivia_questions = {
    1: 'What does “www” stand for in a website browser? [Hint: Three words, all beginning with an uppercase letter!]',
    2: 'How long is an Olympic swimming pool (in meters)? [Hint: Include the word "meters" in your answer]',
    3: 'Which country got hit by fat man and little-boy? [Hint: Country next to California]',
    4: 'Which country do cities of Perth, Adelaide & Brisbane belong to? [Hint: At the bottom of the world]',
    5: 'What geometric shape is generally used for stop signs?'
}

trivia_answers = {
    1: 'World Wide Web',
    2: '50 meters',
    3: 'Japan',
    4: 'Australia',
    5: 'Octagon'
}

math_questions = {
    1: 'What is 64 divided by 8?',
    2: 'What is five squared?',
    3: 'What is five to the power of zero?',
    4: 'Which prime number comes after 3?',
    5: 'What is the square root of 144?'
}

math_answers = {
    1: 8,
    2: 25,
    3: 1,
    4: 5,
    5: 12
}

replay = 'Y'
while replay == 'Y':
    mode = int(input('''\nHow would you like to play the game?
    Random Order(1) 
    Math First(2)
    Trivia First(3)
    Your Answer: '''))

    print('\nRemember, all math questions should be inputted as digits!')

    score = 0
    wrong = 0
    question = 0
    excluded_from_randomM = []
    excluded_from_randomT = []
    if mode == 1:
        while question != 10:

            type_of_question = random.randint(1, 2)

            try:
                random_num_math = random.choice(list(set([x for x in range(1, 6)]) - set(excluded_from_randomM)))
            except IndexError:
                type_of_question = 2
            try:
                random_num_trivia = random.choice(list(set([x for x in range(1, 6)]) - set(excluded_from_randomT)))
            except IndexError:
                type_of_question = 1

            if type_of_question == 1:
                user_ans = int(input('\n' + math_questions[random_num_math] + ': '))
                if user_ans == math_answers[random_num_math]:
                    playsound('CorrectAnswerSound.wav')
                    print("You're right!")
                    score += 1
                    question += 1
                    excluded_from_randomM.append(random_num_math)
                else:
                    playsound('WrongAnswerSound.wav')
                    print(f'Uh oh, you got that question wrong. The correct answer was {math_answers[random_num_math]}')
                    wrong += 1
                    question += 1
                    excluded_from_randomM.append(random_num_math)

            elif type_of_question == 2:
                user_ans = input('\n' + trivia_questions[random_num_trivia] + ': ')
                if user_ans == trivia_answers[random_num_trivia]:
                    print("You're right!")
                    playsound('CorrectAnswerSound.wav')
                    score += 1
                    question += 1
                    excluded_from_randomT.append(random_num_trivia)
                else:
                    print(f'Uh oh, you got that question wrong. The correct answer was {trivia_answers[random_num_trivia]}')
                    playsound('WrongAnswerSound.wav')
                    question += 1
                    wrong += 1
                    excluded_from_randomT.append(random_num_trivia)

    if mode == 2:
        while question != 5:
            type_of_question = 1

            try:
                random_num_math = random.choice(list(set([x for x in range(1, 6)]) - set(excluded_from_randomM)))
            except IndexError:
                type_of_question = 2

            if type_of_question == 1:
                user_ans = int(input('\n' + math_questions[random_num_math] + ': '))
                if user_ans == math_answers[random_num_math]:
                    print("You're right!")
                    playsound('CorrectAnswerSound.wav')
                    score += 1
                    question += 1
                    excluded_from_randomM.append(random_num_math)
                else:
                    print(f'Uh oh, you got that question wrong. The correct answer was {math_answers[random_num_math]}')
                    playsound('WrongAnswerSound.wav')
                    wrong += 1
                    question += 1
                    excluded_from_randomM.append(random_num_math)

        sleep(.5)
        print('\nNow time for the trivia!')

        while question >= 5 and question != 10:
            type_of_question = 2
            try:
                random_num_trivia = random.choice(list(set([x for x in range(1, 6)]) - set(excluded_from_randomT)))
            except IndexError:
                type_of_question = 1

            if type_of_question == 2:
                user_ans = input('\n' + trivia_questions[random_num_trivia] + ': ')
                if user_ans == trivia_answers[random_num_trivia]:
                    print("You're right!")
                    playsound('CorrectAnswerSound.wav')
                    score += 1
                    question += 1
                    excluded_from_randomT.append(random_num_trivia)
                else:
                    print(f'Uh oh, you got that question wrong. The correct answer was {trivia_answers[random_num_trivia]}')
                    playsound('WrongAnswerSound.wav')
                    question += 1
                    wrong += 1
                    excluded_from_randomT.append(random_num_trivia)

    if mode == 3:
        while question != 5:
            type_of_question = 2
            try:
                random_num_trivia = random.choice(list(set([x for x in range(1, 6)]) - set(excluded_from_randomT)))
            except IndexError:
                type_of_question = 1

            if type_of_question == 2:
                user_ans = input('\n' + trivia_questions[random_num_trivia] + ': ')
                if user_ans == trivia_answers[random_num_trivia]:
                    print("You're right!")
                    playsound('CorrectAnswerSound.wav')
                    score += 1
                    question += 1
                    excluded_from_randomT.append(random_num_trivia)
                else:
                    print(
                        f'Uh oh, you got that question wrong. The correct answer was {trivia_answers[random_num_trivia]}')
                    playsound('WrongAnswerSound.wav')
                    question += 1
                    wrong += 1
                    excluded_from_randomT.append(random_num_trivia)

        sleep(.5)
        print('\nNow time for the math!')

        while question >= 5 and question != 10:
            type_of_question = 1
            try:
                random_num_math = random.choice(list(set([x for x in range(1, 6)]) - set(excluded_from_randomM)))
            except IndexError:
                type_of_question = 2

            if type_of_question == 1:
                user_ans = int(input('\n' + math_questions[random_num_math] + ': '))
                if user_ans == math_answers[random_num_math]:
                    print("You're right!")
                    playsound('CorrectAnswerSound.wav')
                    score += 1
                    question += 1
                    excluded_from_randomM.append(random_num_math)
                else:
                    print(f'Uh oh, you got that question wrong. The correct answer was {math_answers[random_num_math]}')
                    playsound('WrongAnswerSound.wav')
                    wrong += 1
                    question += 1
                    excluded_from_randomM.append(random_num_math)


    def question_grammar(type0):
        if type0 != 1:
            question_gramm = 'questions'
        else:
            question_gramm = 'question'
        return question_gramm

    sleep(1)
    print(f'\nGood job on finishing the game {name}, you got {score} {question_grammar(score)} right and {wrong} {question_grammar(wrong)} wrong!')
    replay = input('Would you like to play the game again (Y or N)?: ')
    if replay == 'Y':
        question = 0

print('\nHave a good day! 💝')
