name=input('what is your name?  ')
age = input('how old r u??  ')
age=int(age)
if age <=6:
	print(name + "! go to kinder garden")
elif age <=18:
	print(name +'! Welcome to school')
elif age <=22:
	print(name +'! Go to Univercity')
elif age <= 65:
	print(name + '! you have to work, you studied enough')
else:
	print(name + '! you do not have to work, or study, only die, ')
	print('coz you are to old, but retirement canceled in Russia at all')