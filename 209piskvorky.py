hernipole = 20*"-"

def vyhodnot(pole):
	"""funkce vyhodnoti stav herniho pole"""
	if "xxx" in pole:
		return("x")
	elif "ooo" in pole:
		return("o")
	elif "-" not in pole:
		return("!")
	else:
		return("-")

print(vyhodnot(hernipole))
