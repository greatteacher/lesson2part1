a = input ('Введите pincode а:')
b = input ('Введите pincode ещё раз b:')

def function(a, b):
    if not (isinstance(a, str) and isinstance(b, str)):
        return '0  это не строковые'
    
    elif a == b:
        return  '1 oll Korrect'

    elif len(a) > len(b):
        return "2 not enough symbols"

    elif not ((a == b) and b == 'learn'):
        return 3
    else:
        return 'Введены неверные данные'
main = function(a, b)
print(main)