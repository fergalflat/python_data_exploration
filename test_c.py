# -*- coding: utf-8 -*-
"""
Student ID: A00291231
"""

from assignment_c import earliest_date, latest_date, date_high_value, date_low_value, average_value

def test_earliest_date():
    assert earliest_date({"1961-03-17":2, "1977-03-17":5}) == "1961-03-17"
def test_latest_date():
    assert latest_date({"1961-03-17":2, "1977-03-17":5}) =="1977-03-17"
def test_date_high_value():
    assert date_high_value({"1961-03-17":2, "1977-03-17":5}) == "1977-03-17"
def test_date_low_value():
    assert date_low_value({"1961-03-17":2, "1977-03-17":5}) == "1961-03-17"
def test_average_value():
    assert average_value({"1961-03-18":2, "1961-03-17":4}) == 3