# -*- coding: utf-8 -*-
"""
Student ID: A00291231
"""

from assignment_a import number_of_values, total_height, calc_mean, calc_median, calc_mode, calc_max, calc_min, calc_std_dev, calc_iqr, calc_skewness, calc_correlation
        

def test_number_of_values():
    assert number_of_values([1,2,3]) == 3
def test_total_height():
    assert total_height([1,2,3]) == 6
def test_calc_mean():
    assert calc_mean([2,3,4]) ==  3
def test_calc_median():
    assert calc_median([2,3,4,5]) == 3.5
def test_calc_mode():
    assert calc_mode([1,2,3,2,5]) == 2
def test_calc_max():
    assert calc_max([1,2,3]) == 3
def test_calc_min():
    assert calc_min(([1,2,3])) == 1
def test_calc_std_dev():
    assert calc_std_dev([1,2,3]) == 1
def test_calc_iqr():
    assert calc_iqr([1,2,3,4]) == 2
def test_calc_skewness():
    assert calc_skewness([1,2,3]) == (1.00,0.0)
def test_calc_correlation():
    assert calc_correlation([1,2,3], [1,2,3]) == 1