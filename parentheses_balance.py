"""
Given a string of parentheses, return whether or not the string is balanced.
Ex: "(())" returns True
    "((()" returns False
"""

def is_balanced(str_of_parens):
    count = [0, 0]
    if str_of_parens[0] == ")" or str_of_parens[-1] == "(":
        return False
    for char in str_of_parens:
        if char == "(":
            count[0] += 1
        elif char == ")":
            count[1] += 1
    return count[0] == count[1]


str1 = "()"
str2 = "(()())"
str3 = "(((()))())"

str4 = "((()"
str5 = ")()("
str6 = "()((()()()))()((()()())()"

print is_balanced(str1)
print is_balanced(str2)
print is_balanced(str3)
print is_balanced(str4)
print is_balanced(str5)
print is_balanced(str6)