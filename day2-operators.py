#!/bin/python

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(meal_cost, tip_percent, tax_percent):
    tip_value=meal_cost/100*tip_percent
    tax_value=meal_cost/100*tax_percent
    return(int(round(meal_cost+tip_value+tax_value)))

if __name__ == '__main__':
    meal_cost = float(raw_input())

    tip_percent = int(raw_input())

    tax_percent = int(raw_input())

    print(solve(meal_cost, tip_percent, tax_percent))
