# -*- coding: utf-8 -*-

"""
TESTS goes here
"""


from main import read_titanic#, general_get_desc

def test_get_desc_stats():
    # print(longestSubstring("abcdcca"))
    assert read_titanic()\
        .describe(include="all").\
        loc["count", "PassengerId"] == 891
    assert round(read_titanic().\
        describe(include="all").\
        loc["mean", "Survived"], 4) == 0.3838


if __name__ == "__main__":
    test_get_desc_stats()
    ## TODO generate summary statistics
    df = read_titanic()
    print(
        """
        Below are some summary statistics of variable `Survived` in the Titanic dataset
        """
    )
    df.describe(include="all")

    ## TODO one visualization