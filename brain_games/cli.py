#!/usr/bin/env python3
import prompt

def welcome_user():
	user_name = prompt.string('May I have your name? ')	
	print(f'Hello, {user_name}!')
if __name__ == '__main__':
	welcome_user()
