import prompt

def welcome_user():
    print('Welcome to the Brain Games!')
    print('Hello, {}!'.format(prompt.string('May I have your name? ')))