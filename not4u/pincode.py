line=input('введите свой пинкодище  ')
a=type(line)
if a !=str:
	print('O no no no')
t1=input('введите свой пинкод  ')
t1=str(t1)

t2=input(' повторишь свой пинкод? ')
t2=str(t2) 
if t1 == t2:
    print('попал')
else:
    print('попробуй в другой раз, у тебя получится')