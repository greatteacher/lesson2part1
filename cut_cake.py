parts=input('на сколько делим???')
def cut_cake(parts):
    try:
        return 1/int(parts)
    except (ZeroDivisionError, ValueError, TypeError):
        return "С ума посходили? я работаю с цифрами, can't devide by 0!!"
print(cut_cake(parts))
