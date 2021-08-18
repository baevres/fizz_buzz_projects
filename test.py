"""
Requirements:
1) length of input string: 7 <= string <= 100
2) string contain only lowercase letters
3) every third word replaced on 'Fizz'
4) every fifths letter in word (if len(word) >= 5) replaced on 'Buzz'

This module has 3 positive and 3 negative tests.
Positive tests contain requirements:
1) (1), (2), (4); len(string) == 7
2) (1), (2), (3) and (4); len(string) == 100
3) (1), (2), (3) and (4); len(string) == 53

Negative tests contain requirements:
1) (1); len(string) == 6
2) (1); len(string) == 101
3) input data must be str; extra requirement
"""

import pytest
from FizzBuzz import FizzBuzzDetector, fizz_buzz


positive_params = [('SpeCiaL', 'specBuzzal'),
                   ('Giulietta will always love Romeo. Story about tragic love everyone knows because people likes sames.',
                    'giulBuzzetta will Fizz love romeBuzz. Fizz abouBuzz tragBuzzc Fizz everBuzzone knowBuzz Fizz peopBuzze likeBuzz Fizz'),
                   ('Special_special works_works something unusual_unusual',
                    'specBuzzal_sBuzzeciaBuzz workBuzz_worBuzzs Fizz unusBuzzal_uBuzzusuaBuzz')]
positive_ids = ['len == 7', 'len == 100', 'len == 53']

negative_params = [('OriGIn', 'Invalid length of input string. Length must be: 7 <= string <= 100.'),
                   ('Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt utte labore',
                    'Invalid length of input string. Length must be: 7 <= string <= 100.',
                    )]
negative_ids = ['len == 6', 'len == 101']

second_negative_param = (1234765, 'Type of input value is not a string.')


def setup_cls(cls):
    instance = cls()
    return instance


@pytest.fixture(scope='function',
                params=positive_params,
                ids=positive_ids)
def positive_params_test(request):
    return request.param


def test_positive(positive_params_test):
    inst = setup_cls(FizzBuzzDetector)
    (input_string, expected_string) = positive_params_test
    result = inst.getOverlappings(input_string)
    print(f'input: {input_string}, expected: {expected_string}, result: {result}')
    assert result == expected_string


@pytest.fixture(scope='function',
                params=negative_params,
                ids=negative_ids)
def negative_params_test(request):
    return request.param


def test_negative(negative_params_test):
    inst = setup_cls(FizzBuzzDetector)
    (input_string, expected_string) = negative_params_test
    with pytest.raises(ValueError) as exc:  # exc => exception
        result = inst.getOverlappings(input_string)
    exc_message = exc.value.args[0]
    print(f'input: {input_string}, expected: {expected_string}, result: {exc_message}')
    assert exc_message == expected_string


def test_second_negative():
    inst = setup_cls(FizzBuzzDetector)
    (input_string, expected_string) = second_negative_param
    with pytest.raises(TypeError) as exc:
        result = inst.getOverlappings(input_string)
    exc_message = exc.value.args[0]
    print(f'input: {input_string}, expected: {expected_string}, result: {exc_message}')
    assert exc_message == expected_string