"""
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
"""


def count_th(word):

    # keep track of hits here
    counter = 0
    # print(f"\n0 = {word[0]} || 1 = {word[1]} || word = {word} || counter = {counter}\n")

    # base case: word must be at least 2 letters long
    if len(word) <= 1:
        return 0

    # if length of word is > 1 && 'th' is present, increment counter
    elif word[0] == "t" and word[1] == "h":
        counter += 1
        # print(
        #     f"\n0 = {word[0]} || 1 = {word[1]} || word = {word} || counter = {counter}\n"
        # )

    # run again, moves 1 letter left
    return count_th(word[1:]) + counter


# count_th("abcthxyz")
# count_th("thhtthht")
