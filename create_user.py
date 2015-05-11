
import re


def accountName():
	accountName = input('Please enter your prefered username: ')
	print('Your prefered username is', accountName)


def password():
	PW = 1
	while PW == 1:
		password = input('Please enter your password: ')
		print('Your password is', password)

		confirmPassword = input('Please confirm your password: ')
		if password == confirmPassword:
			break
			print('Your password was confirmed as', confirmPassword)
		else :
			print('Your password did not match')
 

def email():
	PW = 1
	while PW == 1:
		email = input('Please enter your email address: ')	
		if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
			print('the email address', email,' is not valid.')
		else:
			print("Happy days it's a good email!")
			break


if __name__ == '__main__':
	accountName()
	password()
	email()
	