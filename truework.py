# Libraries Included:
# Numpy, Scipy, Scikit, Pandas

# Given a string which is an operation in reverse polish notation, write a function that gives the exact (i.e. fractional) result of this expression.

# For example:
# "1/2 1/5 * 1 +" = "11/10"
# "1 1 + 1 +" = "3"
# "1 1 5 * +" = "6"

# When you get an operand, you push it onto a stack
# When you get an operator, you pop 2 elements from stack, do the operation and push back
# At the end only 1 token, you just pop that

# "1 1 + 1 +"
# []
# 1, stack: [1]
# 1, stack: [1, 1]
# +, stack: [2]
# 1, stack: [2, 1]
# +, stack: [3]
# return 3


# ((1/2*1/5) + 1)

# "1/1 1/5 * +" = "6"
# def multiply_fraction(a, b):
#     if '/' not in a:
#         a = "{}/1".format(a)
#     if '/' not in b:
#         b = "{}/1".format(b)
#     a, b = a.split("/"), b.split("/")
#     num_product = int(a[0])*int(b[0])
#     denom_product = int(a[1])*int(b[1])
#     return "{}/{}".format(num_product, denom_product)
#
# # n/p + q/r = (nr + qp) / pr
#
# def add_fraction(a, b):
#     if '/' not in a:
#         a = "{}/1".format(a)
#     if '/' not in b:
#         b = "{}/1".format(b)
#     a, b = a.split("/"), b.split("/")
#     num_sum, denom_sum = int(a[0])*int(b[1]) + int(b[0])*int(a[1]), (int(a[1])*int(b[1]))
#     return "{}/{}".format(num_sum, denom_sum)

from math import gcd
def simplify_fraction(numer, denom):

    if denom == 0:
        return "undefined"

    common_divisor = gcd(numer, denom)
    reduced_num, reduced_den = int(numer / common_divisor), int(denom / common_divisor)
    if reduced_den == 1:
        return "{}".format(reduced_num)
    else:
        return "{}/{}".format(reduced_num, reduced_den)

def process_fraction(a, b, operator):
    if '/' not in a:
        a = "{}/1".format(a)
    if '/' not in b:
        b = "{}/1".format(b)
    a, b = a.split("/"), b.split("/")
    if operator == '+':
        num, denom = int(a[0]) * int(b[1]) + int(b[0]) * int(a[1]), (int(a[1]) * int(b[1]))
    elif operator == '*':
        num, denom = int(a[0]) * int(b[0]), int(a[1]) * int(b[1])

    return simplify_fraction(num, denom)

def reverse_polish(string):
    string = string.split(" ")
    operators=['+', '*']
    stack = []
    for s in string:
        if s in operators:
            try:
                a, b = str(stack.pop()), str(stack.pop())
            except IndexError as err:
                print(err, "...invalid rpn expression")
                return

            if '/' in a or '/' in b:
                stack.append(process_fraction(a, b, s))
            else:
                if s == '+':
                    stack.append(int(a)+int(b))
                if s == '*':
                    stack.append(int(a)*int(b))
        else:
            stack.append(s)
    return str(stack[0])


print(reverse_polish("1/2 1/5 * 1 +") == "11/10")
print(reverse_polish("1 1 + 1 +") == '3')
print(reverse_polish("1/2 2 * 1") == '1')
print(reverse_polish("1 1 5 * +") == "6")
print(reverse_polish("4/10 2/3 + 1 +") == '31/15')


