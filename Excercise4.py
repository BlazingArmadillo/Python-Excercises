#The program finds the standard deviation of a list of numbers given by the user, without using the 2 smallest and the 2 largest numbers given by the user.
#It is made in a way to provide a quite foolproof and interactive user experience.
#Variable initialization.
nums=[] #Creates a list that the numbers given by the user will be put into.
num='' #This variable saves the user's input each time, so it can be examined and/or put into the number list.
i=0 #Utility variable that count how many numbers the user has put into the list.
error=0 #Utility variable that saves if the user has made an error at a specific part of the program.
#The program asks the user to provide at least 5 numbers. It is five because the program can't operate with less. The reason will be explained further down.
#The user can stop giving numbers by typing "Done". "Done" will be accepted only if the user has given the five required numbers.
print 'Give a list of at least five numbers that you want to find their standard deviation. When you have given as many number as you wanted, give the word "Done" input.'
while(num!='Done'):
	if(i==5 and error==1):
		#The message below is shown after the fifth entry by the user, only if "Done" has been typed before entering the five required numbers.
		#It's purpose is to inform the careless users about when they are finally able to stop giving numbers.
		print 'You can now stop giving numbers by typing the word "Done".'
	num=raw_input() #Reads user input. According to the flow of the program, it can be either a number or the word "Done".
	if(num=='Done' and i<5): #This "if" structure checks if the user has entered "Done" before first giving five numbers and prompts them to give a valid value.
		while(num=='Done'):
			#The message here is dynamic. If the user has never done this mistake before, the program shows them a more complete message,
			#explaining why their input is wrong. If they do it again, it gives shorter message.
			if(error==0):
				print 'You cannot stop giving numbers yet as you have not given enough numbers. Please give a number.'
				error+=1
			else:
				print 'Your input is not a number. Please try again.'
			num=raw_input()
	#The following "if" structure makes sure that if the input is not "Done", it at least is a number.
	#It does that by trying to create the float form of the user input. If it fails to do so, the program prompts the user to give a valid value.
	if(num!='Done'):
		isnum=False
		while(isnum==False):
			try:
				float(num)
				isnum=True
			except:
				isnum=False
				#The message is dynamic so after the 5 required number entries the user can also be indirectly reminded that they can also stop giving numbers.
				if(i<5):
					print 'Your input is not a number. Please try again.'
				else:
					print 'Your input is neither a number or an exit command. Please try again.'
				num=raw_input()
		nums.append(float(num)) #After securing that the input is a number, the program puts its float form in a list.
	i+=1
import numpy #Imports the "numpy" library to use its standard deviation function.
#The program first sorts the number list and then finds and prints the standard deviation of its numbers without taking into account the 2 first and the 2 last ones.
#The fact that it requires 4 numbers to not use, creates the requirement for the program to recieve at least 5 numbers from the user, 
#so it can remove the 4 of them and still have numbers to execute the standard deviation function with.
print 'The standard deviation of the numbers you gave is:', numpy.std(sorted(nums)[2:-2])
x=''
print 'Type "Exit" to quit the program.' #Asks the user to give the word "Exit" to quit the program. By, going into this loop, the program won't instantly close
#after finding the standard deviation and the user will be able to see the result.
while(x!='Exit'):
	x=raw_input()




			
			
	
