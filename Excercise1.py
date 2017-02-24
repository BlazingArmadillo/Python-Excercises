#The program recieves a sentence as input from the user. 
#It then proceeds to remove every exclamation mark in the sentence, except those at the end of the sentence.
#In the first line, the program reads an input from the user.
userstring=raw_input('Write a sentence that contains exclamation marks (!) wherever you like and at the end: ')
#It then checks if the sentence has at least one exclamation mark or is just exlamation marks and ,in case of the previous, prompt the user to correct their mistake.
#If there are no marks at all or if or no marks at the end there would be no problem, but the program would not be utilized for its purpose.
#If the sentence is just marks though, the program would crash. The reason will be explained further down.
while(userstring.count('!')==0 or userstring==len(userstring)*'!' or userstring[-1]!='!'):
	if(userstring.count('!')==0):
		userstring=raw_input('The sentence does not contain any exclamation marks(!). Please try again: ')
	elif(userstring==len(userstring)*'!'):
		userstring=raw_input('The sentence contains only exclamation marks. Please try again: ')
	else:
		userstring=raw_input('The sentence does not have exclamation marks at the end. Please try again: ')
#Instead of wasting time selectively removing the exclamation marks that we don't want, the program wil just count how many marks it should keep, how many marks are at the end of the sentence.
#It will start examining every single element of the sentence from the end of it to the beginning, until it finds a character that is not an exclamation mark.
#"i" is used both as and index to show a specific position in the sentence and a value that counts how many exclamation marks are at the end of the sentence,
#The default number of marks is 0.
i=0
#At this point, it starts becoming clear why the input cannot be just exclamation marks. If it was just marks, the "i" variable would  at some point indicate
#at a position that is out of the sentence's boundaries, because there would be not character different than '!' to cause the loop to stop. This would lead to a crash.
while(userstring[-(i+1)]=='!'):
	i+=1
#The number of exclamation marks is now saved in "i".
#The program will now make a list of the sentence's characters except the exclamation marks.
#Next, it will join the characters of the list, making a sentence that is the initial input without the exclamation marks.
#It will then give as output to the user that sentence along with as many exclamation marks as the initial sentence had in its end.
print ''.join(userstring.split('!'))+i*'!'
print 'Type "Exit" to quit the program.' #Prompts the user to type "Exit" to quit the program. The following loop helps in keeping the console on
#once the program has finished its job, so the user can see the result.
x=''
while(x!='Exit'):
	x=raw_input()