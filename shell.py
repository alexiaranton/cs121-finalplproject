import sawa

while True:
	text = input('Sawa >>> ')
	if text.strip() == "": continue
	result, error = sawa.run('<SAWA>', text)

	if error:
		print(error.as_string())
	elif result:
		if len(result.elements) == 1:
			print(repr(result.elements[0]))
		else:
			print(repr(result))
