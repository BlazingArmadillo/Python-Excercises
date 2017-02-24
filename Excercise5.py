#The program finds the Harshad numbers(integers that are divisible by the sum of their digits) and the numbers that are divisible by the product of 
#their digits from 0 to 1000 and then prints them.
#First, two empty lists are created where numbers of each type will be put.
harshad=[]
prodiv=[]
#In the following loop, "i" takes every value between 0 and 1000 and.
for i in xrange(1001):
	dsum=sum(int(j) for j in str(i)) #It calculates the sum of "i"'s digits
	dprod=1
	for y in str(i): #and also their product.
		dprod*=int(y)
	#It then checks if the number "i" belongs to any of the categories that we want to find their contents.
	#Both "if structures have a check to see if the division is possible at all, a.k.a. if the divisor is not zero."
	#So if the division is possible:
	if(dsum!=0 and i%dsum==0): #a)if the sum of "i"'s digits divides it, it's a Harshad number and is added to the "harshad" list.
		harshad.append(i)
	if(dprod!=0 and i%dprod==0): #b)if the product of "i"'s digits divides it, it is added to the "prodiv" list,
		prodiv.append(i)
#Finally, the program prints the two lists of numbers.
print 'Harshad numbers from 0 to 1000: ',harshad
print 'Numbers divisible by the product of their digits for 0 to 1000: ',prodiv
x=''
print 'Type "Exit" to quit the program.' #Asks the user to give the word "Exit" to quit the program. By, going into this loop, the program won't instantly close
#after finding the numbers, so the user can see them.
while(x!='Exit'):
	x=raw_input()