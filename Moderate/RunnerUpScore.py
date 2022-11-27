"""
# Given the participants' score sheet for your University Sports Day,
# you are required to find the runner-up score.
# You are given  scores. Store them in a list and find the score of the runner-up.

1) ask the user for score input
2) make a list
3) find maximum element in list by using max() and its index by using index().
4) pop the maximum element by using pop() and make new list.
5) again find maximum element in new list .
6) print runners up score

"""


def compute_runnerUp_Score(scores):
    """
    function for runnerUp Score
    """

    x = scores.index(max(scores))

    scores.pop(x)

    z = max(scores)
    return z


def main():
    scores = [45, 24, 56, 87, 95, 52]
    runnerUp_Score = compute_runnerUp_Score(scores)

    print(f"the runner up score is {runnerUp_Score}")


main()
