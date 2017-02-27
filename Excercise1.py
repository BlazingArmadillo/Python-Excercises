#The program recieves a sentence as input from the user. 
#It then proceeds to remove every exclamation mark in the sentence, except those at the end of the sentence.
#The program first explains its purpose to the user and warns them about what input thy cannot give.
print 'The program will take from you a sentence that may have exclamation marks in it, and will remove all, but the ones at its end.'
print 'WARNING: The sentence cannot be a row of continuous exclamation marks!!!!!'
#The program asks the user to type in a sentence.
userstring=raw_input('Write a sentence that may contain exclamation marks wherever you like: ')
#It then checks if the user has given a forbidden input, a row of continuous exclamation marks. The reason that the user should not give this as an input is explained further down.
while(userstring==len(userstring)*'!'):
	print 'Wrong input. The sentence you gave is a row of continuous exclamation marks. Please try again.'
	userstring=raw_input()
#Instead of wasting time selectively removing the exclamation marks that we don't want, the program wil just count how many marks it should keep, how many marks are at the end of the sentence.
#It will start examining every single element of the sentence from the end of it to the beginning, until it finds a character that is not an exclamation mark.
#"i" is used both as and index to show a specific position in the sentence and a value that counts how many exclamation marks are at the end of the sentence.
i=0
#At this point, it starts becoming clear why the input cannot be just exclamation marks. If it was just marks, the "i" variable would  at some point indicate
#at a position that is out of the sentence's boundaries, because there would be not character different than '!' to cause the loop to stop. This would lead to a crash.
while(userstring[-(i+1)]=='!'):
	i+=1
#The number of exclamation marks is now saved in "i".
#The program will now make a list of the sentence's characters except the exclamation marks.
#Next, it will join the characters of the list, making a sentence that is the initial input without the exclamation marks.
#It will then give as output to the user that sentence along with as many exclamation marks as the initial sentence had at its end.
print ''.join(userstring.split('!'))+i*'!'
print 'Type "Exit" to quit the program.' #Prompts the user to type "Exit" to quit the program. The following loop helps in keeping the console on
#once the program has finished its job, so the user can see the result.
x=''
while(x!='Exit'):
	x=raw_input()