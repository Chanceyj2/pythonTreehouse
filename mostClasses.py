# coding: utf-8
def most_classes(school_dict):
	count = 0
	flag = 0 
	teacher_list = []
	
	for key in school_dict:
		teacher_list.append(key)
	
	for value in school_dict.values():
		if len(value) > count:
			count = len(value)
			flag += 1

	return(teacher_list[flag-1])

def stats(school_dict):
	y = []
	
	for key in school_dict:
		y.append([key, len(school_dict[key])])
		
	return(y)

def courses(school_dict):
	j = []
	
	for value in school_dict.values():
		j += value
		
	return(j)
	
x = {'Jonathan': ['python', 'java', 'html'], 'Kenneth': ['python', 'css'], 'Abby': ['Python', 'java']}

a = most_classes(x)
b = stats(x)
c = courses(x)
print(a)
print(b)
print(c)