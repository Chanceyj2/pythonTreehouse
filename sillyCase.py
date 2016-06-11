# coding: utf-8
def sillyCase(item):

	half = int(round(len(item) / 2))
	
	lowerString = item[:half].lower()
	upperString = item[half:].upper()

	return(lowerString + upperString)

a = "Treehouse"

b = sillyCase(a) 

print(b)
print(a)