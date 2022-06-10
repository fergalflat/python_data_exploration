# -*- coding: utf-8 -*-
"""
Student ID: A00291231
"""

from assignment_b import number_of_categories, highest_number_of_values, lowest_number_of_values, highest_total, lowest_total

def test_number_of_categories():
    assert number_of_categories({1,2,3}) == 3
def test_highest_number_of_values():
    assert highest_number_of_values({"1":[2,3],"2":[3,4,5]}) == "2"
def test_lowest_number_of_values():
    assert lowest_number_of_values({"1":[2,3],"2":[3,4,5]}) == "1"
def test_highest_total():
    assert highest_total({"1":[44],"2":[555]}) == "2"
def test_lowest_total():
    assert lowest_total({"1":[44],"2":[555]}) == "1"