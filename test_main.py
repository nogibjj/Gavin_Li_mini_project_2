# -*- coding: utf-8 -*-

"""
TESTS goes here
"""


from main import get_desc_stats#, general_get_desc

def test_get_desc_stats():
    # print(longestSubstring("abcdcca"))
    assert get_desc_stats().loc["count", "PassengerId"] == 891
    assert round(get_desc_stats().loc["mean", "survived"], 4) == 0.3838


# test_main()