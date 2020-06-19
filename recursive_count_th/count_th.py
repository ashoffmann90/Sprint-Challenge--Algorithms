'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):
    # create counter
    th = 0
    # base cases
    # if there can't be any 'th'
    if len(word) < 2:
        return th
    # if 'there can be only one'
    if word[0: len('th')] == 'th':
        th = 1 + count_th(word[1:])
        return th
    # if there can be more than one
    else:
        th = count_th(word[1:])
        return th


print(count_th("othothothothothotho"))
