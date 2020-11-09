def isfirstwordtitle(txt):
	allchars = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',' ']
	for char in allchars:
		if txt.startswith(char):
			return True
	return False
def islower(txt):
	allchars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',' ']
	for char1 in txt:
		for char in allchars:
			if char1 == char:
				c = True
				break
			else:
				c = False
		if not c:
			return False
	return True
def istitle(txt):
	for word in txt.split():
		if not isfirstwordtitle(word):
			return False
	return True
def isupper(txt):
	allchars = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',' ']
	for char1 in txt:
		for char in allchars:
			if char1 == char:
				c = True
				break
			else:
				c=False
		if not c:
			return False
	return True
def getupper(txt):
	line = 0
	allchars = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
	upperline = []
	for char in txt:
		line += 1
		if char in allchars:
			upperline.append(line)
	return upperline