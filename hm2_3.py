# --------------
# User Instructions
#
# Write a function, longest_subpalindrome_slice(text) that takes
# a string as input and returns the i and j indices that
# correspond to the beginning and end indices of the longest
# palindrome in the string.
#
# Grading Notes:
#
# You will only be marked correct if your function runs
# efficiently enough. We will be measuring efficency by counting
# the number of times you access each string. That count must be
# below a certain threshold to be marked correct.
#
# Please do not use regular expressions to solve this quiz!


def longest_subpalindrome_slice(text):
    """Return (i, j) such that text[i:j] is the longest palindrome in text.
    Notes:
    1. Case-insensitive. eg: 'Abcba' is a palindrome
    2. Space matters. eg: 'abcd cba'is not a palindrome but 'abc d cba' is a palindrome
    3. For this exercise, text will not include character other than ascii letter and space.
    """
    text = text.lower()

    i, j, longest = 0, 0, 0
    longest_palindrome = ''

    for m in range(1, len(text)):
        k = 1
        while m - k >= 0 and m + k - 1 < len(text) - 1:
            left = text[m - k]
            right = text[m + k]
            if left == right:
                k = k + 1
            else:
                break
        left_index = m - (k - 1)
        right_index = m + (k - 1)
        palindrome = text[left_index: right_index + 1]
        length = right_index - left_index + 1

        longest, longest_palindrome, i, j = check_longest(
            length, palindrome, left_index, right_index, longest, longest_palindrome, i, j)

        k = 1
        if text[m] == text[m - k]:
            while m - 1 - k >= 0 and m + k - 1 < len(text) - 1:
                left = text[m - 1 - k]
                right = text[m + k]
                if left == right:
                    k = k + 1
                else:
                    break
            left_index = (m - 1) - (k - 1)
            right_index = m + (k - 1)
            palindrome = text[left_index: right_index + 1]
            length = right_index - left_index + 1

        longest, longest_palindrome, i, j = check_longest(
            length, palindrome, left_index, right_index, longest, longest_palindrome, i, j)

    return (i, j)


def check_longest(length, palindrome, left_index, right_index, longest, longest_palindrome, i, j):

    if length > longest:
        longest = length
        longest_palindrome = palindrome
        i = left_index
        j = right_index + 1

    return longest, longest_palindrome, i, j


def test():
    L = longest_subpalindrome_slice
    assert L('racecar') == (0, 7)
    assert L('Racecar') == (0, 7)
    assert L('RacecarX') == (0, 7)
    assert L('Race carr') == (7, 9)
    assert L('') == (0, 0)
    assert L('something rac e car going') == (8, 21)
    assert L('xxxxx') == (0, 5)
    assert L('Mad am I ma dam.') == (0, 15)
    return 'tests pass'


print(test())
