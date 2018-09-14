answers={
    "hi":"Hello",
    "how r u?":"Fine, n u?",
    "bye":"good bye, c u!"
}
def get_answer(question,answers):
    return answers.get(question)
def ask_user(answers):
    while True:
        user_input = input('сэй самсинк  ')
        answer=get_answer(user_input, answers)
        print(answer)
        if user_input == 'bye!':
            break
ask_user(answers)