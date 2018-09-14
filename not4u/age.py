name=input('what is your name?  ')
age = input('how old r u??  ')
age=int(age)
def function(name,age):
if age <=6:
	return (name + "! go to kinder garden")
elif age <=18:
	return (name +'! Welcome to school')
elif age <=22:
	return (name +'! Go to Univercity')
else:
	return (name + '! you have to work, you studied enough')
main = function(name,age)
print(main)