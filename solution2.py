def solve(text,s): 
	result = "" 

	# traverse text 
	for i in range(len(text)): 
		char = text[i] 

		# For uppercase characters 
		if (char.isupper()): 
			result += chr((ord(char) + s-65) % 26 + 65) 

		# For lowercase characters 
		else: 
			result += chr((ord(char) + s - 97) % 26 + 97) 

	return result 

#steps to check  
text = "ABCXYZ"
s = 3
print ("Text : " + text)
print ("Shift : " + str(s))
print ("answer: " + solve(text,s))

