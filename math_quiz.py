def ask_question(question, answer):
    user_answer = int(input(question))
    if user_answer == answer:
        return True
    else:
        return False


def quiz():
    score = 0
    question1 = ask_question("What is 3 + 5? ", 8)
    question2 = ask_question("What is 9 - 4? ", 5)
    question3 = ask_question("What is 6 + 7? ", 13)
    if question1 is True:
        score += 1
    if question2 is True:
        score += 1
    if question3 is True:
        score += 1

    print(f"Your total score is: {score}/3")


quiz()
