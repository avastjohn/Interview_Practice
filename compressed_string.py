""" 
Given a string of letters, compress to number of letters in a row that are the same. 
Example: turn "aabcccccaaa" into "a2b1c5a3"
    BUT if compressed string is not shorter than the original string, just return the original string
"""

string_1 = "aabcccccaaa"
string_2 = "aaaaabbcdddded"
string_3 = "abcde"
string_4 = "a"
"""My solution"""
# def compress(string):
#     compressed_str = ""
#     separated_letters = []
#     i = 0
#     while i < len(string):
#         j = i + 1
#         while j<len(string) and string[i] == string[j]:
#             if j < len(string):
#                 j += 1
#         letter_slice = string[i:j]
#         separated_letters.append(letter_slice)
#         i = j
#     # use list of separated letters to compress string
#     for item in separated_letters:
#         compressed_str += item[0]
#         compressed_str += str(len(item))
#     # figure out whether to return original string or compressed string
#     if len(string) < len(compressed_str):
#         return string
#     else:
#         return compressed_str

"""Christian's solution"""
def compress(s):
    current_letter = s[0]
    current_count = 1
    out = ""
    for i in range(1, len(s)):
        next_letter = s[i]
        if next_letter != current_letter:
            out += current_letter
            out += str(current_count)
            current_letter = next_letter
            current_count = 1
        current_count += 1
    out += current_letter
    out += str(current_count)
    if len(s) < len(out):
        return s
    else:
        return out

print compress(string_1)
print compress(string_2)
print compress(string_3)
print compress(string_4)


