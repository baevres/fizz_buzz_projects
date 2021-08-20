In realisation appeared next question:  P.s.: I will refer to number of requirements which I rewrite in test.py
1) requirement "7 <= s <= 100":
1.1) There are number of input string or number of words in string must be match to requirement?
1.2) If input data don`t match to requirement, is it need to call exception?
1.3) Is it need to take into consider situation when input data is not a string?
My answer:
1.1) on input gives string.
1.2) if string don`t match to requirement will called exception ValueError with message: 'Invalid length of input string. Length must be: 7 <= string <= 100.'.
1.3) if input data is not a string will called exception TypeError with message: 'Type of input value is not a string.'.

2) requirement "string contain only lowercase letters":
2.1) 'Fizz' and 'Buzz' in new string must have lowercase letters too or not?
My answer:
2.1) 'Fizz' and 'Buzz' will have uppercase letters as in requirements (3) and (4).

3) requirements "every third word replaced on 'Fizz'" and "every third word replaced on 'Fizz'":
3.1) what do have bigger priority - operation 'Fizz' or 'Buzz' if word to match both requirements?
3.2) if there are any symbol (.,?!"' etc) near word and word replaced to 'Buzz' - need to save symbol?
My answer:
3.1) operation 'Fizz' have bigger priority as it indicated first.
3.2) any symbols won`t be saved as it don`t need in requirements.

4) requirement about method 'getOverlappings' - I didn`t understand next part: "method must return number OR coincidences for incoming string".
May be means "method must return number OF coincidences for incoming string"?
My answer: method 'getOverlappings' return number OF coincidences for incoming string.
