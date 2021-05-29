# ------------------------------------
def new_game():
    guesses = []
    correct_guess = 0
    question_num = 1

    for keys in questions:
        print('------------------------')
        print(keys)
        for i in options[question_num - 1]:
            print(i)

        guess = input("My answer is(a/b/c/d): ").upper()
        # This coule be used to check answers all at once
        guesses.append(guess)

        correct_guess += check_answer(questions.get(keys), guess)
        question_num += 1

    display_score(correct_guess, guesses)


# ------------------------------------
def check_answer(answer, guess):
    if answer == guess:
        print('CORRECT!')
        return 1
    else:
        print("WRONG!")
        return 0


# ------------------------------------
def display_score(correct_guess, guesses):
    print('------------------------')
    print('RESULTS')
    print('------------------------')
    print("Answers: ", end='')
    for i in questions:
        print(questions.get(i), end=' ')
    print()

    print("Guesses: ", end='')
    for i in guesses:
        print(i, end=' ')
    print()

    print('Your Score: ' + str(correct_guess * 100 / len(questions)) + '%')


# ------------------------------------
def play_again():
    response = input("Play Again?(y/n): ").upper()
    if response != 'Y':
        return False
    else:
        return True


# ------------------------------------

questions = {
    "who created Python?: ": "A",
    "What year was Python created?: ": "B",
    "Python is tributed to which comedy group?: ": "C",
    "Is the Earth round?: ": "A"
}

options = [["A. Guido van Rossum", "B. Elon Musk", "C. Bill Gates", "D. Mark Zuckerberg"],
           ["A. 1989", "B. 1991", "C. 2000", "D. 2016"],
           ["A. Lonely Island", "B. Smosh", "C. Monty Python", "D. SNL"],
           ["A. True", "B. False", "C. sometimes", "D. IDK"]]

new_game()

while play_again():  # play_again() == True
    new_game()

print('BYE!')
