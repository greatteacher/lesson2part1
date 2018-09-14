while True:
    user_say = input('Как дела?  ')
    if user_say == 'Хорошо!':
        print('Это хорошо, что хорошо!')
        break
    else:
        print('И всё же, помимо {}'.format(user_say))
while True:
    user_say2 = input('Чем занят?  ')
    if user_say2 == 'Программирую':
        print('Это хорошо, что программируешь! ')
        break
    else:
        print('Я так и знал!, я тоже {}'.format(user_say2),'а ещё что?')

 