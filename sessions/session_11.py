from typing import List

def ex1(nested_list: List[List[int]]) -> None:
    for my_list in nested_list:
        for value in my_list:
            print(value)

my_matrix = [[0,1,2], [3,4,5], [6,7,8], [9,10,11]]
#  ex1(my_matrix)

#     *
#    ***
#   *****
#  *******

#*
#***
#*****
#*******

def stars(number_of_lines: int) -> None:
    t = 1
    for _ in range(0, number_of_lines):
        for _ in range(0, t):
            print("*", end="")
        t += 2
        print("")

#  stars(10)

FILEPATH = "/Users/luca.peric/Downloads/"
USER_FILE = FILEPATH + "users.txt"

def main():
    users_file = open(USER_FILE, "r")
    users = users_file.read()
    print(users)

class TheWorldIsEndingException(Exception):
    ...

try:
    ... # Exception, RecursionTimeout, TheWorldIsEndingException
except TheWorldIsEndingException:
    print("we hit an error!")
