Voc_Ella = {'как дела?': 'хорошо!', 'что делаешь?': 'иду к бабушке', 
'ты человек?': 'как посмотреть', 'где ты живешь?': 'в лесу',
'как тебя зовут?': 'Красная шапочка', 'что ты несешь?': 'Пирожки', 
'why do java developers wear glasses?': 'because they don"t C#'}

def ask_user ():
    while True:
        user_say = (input ('О чем вы хотите спросить? ')).lower ()
        reply = Voc_Ella.get (user_say)
        if reply != None:
            print (reply)    
ask_user ()