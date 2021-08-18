"""
Read README.md for explaining about problems in realisation
"""


def fizz_buzz(string):
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
			new_string += ' '

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

	new_string = new_string[:len(new_string)-1]

	return new_string


class FizzBuzzDetector:

	def getOverlappings(self, string):
		if isinstance(string, str):
			if 7 <= len(string) <= 100:
				self.new_string = fizz_buzz(string)
				self.countFizz = self.new_string.count('Fizz')
				self.countBuzz = self.new_string.count('Buzz')
			else:
				raise ValueError('Invalid length of input string. Length must be: 7 <= string <= 100.')
		else:
			raise TypeError('Type of input value is not a string.')

		return self.new_string


