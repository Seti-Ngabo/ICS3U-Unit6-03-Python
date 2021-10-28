#!/usr/bin/env python3

# Created by: Seti Ngabo
# Created on: Oct 2021
# This program print 10 random numbers and the smallest number

import random


def lowest_number(randoms):
    # This function calculate smallest number
    second_each_loop = 0
    max_number = 50

    for second_each_loop in randoms:
        if second_each_loop < max_number:
            max_number = second_each_loop

    return max_number


def main():
    # This function shows the smallest number
    numbers = []
    final_lowest = 0
    each_loop = 0

    for each_loop in range(0, 10):
        random_numbers = random.randint(0, 50)
        numbers.append(random_numbers)
        print("The random number {0} is: {1}".format(each_loop + 1, random_numbers))

    # call function
    final_lowest = lowest_number(numbers)

    # output
    print("")
    print("The smallest number is: {0}".format(final_lowest))

    print("\nDone.")


if __name__ == "__main__":
    main()
