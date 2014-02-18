"""Input a string, return the reverse of that string"""


def reverse_string(stringy):
    reversed_stringy = []
    for i in range(len(stringy)):
        temp = stringy[-1 -i]
        reversed_stringy.append(temp)
    return ("").join(reversed_stringy)



stringy = "You like poop"

print reverse_string(stringy)