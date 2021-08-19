"""
Read README.md for explaining about problems in realisation
"""


def fizz_buzz(string):
	"""
	At first function checks: has a string more than one words or not.
	Then 'string' will be converted to list which function checks by iterations.
	"""

	if ' ' in string:
		lst = string.lower().split(' ')
	else:
		lst = [string.lower()]

	new_string = ''
	n = len(lst)

	for x in range(n):
		micro_n = len(lst[x])
		if (x + 1) % 3 == 0:
			lst[x] = 'Fizz'
			new_string += lst[x]
			new_string += ' '  # for space between words

		elif micro_n >= 5:
			new_word = ''
			for y in range(micro_n):
				if (y + 1) % 5 == 0:
					new_word += 'Buzz'
					continue
				new_word += lst[x][y]
			new_string += new_word
			new_string += ' '

		else:
			new_string += lst[x]
			new_string += ' '

	new_string = new_string[:len(new_string)-1]  # delete space in the end of new_string

	return new_string


class FizzBuzzDetector:

	def __init__(self, string):
		if isinstance(string, str):
			if 7 <= len(string) <= 100:
				self.new_string = fizz_buzz(string)
				self.countFizz = 0
				self.countBuzz = 0
			else:
				raise ValueError('Invalid length of input string. Length must be: 7 <= string <= 100.')
		else:
			raise TypeError('Type of input value is not a string.')

	def getOverlappings(self):
		import re
		pattern1 = r'Fizz'
		pattern2 = r'Buzz'

		result1 = re.findall(pattern1, self.new_string)
		if result1:
			self.countFizz = len(result1)

		result2 = re.findall(pattern2, self.new_string)
		if result2:
			self.countBuzz = len(result2)

		return f'"Fizz" in string - {self.countFizz}, "Buzz" in string - {self.countBuzz}'




