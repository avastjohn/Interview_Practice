"""
Given two sorted arrays A and B, where A has enough space alotted to hold all of B, merge the two arrays into A
"""

def merge_arrays(A, B):
    marker_a = len(A) - 1 - len(B)
    marker_b = len(B) - 1
    i = len(A) - 1
    while marker_a >= 0 and marker_b >= 0:
        if A[marker_a] > B[marker_b]:
            A[i] = A[marker_a]
            marker_a -= 1
        else:
            A[i] = B[marker_b]
            marker_b -= 1
        i -= 1
    if marker_a <= 0:
        if marker_b == 0:    
            A[0] = B[0]
        else: # if marker_b doesn't equal 0
            for x in range(marker_b):
                A[x] = B[x]
    return A


A1 = [1,7,9,10,11,12,None,None,None,None]
B1 = [13,14,14,71]
A2 = [14,15,17,None,None,None,None]

print merge_arrays(A1, B1)
print merge_arrays(A2, B1)